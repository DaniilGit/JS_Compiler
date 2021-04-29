import sys
sys.path.append('src/parser/symtab')
from ast_tree import *
from sym import Symbol

class Scope():
  def __init__(self, name, parent):
    self.name = name
    self.hash_table = {}
    self.parent = parent

  def define(self, symbol, position, errors):
    if self.hash_table.get(symbol.name):
      errors.append(f"Error: line {position} redefinition symbol - {symbol.name}")
      return None

    self.hash_table[symbol.name] = symbol.hash_code
  
  def resolve(self, name, position, errors):
    if self.hash_table.get(name):
      return Symbol(name, position)

    if self.parent:
      return self.parent.resolve(name, position, errors)
  
    errors.append(f"Error: line {position} undefined symbol - {name}")
    
