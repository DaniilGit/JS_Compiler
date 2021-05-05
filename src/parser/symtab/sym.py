import sys
sys.path.append('src/parser')
from ast_tree import *
from random import randint

class Symbol:
  def __init__(self, name, type, position):
    self.name = name
    self.type = type
    self.hash_code = hash(position)