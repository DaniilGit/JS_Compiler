import sys
import argparse
from antlr4 import *
from build_antlr.JSLexer import JSLexer
from build_antlr.JSParser import JSParser
from JSVisitor import JSVisitor

def javascript_parser(input, output):
  input_stream = FileStream(input)
  lexer = JSLexer(input_stream)
  stream = CommonTokenStream(lexer)
  parser = JSParser(stream)
  tree = parser.program()
  ast = JSVisitor().visitProgram(tree)
  # output.write(tree.toStringTree(recog=parser))
  # output.write('\n')

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