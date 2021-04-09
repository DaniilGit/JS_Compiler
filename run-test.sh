#!/bin/bash

pytest -q src/parser/test/lexer-test/lexer-test.py
rm src/parser/test/lexer-test/output.txt

pytest -q src/parser/test/parser-test/parser-test.py
rm src/parser/test/parser-test/output.txt

rm -R .pytest_cache
rm -R src/parser/__pycache__
rm -R src/parser/test/lexer-test/__pycache__
rm -R src/parser/test/parser-test/__pycache__