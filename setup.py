#!/usr/bin/env python

from __future__ import absolute_import

import codecs

from setuptools import setup

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
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
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
    py_modules=['cas'],
    url='https://github.com/python-cas/python-cas',
    download_url ='https://github.com/python-cas/python-cas/releases',
    version='1.4.0',
)
