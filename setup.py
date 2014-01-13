#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='multiple-git-status',
    version="0.1",
    description='Command to show git status of many repos at once',
    long_description='''Command to show git status of many repos at once''',
    keywords='python git',
    author='Marinho Brandao',
    author_email='mario@gmail.com',
    url='http://github.com/marinho/multiple-git-status/',
    license="BSD",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "colorama",
        #"derpconf",
    ],
    scripts=['multiple_git_status.py',],
)
