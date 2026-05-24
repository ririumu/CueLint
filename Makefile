.PHONY: lint test

PYTHON ?= python

lint:
	PYTHONPATH=src $(PYTHON) -m cuelint samples/assistant-response.txt

test:
	PYTHONPATH=src $(PYTHON) -m unittest discover -s tests
