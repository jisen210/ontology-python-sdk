#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, getcwd
from codecs import open
from setuptools import setup, find_packages


with open(path.join(getcwd(), 'DESCRIP.md')) as f:
    long_description = f.read()


setup(
    name='ontology-python-sdk',
    version='0.1.1',
    description='Comprehensive Python library for the Ontology BlockChain.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ontology',
    author_email='contact@ont.io',
    maintainer='NashMiao',
    maintainer_email='wdx7266@outlook.com',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    packages=find_packages(),
    install_requires=[
        'pycryptodomex',
        'cryptography',
        'ecdsa',
        'base58',
        'requests'
    ],
    python_requires='>=3.7',
    platforms=["all"],
    url='https://github.com/ontio/ontology-python-sdk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.7',
    ],
)
