#!/usr/bin/env python

from io import open
from setuptools import setup



version = '0.0.2'


long_description = "Some long description"

setup(
    name='dbez',
    version=version,

    author='nikit0ska',
    author_email='nik.ryabov.2014@mail.ru',

    description=(
        u'Python module for for working with databases of different types'
    ),
    long_description=long_description,
    # long_description_content_type='text/markdown',

    url='https://github.com/Nikit0ska/dbez',
    download_url='https://github.com/Nikit0ska/dbez/archive/refs/heads/main.zip'
    ,

    license='MIT License',

    packages=['dbez'],
    install_requires=['pyodbc', 'xlrd3'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)