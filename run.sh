#!/bin/bash

# python3 src/compiler/js_lexer.py example/example2.js --out result.txt
python3 src/compiler/js_parser.py example/example2.js --dump ast --out console

rm -R src/compiler/__pycache__
rm -R src/compiler/symtab/__pycache__