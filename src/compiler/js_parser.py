import sys
import argparse
import json
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from build_antlr.JSLexer import JSLexer
from build_antlr.JSParser import JSParser
from symtab.symtab import Symtab
from dump_tokens import dump_tokens
from ast_visitor import AstVisitor
from js_visitor import JSVisitor

class StreamErrorListener(ErrorListener):
  def __init__(self):
    self.errors = []

  def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
    self.errors.append(("Error: line " + str(line) + ":" + str(column) + " " + msg))

def javascript_parser(input, output, dump):
  input_stream = FileStream(input)
  lexer = JSLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = JSParser(stream)

  error_listener = StreamErrorListener()
  parser.removeErrorListeners()
  parser.addErrorListener(error_listener)
  tree = parser.program()

  ast = JSVisitor().visitProgram(tree)
  ast_json = AstVisitor().astVisitProgram(ast)
  symtab = Symtab(error_listener.errors).astVisitProgram(ast)

  if dump.count('tokens'):
    dump_tokens(input, output)

  if bool(error_listener.errors):
    for error in error_listener.errors:
      print(error)
    return error_listener

  if dump.count('ast'):
    output.write(json.dumps(ast_json, indent=2))
  if dump.count('asm'):
    pass

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=str, help="Path to javascript file", metavar="Input file")
  parser.add_argument("--out", type=str, default="console", help="Path to output file (default: console)", metavar="Output file or console")
  parser.add_argument("--dump", nargs='+', type=str, help="example '--dump tokens'", metavar="Options: tokens, ast, asm")
  args = parser.parse_args()

  if args.out == 'console':
    javascript_parser(args.input, sys.stdout, args.dump)
  else:
    try:
      output_stream = open(args.out, 'w')
      javascript_parser(args.input, output_stream)
    except:
      print("Error: output file does not open")
      sys.exit(0)

if __name__ == '__main__':
  main()