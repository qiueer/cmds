#!/usr/bin/env python
# # coding: utf-8
from setuptools import find_packages, setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='cmds',
    description='cmds for Python',
    version='0.1.1',
    long_description=long_description,
    author='qiueer',
    author_email='qiujqin@163.com',
    url='https://github.com/qiueer/cmds',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU Library or Lesser '
         'General Public License (LGPL)'),
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
