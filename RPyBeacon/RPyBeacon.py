#!/usr/bin/python
import sys, os
from subprocess import call

prefixes = ['http://www.', 'https://www.', 'http://', 'https://']
tlds =['.com', '.org', '.edu', '.net', '.info', '.biz', '.gov']

tld_offset = 7
len1_offset = 15
len2_offset = 7
cmd = ''

def get_url_hex(url):
	out = 'sudo hcitool -i hci0 cmd 0x08 0x0008 '
	url_hex = ''
	prefix = '02'
	tld = ''
	for x in prefixes:
		if x in url:
			url = url.replace(x, '')
			prefix = '0' + str(prefixes.index(x))
			break
	url_hex += prefix

	for x in tlds:
		if (x + '/') in url:
			url = url.split(x + '/')
			tld = '0' + str(tlds.index(x))
			break
		elif x in url:
			url = url.split(x)
			tld = '0' + str(tlds.index(x) + tld_offset)
			break
	if len(tld) == 0:
		return 'echo Please enter valid url'

	# identify host to add tld code
	flag = True
	url_len = 0
	for item in url:
		if len(item) != 0:
			for c in item:
				url_hex += ' ' + format(ord(c), "x")
				url_len += 1
		if flag:
			url_hex += ' ' + tld
			flag = False

	len1 = url_len + len1_offset
	len2 = url_len + len2_offset

	if len(hex(len1).split('x')[1]) < 2:
		out += '0'
	out += hex(len1).split('x')[1] + ' '
	out += '02 01 06 03 03 aa fe '
	
	if len(hex(len2).split('x')[1]) < 2:
		out += '0'
	out += hex(len2).split('x')[1] + ' '
	out += '16 aa fe 10 00 '
	out += url_hex + ' '
	out += '00 00 00 00 00 00 00 00'
	return out

def get_command(arg1, arg2 = ''):
	if arg1 == 'start':
		print 'Enabling bluetooth and setting advertise mode'
		return 'sudo hciconfig hci0 up && sudo hciconfig hci0 leadv 3 && ' + get_url_hex('http://nirmankarta.com')
	elif arg1 == 'enable':
		print 'Enabling bluetooth'
		return 'sudo hciconfig hci0 up'
	elif arg1 == 'admode':
		print 'Set the Bluetooth device to advertise and not-connectable'
		return 'sudo hciconfig hci0 leadv 3'
	elif arg1 == 'beaconurl':
		if len(arg2) == 0:
			return 'echo url missing'
		print 'Setting beacon url to', arg2
		return get_url_hex(arg2)
	else:
		return 'echo Invalid parameters'


def main():
	cmd = ''
	if len(sys.argv) == 2:
		cmd = get_command(sys.argv[1])
	elif len(sys.argv) == 3:
		cmd = get_command(sys.argv[1], sys.argv[2])
	else:
		print 'no parameter found'
		exit()
	print cmd
	os.system(cmd)

if __name__ == "__main__":
	main()
	