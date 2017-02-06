none: help

help:
	@echo "Elements: A modern music library."
	@echo
	@echo "run            Run Elements."
	@echo "lint           Run pylint3 on the Elements package."
	@echo "test           Run pytests for Elements."

lint:
	pylint3 --rcfile=pylintrc elements

run:
	python3 elements/elements.py

test:
	python3 -m pytest elements

.PHONY: lint run test
