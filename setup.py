#!/usr/bin/env python

from __future__ import absolute_import
import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    author='Ming Chen',
    author_email='mockey.chen@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'six',
        'requests',
        'lxml>=3.4',
    ],
    description='Python CAS client library',
    keywords=['cas', 'cas2', 'cas3', 'client', 'sso', 'single sign-on', 'authentication', 'auth'],
    license='MIT',
    long_description=readme,
    name='python-cas',
    packages=['.'],
    url='https://github.com/python-cas/python-cas',
    download_url ='https://github.com/python-cas/python-cas/releases',
    version='1.4.0',
)

