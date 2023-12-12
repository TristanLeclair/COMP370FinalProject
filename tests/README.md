# Tests

## Running tests

The test folder contains unit tests for the project. To run them, use the following command:
```bash
make run_tests
```

## Adding tests

The tests folder mimics the structure of the project.
Tests for `src` should be placed in `tests/src`, tests for `scripts` should be placed in `tests/scripts`, etc. 

**Don't forget to add `__init__.py` files to *all* of the folders you create inside `tests/` or they won't be automatically discovered.**

To add a new test or to test a new module, create a new file in the tests folder with the name `test_<name>.py` and add the following code:

## Structure

```
.
├── README.md
├── __init__.py
└── src
    ├── __init__.py
    └── common
        ├── __init__.py
        └── testrequestutils.py
```
