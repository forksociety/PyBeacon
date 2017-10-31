# PyBeacon
[![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red.svg)](https://github.com/nirmankarta/PyBeacon)
[![Build Status](https://travis-ci.org/nirmankarta/PyBeacon.svg?branch=master)](https://travis-ci.org/nirmankarta/PyBeacon)
[![PyPI](https://img.shields.io/pypi/v/PyBeacon.svg)](https://pypi.python.org/pypi/PyBeacon)
[![Operating System](https://img.shields.io/badge/Operating%20System-Linux-blue.svg)](https://en.wikipedia.org/wiki/Linux)
[![Python Versions](https://img.shields.io/badge/Python-2.6%2C%202.7%2C%203.3%2C%203.4%2C%203.5%2C%203.6-red.svg)]()   
[![Contributors](https://img.shields.io/github/contributors/cdnjs/cdnjs.svg)](https://github.com/nirmankarta/PyBeacon/graphs/contributors)
[![Slack](https://img.shields.io/badge/Slack%20channel-%20%20-blue.svg)](http://nirmankarta.herokuapp.com)
[![PyPI](https://img.shields.io/pypi/l/PyBeacon.svg)](https://github.com/nirmankarta/PyBeacon/blob/master/LICENSE)

Python package for scanning and advertising [Eddystone-URL and Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-url/implementations/PyBeacon).

**Note:** Please read [contribution.md](https://github.com/nirmankarta/PyBeacon/blob/master/CONTRIBUTING.md) before making any kind of contribution.

## Requirements

* Python 3.x (Scanning will not work on Python 2.x)
* Bluez
    * sudo apt-get install bluez bluez-hcidump
* Pip Packages
    * pip install enum34

## Installation

    sudo pip install PyBeacon

## Upgrade

    sudo pip install PyBeacon --upgrade

## Usage
	PyBeacon [-h] [-u [URL]] [-s] [-t] [-o] [-v] [-V]

	optional arguments:
		-h, --help            show this help message and exit
		-u [URL], --url [URL] URL to advertise.
		-i [UID], --uid [UID] UID to advertise.
		-s, --scan            Scan for URLs.
		-t, --terminate       Stop advertising URL.
		-o, --one             Scan one URL only.
		-v, --version         Version of PyBeacon.
		-V, --Verbose         Print lots of debug output.

## Projects using PyBeacon
* [PyBTSteward](https://github.com/wolfspyre/PyBTSteward)
* [pikiosk](https://github.com/chriso0710/pikiosk)

Please add your projects here if you are using PyBeacon's code so that similar projects can be accessed easily.
