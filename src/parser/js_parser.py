import sys
import argparse
import json
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from build_antlr.JSLexer import JSLexer
from build_antlr.JSParser import JSParser
from AstVisitor import AstVisitor
from JSVisitor import JSVisitor

class StreamErrorListener(ErrorListener):
  def __init__(self):
    self.errors = []

  def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    print("line " + str(line) + ":" + str(column) + " " + msg)
    self.errors.append({
      "line": str(line),
      "column": str(column),
      "msg": msg
    })

def javascript_parser(input, output):
  input_stream = FileStream(input)
  lexer = JSLexer(input_stream) 
  stream = CommonTokenStream(lexer)
  parser = JSParser(stream)

  error_listener = StreamErrorListener()
  parser.removeErrorListeners()
  parser.addErrorListener(error_listener)

  tree = parser.program()

  if bool(error_listener.errors):
    return error_listener 

  ast = JSVisitor().visitProgram(tree)
  result = AstVisitor().astVisitProgram(ast)

  output.write(json.dumps(result, indent=2))
  # print(result)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=str, help="Path to javascript file", metavar="Input file")
  parser.add_argument("--out", type=str, default="console", help="Path to output file (default: console)", metavar="Output file or console")
  args = parser.parse_args()

  if args.out == 'console':
    javascript_parser(args.input, sys.stdout)
  else:
    try:
      output_stream = open(args.out, 'w')
      javascript_parser(args.input, output_stream)
    except:
      print("Error: output file does not open")
      sys.exit(0)

if __name__ == '__main__':
  main()