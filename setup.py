from setuptools import setup
import platform, warnings

#Pypy dependency support
python_implementation = platform.python_implementation()

install_requires = ['pygeoip', 'argparse',]
if python_implementation == "PyPy":
    install_requires = ['pygeoip', 'argparse',]
elif python_implementation != "CPython":
    warnings.warn("We don't know how to deal with the {} runtime. Treating it like CPython".format(python_implementation), RuntimeWarning)

setup(name='geolocip',
        version='0.1',
        description='Geolocation from an ip address in the terminal',
        url='http://github.com/b0un7y/geolocip',
        author='b0un7y',
        author_email='b0un7y@bk.ru',
        license='GNU',
        scripts=['bin/geolocip',],
        install_requires=install_requires,
        include_package_data=True
)
