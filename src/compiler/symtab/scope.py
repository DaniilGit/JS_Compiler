import sys
sys.path.append('src/compiler/ast')
sys.path.append('src/compiler/symtab')

from ast_tree import *

class Scope():
  def __init__(self, name, parent):
    self.name = name
    self.hash_table = {}
    self.parent = parent
    self.func_args = {} # Словарь где ключ - имя функции, значение - кол-во аргументов

  def define(self, symbol, position, errors):
    if self.hash_table.get(symbol.name):
      errors.append(f"Error: line {position} redefinition symbol - {symbol.name}")
      return None

    self.hash_table[symbol.name] = symbol
  
  def resolve(self, name, position, errors):
    if self.hash_table.get(name):
      return self.hash_table[name]

    if self.parent:
      return self.parent.resolve(name, position, errors)
  
    if errors != None:
      errors.append(f"Error: line {position} undefined symbol - {name}")
    
