.PHONY: all build clean install test

PYTHON=python

all: build

build:
	$(PYTHON) setup.py build

clean:
	$(PYTHON) setup.py clean --all
	find . -name '*.py[co]' -exec rm -f "{}" ';'
	rm -rf build dist django_cas_ng.egg-info temp

install:
	$(PYTHON) setup.py install

test:
	TOXENV=py310 tox
