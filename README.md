# Testing in Python, from 0 to 100

This repository contains the slides and code examples from my talk on testing in Python, presented at the monthly Python Valencia meetup in December 2022.

The goal of the talk was to provide an introduction to testing in Python, starting from the basics and working up to more advanced techniques, as well as launch open questions on what is a good test.

I hope you find this repository useful as you explore testing in Python. If you have any questions or feedback, please feel free to ask me.

## Content

### Presentation Slides

The `slides.pdf` file contains the slides from my presentation. The original talk
goes up to page 24, presenting basic tests done in `pytest`, the use of mocks
and fixtures, and ends with an example of mutation testing.

The slides also include additional testing methods (from page 25 on) that were
not covered in detail during the original talk, which includes property based
testing and behaviour based testing.

### The code under test

The file `moon_locator.py` contains an easy example of code that calculates
the date & time when the moon will be located in the South.

### The tests

- An example of not-proper way to test: `this_is_not_a_proper_way_to_test.py`
- Some easy tests using pytest: `test_moon_locator.py`
- A test using a pytest fixture: `test_with_fixture.py`
- A test using mocking: `test_with_mock.py`
- A test using property-based testing: `test_property_based.py`
- An example of BBD test: `/features`

## Instalation

You can create a virtual enviroment (pyenv, etc) and install the dependencies
from `requirements.txt` or you can use docker.

### Using docker

Build the image:
`docker build -t moon_image .`

Explore the container:
`docker run -ti moon_image bash`

Run a command (f.ex. pytest):
`docker run moon_image pytest -v`

### VS Code + Dev Containers

If you happen to use VS Code, you can install the Dev Container plugin and
work with the code inside a docker container. Just use "Reopen in container"
(as the Development Container config file is in the repo already).
Notice that you may need to install `Python` extension in Dev Container.

## Executing the tests

### Basic tests (pytest)

Run pytest:
`docker run moon_image pytest -vv`

Run pytest with coverage:
`pytest -v --cov=. --cov-report=html .`

### Mutation testing (mutmut)

Run mutation testing:
`mutmut run --paths-to-mutate=.`

See results:
`mutmut results`

Show a mutation:
`mutmut show 1`

Execute one mutation:
`mutmut run 1 --paths-to-mutate=.`

### Property-based testing (hypothesis)

Execute the example test that uses hypothesis:
`pytest -v tests/test_property_based.py --hypothesis-show-statistics`

### BBD testing (behave)

Run the *features* tests:
`behave`
