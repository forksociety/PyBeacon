#!/usr/bin/env python3
#
# Copyright 2015 Opera Software ASA. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Python script for scanning and advertising urls over Eddystone-URL.
"""
import re
import os
import signal
import subprocess
import sys
import time
import argparse
from . import __version__
from pprint import pprint
from enum import Enum

application_name = 'PyBeacon'
version = __version__ + 'beta'


if (sys.version_info > (3, 0)):
    DEVNULL = subprocess.DEVNULL
else:
    DEVNULL = open(os.devnull, 'wb')

# The default url
defaultUrl = "https://goo.gl/SkcDTN"

# The default uid
defaultUid = "01234567890123456789012345678901"

schemes = [
        "http://www.",
        "https://www.",
        "http://",
        "https://",
        ]


class Eddystone(Enum):
    uid = 0x00
    url = 0x10
    tlm = 0x20


extensions = [
        ".com/", ".org/", ".edu/", ".net/", ".info/", ".biz/", ".gov/",
        ".com", ".org", ".edu", ".net", ".info", ".biz", ".gov",
        ]

parser = argparse.ArgumentParser(prog=application_name, description= __doc__)
group = parser.add_mutually_exclusive_group()

group.add_argument("-u", "--url", nargs='?', const=defaultUrl, type=str,
                    default=defaultUrl, help='URL to advertise.')
group.add_argument("-i", "--uid", nargs='?',  type=str,
                    const=defaultUid, help='UID to advertise.')
parser.add_argument('-s','--scan', action='store_true',
                    help='Scan for URLs.')
parser.add_argument('-t','--terminate', action='store_true',
                    help='Stop advertising URL.')
parser.add_argument('-o','--one', action='store_true',
                    help='Scan one URL only.')
parser.add_argument("-v", "--version", action='store_true',
                    help='Version of ' + application_name + '.')
parser.add_argument("-V", "--Verbose", action='store_true',
                    help='Print lots of debug output.')

args = parser.parse_args()

def verboseOutput(text = ""):
    if args.Verbose:
        sys.stderr.write(text + "\n")


def encodeurl(url):
    i = 0
    data = []

    for s in range(len(schemes)):
        scheme = schemes[s]
        if url.startswith(scheme):
            data.append(s)
            i += len(scheme)
            break
    else:
        raise Exception("Invalid url scheme")

    while i < len(url):
        if url[i] == '.':
            for e in range(len(extensions)):
                expansion = extensions[e]
                if url.startswith(expansion, i):
                    data.append(e)
                    i += len(expansion)
                    break
            else:
                data.append(0x2E)
                i += 1
        else:
            data.append(ord(url[i]))
            i += 1

    return data


def encodeUid(uid):
    if not uidIsValid(uid):
        raise ValueError("Invalid uid. Please specify a valid 16-byte (e.g 32 hex digits) hex string")
    ret = []
    for i in range(0, len(uid), 2):
        ret.append(int(uid[i:i+2], 16))
    ret.append(0x00)
    ret.append(0x00)
    return ret


def uidIsValid(uid):
    if len(uid) == 32:
        try:
            int(uid, 16)
            return True
        except ValueError:
            return False
    else:
        return False


def encodeMessage(data, beacon_type=Eddystone.url):
    if beacon_type == Eddystone.url:
        payload = encodeurl(data)
    elif beacon_type == Eddystone.uid:
        payload = encodeUid(data)
    encodedmessageLength = len(payload)

    verboseOutput("Encoded message length: " + str(encodedmessageLength))

    if encodedmessageLength > 18:
        raise Exception("Encoded url too long (max 18 bytes)")

    message = [
            0x02,   # Flags length
            0x01,   # Flags data type value
            0x1a,   # Flags data

            0x03,   # Service UUID length
            0x03,   # Service UUID data type value
            0xaa,   # 16-bit Eddystone UUID
            0xfe,   # 16-bit Eddystone UUID

            5 + len(payload), # Service Data length
            0x16,   # Service Data data type value
            0xaa,   # 16-bit Eddystone UUID
            0xfe,   # 16-bit Eddystone UUID

            beacon_type.value,   # Eddystone-url frame type
            0xed,   # txpower
            ]

    message += payload

    return message

def decodeUrl(encodedUrl):
    """
    Decode a url encoded with the Eddystone (or UriBeacon) URL encoding scheme
    """

    decodedUrl = schemes[encodedUrl[0]]
    for c in encodedUrl[1:]:
        if c <= 0x20:
            decodedUrl += extensions[c]
        else:
            decodedUrl += chr(c)

    return decodedUrl


def resolveUrl(url):
    """
    Follows redirects until the final url is found.
    """

    try:
        if (sys.version_info > (3, 0)):
            import http.client
            import urllib.parse

            parsed = urllib.parse.urlsplit(url)

            conn = None
            if parsed.scheme == "https":
                conn = http.client.HTTPSConnection(parsed.netloc)
            elif parsed.scheme == "http":
                conn = http.client.HTTPConnection(parsed.netloc)

            path = parsed.path
            if parsed.query:
                path += "&" + parsed.query

            conn.request("HEAD", path)
            response = conn.getresponse()
        else:
            import httplib
            import urlparse

            parsed = urlparse.urlparse(url)
            h = httplib.HTTPConnection(parsed.netloc)
            h.request('HEAD', parsed.path)
            response = h.getresponse()

        if response.status >= 300 and response.status < 400:
                return resolveUrl(response.getheader("Location"))
        else:
                return url

    except:
        return url


def onUrlFound(url):
    """
    Called by onPacketFound, if the packet contains a url.
    """

    url = resolveUrl(url)
    sys.stdout.write("\n/*          Eddystone-URL         */\n")
    sys.stdout.write(url)
    sys.stdout.write("\n")
    sys.stdout.flush()


foundPackets = set()


def onUidFound(bytearray):
    print("\n/*       Eddystone-UID      */")
    namespace = ("".join(format(x, '02x') for x in bytearray[0:10]))
    instance = ("".join(format(x, '02x') for x in bytearray[10:16]))
    print("Namspace: {}\nInstance: {}\n".format(namespace, instance))


def onPacketFound(packet):
    """
    Called by the scan function for each beacon packets found.
    """

    data = bytearray.fromhex(packet)

    if args.one:
        tmp = packet[:-3]
        if tmp in foundPackets:
            return
        foundPackets.add(tmp)

    # Eddystone
    if len(data) >= 20 and data[19] == 0xaa and data[20] == 0xfe:
        serviceDataLength = data[21]
        frameType = data[25]

        # Eddystone-URL
        if frameType == Eddystone.url.value:
            onUrlFound(decodeUrl(data[27:22 + serviceDataLength]))
        elif frameType == Eddystone.uid.value:
            onUidFound(data[27:22 + serviceDataLength])
        elif frameType == Eddystone.tlm.value:
            verboseOutput("Eddystone-TLM")
        else:
            verboseOutput("Unknown Eddystone frame type: {}".format(frameType))

    # UriBeacon
    elif len(data) >= 20 and data[19] == 0xd8 and data[20] == 0xfe:
        serviceDataLength = data[21]
        verboseOutput("UriBeacon")
        onUrlFound(decodeUrl(data[27:22 + serviceDataLength]))

    else:
        verboseOutput("Unknown beacon type")

    verboseOutput(packet)
    verboseOutput()


def scan(duration = None):
    """
    Scan for beacons. This function scans for [duration] seconds. If duration
    is set to None, it scans until interrupted.
    """

    print("Scanning...")
    subprocess.call("sudo hciconfig hci0 reset", shell = True, stdout = DEVNULL)

    lescan = subprocess.Popen(
            ["sudo", "-n", "hcitool", "lescan", "--duplicates"],
            stdout = DEVNULL)

    dump = subprocess.Popen(
            ["sudo", "-n", "hcidump", "--raw"],
            stdout = subprocess.PIPE)

    packet = None
    try:
        startTime = time.time()
        for line in dump.stdout:
            line = line.decode()
            if line.startswith("> "):
                if packet: onPacketFound(packet)
                packet = line[2:].strip()
            elif line.startswith("< "):
                if packet: onPacketFound(packet)
                packet = None
            else:
                if packet: packet += " " + line.strip()

            if duration and time.time() - startTime > duration:
                break

    except KeyboardInterrupt:
        pass

    subprocess.call(["sudo", "kill", str(dump.pid), "-s", "SIGINT"])
    subprocess.call(["sudo", "-n", "kill", str(lescan.pid), "-s", "SIGINT"])


def advertise(ad, beacon_type=Eddystone.url):
    print("Advertising: {} : {}".format(beacon_type.name, ad))
    message = encodeMessage(ad, beacon_type)

    # Prepend the length of the whole message
    message.insert(0, len(message))

    # Pad message to 32 bytes for hcitool
    while len(message) < 32: message.append(0x00)

    # Make a list of hex strings from the list of numbers
    message = map(lambda x: "%02x" % x, message)

    # Concatenate all the hex strings, separated by spaces
    message = " ".join(message)
    verboseOutput("Message: " + message)

    subprocess.call("sudo hciconfig hci0 up", shell = True, stdout = DEVNULL)

    # Stop advertising
    subprocess.call("sudo hcitool -i hci0 cmd 0x08 0x000a 00", shell = True, stdout = DEVNULL)

    # Set message
    subprocess.call("sudo hcitool -i hci0 cmd 0x08 0x0008 " + message, shell = True, stdout = DEVNULL)

    # Resume advertising
    subprocess.call("sudo hcitool -i hci0 cmd 0x08 0x000a 01", shell = True, stdout = DEVNULL)


def stopAdvertising():
    print("Stopping advertising")
    subprocess.call("sudo hcitool -i hci0 cmd 0x08 0x000a 00", shell = True, stdout = DEVNULL)

def showVersion():
    print(application_name + " " + version)

def main():
    if args.version:
        showVersion()
    else:
        subprocess.call(["sudo", "-v"])
        if args.terminate:
            stopAdvertising()
        elif args.one:
            scan(3)
        elif args.scan:
            scan()
        elif args.uid:
            advertise(args.uid, Eddystone.uid)
        else:
            advertise(args.url)

if __name__ == "__main__":
    main()