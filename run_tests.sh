#!/bin/bash

python3 -m coverage run --source core -m unittest discover operations_tests
python3 -m coverage report
python3 -m coverage html
