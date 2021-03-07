up:
	pipenv shell

install:
	pipenv install
	pipenv install --dev

build:
	pipenv run python main.py

lint:
	pipenv run pylint --rcfile=.pylintrc *.py

.PHONY: build
