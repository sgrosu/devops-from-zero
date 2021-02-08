install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=hello test_hello.py
	pytest
lint:
	pylint --disable=R,C,E1120 hello.py

format:
	black *.py

all: install lint test
