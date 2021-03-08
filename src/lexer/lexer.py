import sys
sys.path.append('./grammar/build-antlr-lexer')

from JSLexer import JSLexer
from antlr4 import *

def main(argv):
  input_stream = FileStream(argv[1])
  lexer = JSLexer(input_stream)

  while lexer._hitEOF != True:
    token = lexer.nextToken()
    print(f'Loc=<{token.line}:{lexer.column}>  {lexer.symbolicNames[token.type]} {token.text}')
 
if __name__ == '__main__':
    main(sys.argv)