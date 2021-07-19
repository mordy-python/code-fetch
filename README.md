# Code Fetch

[![PyPi Version](https://img.shields.io/pypi/v/code_fetch)](https://img.shields.io/pypi/v/code_fetch)&Tab;[![Maintained](https://img.shields.io/maintenance/yes/2021)](https://img.shields.io/maintenance/yes/2021)&Tab;[![Top Languages](https://img.shields.io/github/languages/top/mordy-python/code-fetch)](https://img.shields.io/github/languages/top/mordy-python/code-fetch)

Code fetch is a command line tool for fetching code from a single file on GitHub instead of cloning the whole repository.

## Installation

Install the package from PyPi:

`pip install code_fetch` or `pip3 install code_fetch`

Install the package from source:

`git clone https://github.com/mordy-python/code-fetch.git`

`cd code-fetch`

`python setup.py install`

## Usage

```
python -m code_fetch [OPTIONS] USER REPO FILE

Options:
  --save            Save the file to disk
  --save-file TEXT  The output file
  --help            Show this message and exit.
```
