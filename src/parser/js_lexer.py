import sys
import argparse
from build_antlr.JSLexer import JSLexer
from antlr4 import *

def javascript_lexer(input, output):
  input_stream = FileStream(input)
  lexer = JSLexer(input_stream)

  while lexer._hitEOF != True:
    token = lexer.nextToken()
    output.write(f'Loc=<{token.line}:{lexer.column}>  {lexer.symbolicNames[token.type]} {token.text}\n')

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=str, help="Path to javascript file", metavar="Input file")
  parser.add_argument("--out", type=str, default="console", help="Path to output file (default: console)", metavar="Output file or console")
  args = parser.parse_args()

  if args.out == 'console':
    javascript_lexer(args.input, sys.stdout)
  else:
    try:
      output_stream = open(args.out, 'w')
      javascript_lexer(args.input, output_stream)
    except:
      print("Error: output file does not open")
      sys.exit(0)
 
if __name__ == '__main__':
  main()