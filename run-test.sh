#!/bin/bash

pytest -q src/parser/test/lexer-test.py
rm src/parser/test/output.txt
rm -R .pytest_cache
rm -R src/parser/__pycache__
rm -R src/parser/test/__pycache__