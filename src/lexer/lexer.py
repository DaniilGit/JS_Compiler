import sys
sys.path.append('src/grammar/build-antlr-lexer')
sys.path.append('src/grammar/antlr-runtime-python')
from JSLexer import JSLexer
from antlr4 import *

def JavaScriptLexer(input, output):
  input_stream = FileStream(input)
  lexer = JSLexer(input_stream)

  if output != "print":
    output_stream = open(output, 'w')

  while lexer._hitEOF != True:
    token = lexer.nextToken()
    if output == "print":
      print(f'Loc=<{token.line}:{lexer.column}>  {lexer.symbolicNames[token.type]} {token.text}')
    else:
      output_stream.write(f'Loc=<{token.line}:{lexer.column}>  {lexer.symbolicNames[token.type]} {token.text}\n')


def main(argv):
  JavaScriptLexer(argv[1], "print")
 
if __name__ == '__main__':
  main(sys.argv)