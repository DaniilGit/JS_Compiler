#!/bin/bash

pytest -q src/compiler/test/lexer-test/lexer_test.py
rm src/compiler/test/lexer-test/output.txt

pytest -q src/compiler/test/parser-test/parser_test.py
rm src/compiler/test/parser-test/output.txt

pytest -q src/compiler/test/symtab-test/symtab_test.py
rm src/compiler/test/symtab-test/output.txt

pytest -q src/compiler/test/semantic-test/semantic_test.py
rm src/compiler/test/semantic-test/output.txt

rm -R .pytest_cache
rm -R src/compiler/__pycache__
rm -R src/compiler/test/lexer-test/__pycache__
rm -R src/compiler/test/parser-test/__pycache__
rm -R src/compiler/test/symtab-test/__pycache__
rm -R src/compiler/test/semantic-test/__pycache__