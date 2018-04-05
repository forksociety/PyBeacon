"""PyBeacon module to set some basic stuff up."""

import re
from setuptools import setup

with open('PyBeacon/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='PyBeacon',
    version=version,
    packages=['PyBeacon'],
    entry_points={
        "console_scripts": ['PyBeacon = PyBeacon.PyBeacon:main']
    },
    description='Python package for scanning and advertising \
    Eddystone-URLs and Eddystone-UID.',
    long_description='Python package for scanning and advertising \
    Eddystone-URLs and Eddystone-UID.',
    url='https://github.com/forksociety/PyBeacon',
    download_url='https://github.com/forksociety/PyBeacon/archive/master.zip',
    author='forksociety',
    author_email='os@forksociety.com',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    keywords=['Eddystone', 'Eddystone URL', 'Beacon', 'Raspberry Pi'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'enum34'
    ],
)
