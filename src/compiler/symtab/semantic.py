import sys
sys.path.append('src/compiler')

from ast_tree import *
from antlr4 import *

class Semantic:
  def __init__(self, errors, token):
    self.errors = errors;
    self.token = token

  def get_type(self, node, scope):
    if isinstance(node, String_literal):
      return 'str'

    if isinstance(node, Integer_literal):
      return 'int'

    if isinstance(node, Array):
      return 'array'

    if isinstance(node, Method_call) and node.method_name == 'read_int':
      return 'int'

    if isinstance(node, Function_call):
      return 'int'

    if isinstance(node, Id):
      symbol = scope.resolve(node.name, True, None)
      if symbol:
        return symbol.type

    if isinstance(node, BinaryExpression):
      if isinstance(node.left, BinaryExpression):
        self.get_type(node.left, scope)

      if isinstance(node.right, BinaryExpression):
        self.get_type(node.right, scope)

      left_type = self.get_type(node.left, scope)
      right_type = self.get_type(node.right, scope)

      return self.compare_types(left_type, right_type, node.operation)
  
  def compare_types(self, left, right, operation):
    if left != right:
      self.errors.append(f"Error: line {self.token.line} unsupported operand type(s) for {operation} {left} and {right}")
    else:
      return left

  def compare_func_args(self, name, args, func_args):
    if func_args.get(name) == None:
      self.errors.append(f"Error: line {self.token.line} undefined function {name}()")
      return

    if len(func_args.get(name)) != len(args):
      self.errors.append(f"Error: line {self.token.line} invalid number of arguments {name}() takes {len(func_args[name])}, given {len(args)}")
