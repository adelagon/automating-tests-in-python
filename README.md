# Automating Tests in Python

## About
This is a collection of jupyter notebooks that have code snippets about how to automate different kinds of tests in python.

* [Unit Tests](chapter-1-unit-testing.ipynb)
* [Integration Tests](chapter-2-integration-testing.ipynb)
* [UI Tests](chapter-3-ui-testing.ipynb)
* [Performance Tests](chapter-4-performance-testing.ipynb)

The current version of the collection uses the following tools:

* [unittest](https://docs.python.org/3/library/unittest.html) - if you want to stay low-level
* [pytest](https://docs.pytest.org/en/stable/) - an awesome test framework that can be used in many different kinds of testing.
* [pytest-bdd](https://github.com/pytest-dev/pytest-bdd) - for writing tests in pytest when your team uses the Behavior-Driven Development methodology
* [pytest-splinter](https://github.com/pytest-dev/pytest-splinter) - for writing automated UI tests in pytest
* [Faker](https://faker.readthedocs.io/en/master/) - for generating mock data
* [locust](https://locust.io/) - A load testing framework
* [Splinter](https://splinter.readthedocs.io/en/latest/) - to automate web browser actions
* [json-server](https://github.com/typicode/json-server) - for creating a mock RESTFul API server.

## Requirements

* You need to have at least Python 3.7 and node.js v12.18.2 installed
* It is ideal to run this on a virtual environment. I used [venv](https://docs.python.org/3/library/venv.html) for this.

## Installation

* Clone this repo: ```git clone https://github.com/adelagon/automating-tests-in-python.git```
* Go the project root: ```cd automation-test-in-python```
* Install json-server with: ```npm install -g json-server```
* Run the json-server in the background in order to run the sample tests: ```json-server --watch db.json``` and open a new terminal session.
* Create a virtual environment: ```python -m venv .env```
* Activate virtual environment: ```source .env/bin/activate```
* Install all dependencies: ```pip install -r requirements.txt```
* Run the jupyter notebook: ```jupyter notebook```. This should open your web browser and navigate to the *.ipynb files to open the tutorials.
* Alternatively, you can use Microsoft VSCode to open the *.ipynb files

## Notes

Please feel free to reach out to me at me@adelagon.com for any additions/corrections.
