import sys
sys.path.append('src/parser')
from ast_tree import *
from random import randint

class Symbol:
  def __init__(self, name, position):
    self.name = name
    self.hash_code = hash(position)