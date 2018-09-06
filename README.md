# GEOLOCIP [![Version-shield]](https://github.com/b0un7y/geolocip/releases) [![Python3-shield]](https://www.python.org/) [![License-shield]](https://raw.githubusercontent.com/b0un7y/geolocip/master/LICENSE)

> **Geolocation from an ip address in the terminal**

---

## Installation
~~~
$ git clone https://github.com/b0un7y/geolocip.git
$ cd geolocip
$ python setup.py install               # requires python3
~~~

### Dependencies
pip:
* argparse
* pygeoip

system:
* wget
* gzip

## Usage
~~~
usage: geolocip [-h] [-u] [-i IP]

optional arguments:
 -h, --help            show this help message and exit
 -u, --update          updates the database
 -i IP, --ip IP        ip address of the target
~~~

## License

GEOLOCIP - Geolocation from an ip address in the terminal

Copyright (c) 2018 b0un7y

So it is done...

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

[Version-shield]: https://img.shields.io/badge/version-0.1-blue.svg?style=flat-square&colorA=273133&colorB=0093ee "Latest version"
[Python3-shield]: https://img.shields.io/badge/python-3.6%2B-blue.svg?style=flat-square&colorA=273133&colorB=00db00 "Python3.6 or later"
[License-shield]: https://img.shields.io/badge/license-GPL%20v3%2B-blue.svg?style=flat-square&colorA=273133&colorB=bd0000 "GPL v3+"
