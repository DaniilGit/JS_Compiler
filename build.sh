#!/bin/bash

pushd src/grammar
antlr4 -o ../parser/build_antlr/ -visitor -Dlanguage=Python3 JS.g4

pip3 install antlr4-python3-runtime