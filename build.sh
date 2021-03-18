#!/bin/bash

cd src/grammar

mkdir build-antlr-lexer
antlr4 -o ./build-antlr-lexer -Dlanguage=Python3 JSLexer.g4

pip3 install antlr4-python3-runtime

cd build-antlr-lexer
touch __init__.py