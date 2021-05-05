#!/bin/bash

# python3 src/parser/js_lexer.py example/example2.js --out result.txt
python3 src/parser/js_parser.py example/example8.js --out console

rm -R src/parser/__pycache__
rm -R src/parser/symtab/__pycache__