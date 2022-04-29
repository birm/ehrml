init:
	pip install -r requirements.txt

test:
	pytest

dist:
	python setup.py sdist
