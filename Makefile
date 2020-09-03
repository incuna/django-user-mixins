SHELL := /bin/bash

keepdb=1 

help:
	@echo "Usage:"
	@echo " make test           | Run the tests."
	@echo " make test keepdb=0  | Run the tests without keeping the db."

test: export KEEPDB=$(keepdb)
test:
	@coverage run ./user_mixins/tests/run.py
	@coverage report
	@flake8

release:
	@(git diff --quiet && git diff --cached --quiet) || (echo "You have uncommitted changes - stash or commit your changes"; exit 1)
	@git clean -dxf
	@python setup.py sdist bdist_wheel
	@twine upload dist/*
