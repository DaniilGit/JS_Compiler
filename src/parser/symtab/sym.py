import sys
sys.path.append('src/parser')
from ast_tree import *
from random import randint

class Symbol:
  def __init__(self, name):
    self.name = name
    self.hash_code = randint(-1000000, 1000000)