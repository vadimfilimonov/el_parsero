up:
	pipenv shell

install:
	pipenv install

build:
	pipenv run python main.py

lint:
	pipenv run pylint --rcfile=.pylintrc *.py

.PHONY: build
