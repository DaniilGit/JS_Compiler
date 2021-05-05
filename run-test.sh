#!/bin/bash

pytest -q src/parser/test/lexer-test/lexer_test.py
rm src/parser/test/lexer-test/output.txt

pytest -q src/parser/test/parser-test/parser_test.py
rm src/parser/test/parser-test/output.txt

pytest -q src/parser/test/symtab-test/symtab_test.py
rm src/parser/test/symtab-test/output.txt

pytest -q src/parser/test/semantic-test/semantic_test.py
rm src/parser/test/semantic-test/output.txt

rm -R .pytest_cache
rm -R src/parser/__pycache__
rm -R src/parser/test/lexer-test/__pycache__
rm -R src/parser/test/parser-test/__pycache__
rm -R src/parser/test/symtab-test/__pycache__
rm -R src/parser/test/semantic-test/__pycache__