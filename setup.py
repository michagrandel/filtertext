"""Filter text and save result to file or print to output!
If no output file or output directory is specified, filter_text.py will output to console"""

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import os
import sys

import filtertext

here = os.path.abspath(os.path.dirname(__file__))

__version__ = '1.0.0'
__url__ = 'http://github.com/michagrandel/textfilter/'
__author__ = 'Micha Grandel'
__author_email__ = 'hello@michagrandel.de'
__license__ = 'Apache 2.0 License'

def read(*filenames):
    buf = []
    for filename in filenames:
        with io.open(filename) as f:
            buf.append(f.read())
    return '\n'.join(buf)

long_description = read('README.md')

setup(
    name='textfilter',
    version=__version__,
    url=__url__,
    license=__license__,
    author=__author__,
    install_requires=['Flask>=0.10.1',
                    'Flask-SQLAlchemy>=1.0',
                    'SQLAlchemy==0.8.2',
                    ],
    author_email=__author_email__,
    description=__doc__,
    long_description=long_description,
    packages=['textfilter'],
    include_package_data=True,
    platforms='any',
    scripts=['scripts/filter_text.py']
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        ],
)