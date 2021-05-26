import sys
import pytest
sys.path.append('src/compiler')
from js_parser import javascript_parser
from antlr4 import *

test_paths = [
  ("example/example9.js", "src/compiler/test/codegen-test/right-test1.txt"),
  ("example/example10.js", "src/compiler/test/codegen-test/right-test2.txt"),
  ("example/example11.js", "src/compiler/test/codegen-test/right-test3.txt")
]

output = "src/compiler/test/codegen-test/output.txt"

@pytest.mark.parametrize("input,expected", test_paths)
def test_codegen(input, expected):
  output_stream = open(output, 'w')
  javascript_parser(input, output_stream, ['asm'], '')

  output_stream.close()
  assert ([row for row in open(output)] == [row for row in open(expected)])