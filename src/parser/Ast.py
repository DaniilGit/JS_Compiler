import sys
import argparse
from build_antlr.JSParser import JSParser
from antlr4 import *

class Program:
  def __init__(self):
    self.children = []

class Function_declaration:
  def __init__(self):
    self.name = ''
    self.body = []
    self.arg_list = []

  def accept(self, visitor):
    return visitor.astVisitFunction_declaration(self)

class Statement:
  def __init__(self):
    self.statement = ''

  def accept(self, visitor):
    return visitor.astVisitStatement(self)

class Function_call:
  def __init__(self):
    self.name = ''
    self.arg_list = []

  def accept(self, visitor):
    return visitor.astVisitFunction_call(self)

class Method_call:
  def __init__(self):
    self.object_name = ''
    self.method_name = ''
    self.arg_list = []

  def accept(self, visitor):
    return visitor.astVisitMethod_call(self)

class Declaration:
  def __init__(self):
    self.type = ''
    self.name = ''
    self.value = ''

  def accept(self, visitor):
    return visitor.astVisitDeclaration(self)

class Assign:
  def __init__(self):
    self.name = ''
    self.operation = ''
    self.value = ''

  def accept(self, visitor):
    return visitor.astVisitAssign(self)

class Expression:
  def __init__(self):
    self.operation = ''
    self.id = ''
    self.literal = ''

  def accept(self, visitor):
    return visitor.astVisitExpression(self)

class BinaryExpression(Expression):
  def __init__(self):
    self.operation = ''
    self.left_sibling = ''
    self.right_sibling = ''
  
  def accept(self, visitor):
    return visitor.astVisitExpression(self)

class Return_statement:
  def __init__(self):
    self.value = ''

  def accept(self, visitor):
    return visitor.astVisitReturn_statement(self)

class Array_element:
  def __init__(self):
    self.name = ''
    self.body = ''

  def accept(self, visitor):
    return visitor.astVisitArray_element(self)

class For_loop:
  def __init__(self):
    self.start = ''
    self.condition = ''
    self.step = ''
    self.body = []

  def accept(self, visitor):
    return visitor.astVisitFor_loop(self)

class While_loop:
  def __init__(self):
    self.condition = ''
    self.body = []

  def accept(self, visitor):
    return visitor.astVisitWhile_loop(self)

class Instruction_if:
  def __init__(self):
    self.condition = ''
    self.body = []
    self.instuction_elseif = []
    self.instuction_else = ''

  def accept(self, visitor):
    return visitor.astVisitInstruction_if(self)

class Instruction_elseif:
  def __init__(self):
    self.condition = ''
    self.body = []

  def accept(self, visitor):
    return visitor.astVisitInstruction_elseif(self)
  
class Instruction_else:
  def __init__(self):
    self.body = []

  def accept(self, visitor):
    return visitor.astVisitInstruction_else(self)

class Condition:
  def __init__(self):
    self.left_argument = ''
    self.operation = ''
    self.right_argument = ''

  def accept(self, visitor):
    return visitor.astVisitCondition(self)

class Object_property:
  def __init__(self):
    self.object_name = ''
    self.property = ''
  
  def accept(self, visitor):
    return visitor.astVisitObject_property(self)