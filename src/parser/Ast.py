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