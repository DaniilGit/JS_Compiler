import sys
import pytest
sys.path.append('src/parser')
from js_parser import javascript_parser
from antlr4 import *

test_paths = [
  ("example/example7.js", "src/parser/test/semantic-test/right-test1.txt"),
  ("example/example8.js", "src/parser/test/semantic-test/right-test2.txt")
]

output = "src/parser/test/semantic-test/output.txt"

def test_semantic():
  output_stream = open(output, 'w')
  errors = javascript_parser("example/example4.js", output_stream)
  output_stream.close()

  assert (errors == None)

@pytest.mark.parametrize("input,expected", test_paths)
def test_semantic_negative(input, expected):
  output_stream = open(output, 'w')
  errors = javascript_parser(input, output_stream)

  for elem in errors.errors:
    output_stream.write(elem)
    output_stream.write('\n')

  output_stream.close()
  assert ([row for row in open(output)] == [row for row in open(expected)])