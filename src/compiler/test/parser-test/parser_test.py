import sys
import pytest
sys.path.append('src/compiler')
from js_parser import javascript_parser
from antlr4 import *

test_paths = [
  ("example/example2.js", "src/compiler/test/parser-test/right-test2.txt"),
  ("example/example3.js", "src/compiler/test/parser-test/right-test3.txt")
]

output = "src/compiler/test/parser-test/output.txt"

@pytest.mark.parametrize("input,expected", test_paths)
def test_parser(input, expected):
  output_stream = open(output, 'w')
  javascript_parser(input, output_stream, ['ast'])
  output_stream.close()

  assert ([row for row in open(output)] == [row for row in open(expected)])

def test_parser_negative():
  output_stream = open(output, 'w')
  errors = javascript_parser("example/example1.js", output_stream, ['ast'])
  output_stream.close()

  assert ([str(row) for row in errors.errors] == [row for row in open("src/compiler/test/parser-test/right-test1.txt")])