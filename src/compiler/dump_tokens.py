from build_antlr.JSLexer import JSLexer
from antlr4 import *

def dump_tokens(input, output):
  input_stream = FileStream(input)
  lexer = JSLexer(input_stream)

  while lexer._hitEOF != True:
    token = lexer.nextToken()
    output.write(f'Loc=<{token.line}:{lexer.column}>  {lexer.symbolicNames[token.type]} {token.text}\n')