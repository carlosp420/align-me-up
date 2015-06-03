clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr html/
	rm -rf cover/

test: clean-test
	coverage run --source alignme setup.py test

test-all:
	tox

coverage: test
	coverage report -m
	coverage html
