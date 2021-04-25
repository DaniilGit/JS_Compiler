#!/bin/bash

# python3 src/parser/js_lexer.py example/example1.js --out result.txt
python3 src/parser/js_parser.py example/helloworld.js --out console

rm -R src/parser/__pycache__