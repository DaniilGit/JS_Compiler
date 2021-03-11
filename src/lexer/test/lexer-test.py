import sys
import pytest
sys.path.append('src/grammar/build-antlr-lexer')
sys.path.append('src/grammar/antlr-runtime-python')
sys.path.append('src/lexer')

from JSLexer import JSLexer
from lexer import JavaScriptLexer
from antlr4 import *

output_path = "src/lexer/test/output.txt"

def comparison_results(input, output):
  input_stream = open(input, 'r')
  output_stream = open(output, 'r')

  for line1 in input_stream:
    for line2 in output_stream:
      if line1 == line2:
        break
      else:
        return False

  return True

def test_lexer1():
  JavaScriptLexer("example/example1.js", output_path)
  assert (comparison_results("src/lexer/test/right-test1.txt", output_path))

def test_lexer2():
  JavaScriptLexer("example/example2.js", output_path)
  assert (comparison_results("src/lexer/test/right-test2.txt", output_path))

def test_lexer3():
  JavaScriptLexer("example/example3.js", output_path)
  assert (comparison_results("src/lexer/test/right-test3.txt", output_path))

def main():
  test_lexer1()
  test_lexer2()
  test_lexer3()

if __name__ == '__main__':
  main()