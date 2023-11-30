# COMP 370 Final Project

# Overview

The task we've been assigned is described in [this file](./assignment_description/assignment.md)

We've chosen to work on task 2.

# Installation and Setup

## Python

*Optional: create a virtual environment*
`python -m venv venv`

Install dependencies:
`python -m pip install -r requirements.txt`

## API Keys

Please create a file named `creds.py` in the root directory of the project and add the following lines:

```Python
API_KEY = "<your-api-key-goes-here>"
```

## Tests

### Running tests

The test folder contains unit tests for the project. To run them, use the following command:
```bash
make run_tests
```

### Adding tests

The tests folder mimics the structure of the project.
Tests for `src` should be placed in `tests/src`, tests for `scripts` should be placed in `tests/scripts`, etc. 

**Don't forget to add `__init__.py` files to *all* of the folders you create inside `tests/` or they won't be automatically discovered.**

To add a new test or to test a new module, create a new file in the tests folder with the name `test_<name>.py` and add the following code:

```Python
import unittest

class Test<Name>(unittest.TestCase):
    def test_<name>(self):
        # Test code goes here
        pass

if __name__ == '__main__':
    unittest.main()
```

# Data

We've decided to look at all the wide-releases that had a top 5 domestic weekend gross since Oct 13th 2023 inclusive according to [the-numbers.com](the-numbers.com). The list includes re-releases.

The movie we've specifically chosen is:
TODO: select movie
...

The other movies to compare it to are:
- Taylor Swift | The Eras Tour
- The Exorcist: Believer
- PAW Patrol: The Mighty Movie
- Killers of the Flower Moon
- Five Nights at Freddy’s
- Priscilla
- Saw X
- The Creator
- After Death
- The Marvels


## Source Data

We've taken our data from [newsapi](https://newsapi.org/)

## Data Acquisition

## Data Preprocessing

# Code structure

.
├── assignment_description
├── data
│   ├── articles
│   └── interim
│       └── keywords
├── notebooks
├── scripts
│   └── python
├── src
│   └── common
└── tests
    └── src
        └── common

# Results

# Future work

# Contributors

- [Tristan Leclair-Vani](https://github.com/TristanLeclair)
- [Jean-Alexandre Nolin](https://github.com/JANolin)
- [Juan Rodriguez](https://github.com/JiRodriguez2411)
- [Michael Almanza](https://github.com/MichaelAlmanza)
