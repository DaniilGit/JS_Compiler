import sys
sys.path.append('src/compiler')

class Symbol:
  def __init__(self, name, type, position):
    self.name = name
    self.type = type
    self.hash_code = hash(position)