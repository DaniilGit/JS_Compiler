import sys
import pytest
sys.path.append('src/parser')
from js_parser import javascript_parser
from antlr4 import *

test_paths = [
  ("example/example5.js", "src/parser/test/symtab-test/right-test1.txt"),
  ("example/example6.js", "src/parser/test/symtab-test/right-test2.txt")
]

output = "src/parser/test/symtab-test/output.txt"

def test_symtab():
  output_stream = open(output, 'w')
  errors = javascript_parser("example/example4.js", output_stream)
  output_stream.close()

  assert (errors == None)

@pytest.mark.parametrize("input,expected", test_paths)
def test_symtab_negative(input, expected):
  output_stream = open(output, 'w')
  errors = javascript_parser(input, output_stream)
  output_stream.close()

  assert ([str(row) for row in errors.errors] == [row for row in open(expected)])