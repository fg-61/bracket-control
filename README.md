# Bracket Control

bracket_control is a module containing the function isBalanced.

## isBalanced Function Description

Checks if the brackets sequences are balanced for each set of brackets. Returns YES if a string is balanced. Otherwise, it returns NO.

## Usage

1. Add bracket_control.py file in the same directory as your project.
2. Put the following line in your project:
```python
import bracket_control
```

## Example
```python
import bracket_control

# returns 'YES'
bracket_control.isBalanced('([{}])')

# returns 'NO'
bracket_control.isBalanced('(]')
```


# Unit Test

## Installation
pytest requires : Python 3.7+

1. Run the following command in your command line:
```bash
pip install -U pytest
```
2. Check that you installed correct version:
```bash
$ pytest –version
	pytest 7.1.2
```

## Run pytest
1. Run the following command in your command line:
```bash
python -m pytest test_bracket_control.py
```
