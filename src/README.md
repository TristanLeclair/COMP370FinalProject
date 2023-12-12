# src

This is the source code folder. It contains the following subfolders:

## common

This folder contains common code that is used by multiple modules. It contains the following files:

### requestutils.py

A collection of functions help with making HTTP requests and structuring queries.

### jsonutils.py

A collection of functions to help with JSON parsing and outputting.

### logging_utils.py

A collection of functions to help with logging.

### collect.py

A collection of functions to help with collecting data from newsapi.org, including caching.

## adding your own modules

To add your own modules, create a new folder in `src/` and add a file named `__init__.py` to it.
