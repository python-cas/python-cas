Python CAS
==========

.. image:: https://travis-ci.org/python-cas/python-cas.svg?branch=master
    :target: https://travis-ci.org/python-cas/python-cas


``Python CAS`` Python utilities to implement CAS protocol (Central Authentication Service).

This project was started by factoring out CASClient* classes from the
`django-cas-ng`_ project, which was a continuation of `django-cas`_

Features
--------

- Support Client part of CAS_ version 1.0, 2.0 and 3.0.
- Support Python 2.7, 3.x


Installation
------------

Install with `pip`_::

    pip install python-cas

Install the latest code::

    pip install https://github.com/python-cas/python-cas/archive/master.zip

Install from source code::

    python setup.py install


Testing
-------

Every code commit triggers a **travis-ci** build. checkout current build status at https://travis-ci.org/python-cas/python-cas

Testing is managed by ``pytest`` and ``tox``.
Before run install, you need install required packages for testing::

    pip install -r requirements-dev.txt


To run testing on locally::

    py.test


To run all testing on all enviroments locally::

    tox


Contribution
------------

Contributions are welcome!

If you would like to contribute this project.
Please feel free to fork and send pull request.
Please make sure tests are passed.
Also welcome to add your name to **Credits** section of this document.

New code should follow both `PEP8`_.


Credits
-------

* `django-cas`_.
* `Stefan Horomnea`_.
* `Piotr Buliński`_.
* `Piper Merriam`_.
* `Nathan Brown`_.
* `Jason Brownbridge`_.
* `Bryce Groff`_.
* `Jeffrey P Gill`_.
* `timkung1`_.
* `Domingo Yeray Rodríguez Martín`_.
* `Rayco Abad-Martín`_.
* `Édouard Lopez`_.
* `Guillaume Vincent`_.
* `Evgeny Fadeev`_.

References
----------

* `django-cas-ng`_
* `CAS protocol`_
* `Jasig CAS server`_

.. _CAS: https://www.apereo.org/cas
.. _CAS protocol: https://www.apereo.org/cas/protocol
.. _django-cas-ng: https://bitbucket.org/cpcc/django-cas
.. _pip: http://www.pip-installer.org/
.. _PEP8: http://www.python.org/dev/peps/pep-0008
.. _Django coding style: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style
.. _User custom model: https://docs.djangoproject.com/en/1.5/topics/auth/customizing/
.. _Jasig CAS server: http://jasig.github.io/cas
.. _Piotr Buliński: https://github.com/piotrbulinski
.. _Stefan Horomnea: https://github.com/choosy
.. _Piper Merriam: https://github.com/pipermerriam
.. _Nathan Brown: https://github.com/tsitra
.. _Jason Brownbridge: https://github.com/jbrownbridge
.. _Bryce Groff: https://github.com/bgroff
.. _Jeffrey P Gill: https://github.com/jpg18
.. _timkung1: https://github.com/timkung1
.. _Domingo Yeray Rodríguez Martín: https://github.com/dyeray
.. _Rayco Abad-Martín: https://github.com/Rayco
.. _Édouard Lopez: https://github.com/edouard-lopez
.. _Guillaume Vincent: https://github.com/guillaumevincent
.. _Evgeny Fadeev: https://github.com/evgenyfadeev
