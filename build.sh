#!/bin/bash

cd src/grammar

antlr4 -Dlanguage=Python3 JSLexer.g4

mkdir build-antlr-lexer
mv JSLexer.interp ./build-antlr-lexer
mv JSLexer.py ./build-antlr-lexer
mv JSLexer.tokens ./build-antlr-lexer

cd build-antlr-lexer
touch __init__.py