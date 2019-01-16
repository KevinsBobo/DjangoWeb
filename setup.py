#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='shunchuang',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='shunchuang website',
    # GETTING-STARTED: set author name (your name):
    author='Kevins Bobo',
    # GETTING-STARTED: set author email (your email):
    author_email='kevins.bobo@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.kevins.pro',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.11.18'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
