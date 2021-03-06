up:
	pipenv shell

install:
	pipenv install

build:
	pipenv run python main.py

lint:
	pylint --rcfile=.pylintrc *.py

.PHONY: build
