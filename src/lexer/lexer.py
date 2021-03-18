import sys
sys.path.append('src/grammar/build-antlr-lexer')
from JSLexer import JSLexer
import argparse
from antlr4 import *

def javascript_lexer(input, output):
  input_stream = FileStream(input)
  lexer = JSLexer(input_stream)

  try:
    output_stream = open(output, 'w')
    while lexer._hitEOF != True:
      token = lexer.nextToken()
      output_stream.write(f'Loc=<{token.line}:{lexer.column}>  {lexer.symbolicNames[token.type]} {token.text}\n')
  except:
    print("Error: output file does not open")
    sys.exit(0)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("input", type=str, help="Path to javascript file", metavar="Input file",)
  parser.add_argument("output", type=str, help="Path to output file", metavar="Output file",)
  args = parser.parse_args()

  javascript_lexer(args.input, args.output)
 
if __name__ == '__main__':
  main()