#!/bin/bash

mkdir result
python3 src/compiler/js_parser.py example/example9.js --dump asm --out console
clang -o ./result/example9 ./result/example9.ll
./result/example9

rm -R src/compiler/__pycache__
rm -R src/compiler/symtab/__pycache__
rm -R src/compiler/ast/__pycache__
rm -R src/compiler/codegen/__pycache__