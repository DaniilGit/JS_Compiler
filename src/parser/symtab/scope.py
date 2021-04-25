import sys
sys.path.append('src/parser/symtab')
from ast_tree import *
from sym import Symbol

class Scope():
  def __init__(self, name, parent):
    self.name = name
    self.hash_table = {}
    self.parent = parent

  def define(self, symbol, token, errors):
    if self.hash_table.get(symbol.name):
      errors.append("Error: " + "line " 
        + str(token.line) + ":" + str(token.column) 
          + " redefinition symbol - " + str(symbol.name))
      return None

    self.hash_table[symbol.name] = symbol.hash_code
  
  def resolve(self, name, token, errors):
    if self.hash_table.get(name):
      return Symbol(name)

    if self.parent:
      return self.parent.resolve(name, token, errors)
  
    errors.append("Error: " + "line " 
      + str(token.line) + ":" + str(token.column) 
        + " undefined symbol - " + str(name))
    
