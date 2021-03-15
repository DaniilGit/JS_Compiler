import sys
import pytest
sys.path.append('src/grammar/build-antlr-lexer')
sys.path.append('src/grammar/antlr-runtime-python')
sys.path.append('src/lexer')
from JSLexer import JSLexer
from lexer import java_script_lexer
from antlr4 import *

test_paths = [
  ("example/example1.js", "src/lexer/test/right-test1.txt"),
  ("example/example2.js", "src/lexer/test/right-test2.txt"),
  ("example/example3.js", "src/lexer/test/right-test3.txt")
]
output = "src/lexer/test/output.txt"

@pytest.mark.parametrize("input,expected", test_paths)
def test_lexer(input, expected):
  java_script_lexer(input, output)
  assert ([row for row in open(output)] == [row for row in open(expected)])