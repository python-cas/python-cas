#!/usr/bin/env python

from __future__ import absolute_import

import codecs

from setuptools import setup

with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    author='Ming Chen',
    author_email='ming@djangocas.dev',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires=">=3.10",
    install_requires=[
        'six>=1.10.0',
        'requests>=2.11.1',
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
    version='1.6.0',
)
