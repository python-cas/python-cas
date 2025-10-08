*********
Changelog
*********

Listed are the high-level, notable changes for python-cas release.
Backwards incompatible changes or other upgrade issues are also described
here. For additional detail, read the complete `commit history`_.

**python-cas 1.0.0** ``[2015-6-17]``

* Factored out `python-cas` library from `django-cas-ng`_ Django app.


**python-cas 1.1.0** ``[2015-11-08]``

* port changes form django-cas-ng.
* copied test from django-cas-ng.
* more syncing of cas code with that in django-cas-ng
* add SAML single logout to CAS v3
* synced the protocol part with django-cas-ng in hope to use this library in django-cas-ng
* allowed to customize name of logout redirect url parameter
* base cas client with SAML on CASClientV2


**python-cas 1.2.0** ``[2016-11-06]``

* Replace urllib2 calls with requests to avoid SNI issues
* In SAMLV1.1, the user username is within NameIdentifier tags

.. _commit history: https://github.com/python-cas/python-cas/commits
.. _django-cas-ng: https://github.com/mingchen/django-cas-ng


**python-cas 1.3.0** ``[2018-08-02]``

* Improve CASv2 XML parsing when response is not standard
* Update URL suffix for CAS v3 serviceValidate
* Add method verify_logout_request
* Add lxml to setup.py


**python-cas 1.4.0** ``[2018-10-09]``

* Add kwarg `verify_ssl_certificate` to bypass SSL certificate validation

**python-cas 1.5.0** ``[2020-01-30]``

* PR-17: Test and document support for all modern Python versions
* PR-18: Distribute package as a universal Python Wheel
* PR-20: README: Link to python.org using HTTPS
* PR-21: Minor refactor: Prefer dict literals {} over dict()
* PR-22: Enable native pip cache in Travis CI
* PR-23: Fix setup.py: Declare cas.py as a module, not a package
* PR-24: setup.py: Pass python_requires argument to setuptools
* PR-25: Remove unnecessary distutils fallback from setup.py
* PR-26: Fix links in README.rst
* PR-27: Simplify tox configuration
* PR-28: Include tests in the source distribution
* PR-29: Remove pytest-pythonpath dependency
* PR-30: Use skip_install=true for lint or static tox targets
* PR-32: Use tox's builtin support for the TOXENV environment variable
* PR-31: Introduce isort for automatic import ordering
* PR-33: Simplify dependency handling in tox.ini
* PR-35: Fix SSL certificate validation due to client field for get_proxy_ticket
* PR-36: Add support for <norEduPerson> element under <cas:authenticationSuccess>
* Fix #34: Exclude setup from installed package

**python-cas 1.6.0** ``[2021-09-17]``

* Refine docstring to google style for better documentation
* PR #39: Fix SAML ticket verification failing when response is not namespaced @mbenadda 
* PR #44: Use Session for making requests & allow customization @intgr

**python-cas 1.7.0** ``[2025-10-08]``

* github actions: test on ubuntu 24 (#58) @nikolas
* Update supported python versions (#57) @nikolas
* Test on python 3.10 by default (#56) @nikolas
* Remove old python versions from tox (#55) @nikolas
* Remove universal wheel (#54) @nikolas
* Update pytest (#53) @nikolas
* Add python 3.11 testing, update github actions envs (#52) @nikolas
* setup.py: add classifiers for py3.9, py3.10 (#50) @nikolas
* Add python 3.10 testing (#49) @nikolas
* Fixing 'requests.api' has no attribute 'Session' (#47) @vhelke
* Fix get_proxy_url adding unnecessary '/' (#41) @seayjohnny
* Fix a few typos in changelog (#45) @intgr
