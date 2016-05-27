from setuptools import setup

setup(
	name='RPyBeacon',
	version='0.1.5',
	packages=['RPyBeacon'],
    entry_points = {
        "console_scripts": ['RPyBeacon = RPyBeacon.RPyBeacon:main']
    },

    description ='Make your raspberry pi 3 an Eddystone URL beacon',

    url='https://github.com/nirmankarta/RPyBeacon',

    author='Nirmankarta',

    license='MIT',

	classifiers=[
       
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)