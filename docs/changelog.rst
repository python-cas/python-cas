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
* In SAMLV1.1, the user username is withing NameIdentifier tags

.. _commit history: https://github.com/python-cas/python-cas/commits
.. _django-cas-ng: https://github.com/mingchen/django-cas-ng


**python-cas 1.3.0** ``[2018-08-02]``

* Improve CASv2 XML parsing when response is not standard
* Update URL suffix for CAS v3 serviceValidate
* Add method verify_logout_request
* Add lxml to setup.py


**python-cas 1.4.0** ``[2018-10-09]``

* Add kwarg `verify_ssl_certificate` to bypass SSL certificate validation
