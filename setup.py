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
__url__ = 'http://github.com/michagrandel/filtertext/'
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
    name='filtertext',
    version=__version__,
    url=__url__,
    license=__license__,
    author=__author__,
    author_email=__author_email__,
    description=__doc__,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=['filtertext'],
    include_package_data=True,
    platforms='any',
    scripts=['scripts/filter_text.py'],
    download_url='https://github.com/michagrandel/filtertext/releases/download/v1.0/filtertext-1.0.0-py3-none-any.whl',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        ],
)