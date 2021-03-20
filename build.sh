#!/bin/bash

pushd src/grammar
antlr4 -o ../lexer/build_antlr_lexer/ -Dlanguage=Python3 JSLexer.g4

pip3 install antlr4-python3-runtime