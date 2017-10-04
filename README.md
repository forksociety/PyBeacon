# PyBeacon
[![Build Status](https://travis-ci.org/nirmankarta/PyBeacon.svg?branch=master)](https://travis-ci.org/nirmankarta/PyBeacon)

Python package for scanning and advertising [Eddystone-URL and Eddystone-UID](https://github.com/google/eddystone/tree/master/eddystone-url/implementations/PyBeacon).

Note: Please create you pull requests against dev branch.

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
