clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr html/
	rm -rf cover/

test:
	nosetests --verbosity 2 --with-doctest --doctest-extension=rst alignme

test-all:
	tox

coverage: clean-test
	nosetests --verbosity 2 --with-doctest --doctest-extension=rst alignme
	coverage run --source alignme setup.py test
	coverage report -m
	coverage html
