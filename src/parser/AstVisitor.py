import sys
from build_antlr.JSParser import JSParser
from Ast import *
from antlr4 import *

class AstVisitor():
  def visit(self, tree):
    return tree.accept(self)

  def astVisitProgram(self, ctx:Program):
    nodes = []

    for i in range(len(ctx.children)):
      nodes.append(self.visit(ctx.children[i]))

    return {
      "program": nodes,
    }

  def astVisitFunction_declaration(self, ctx:Function_declaration):
    body = []

    for i in range(len(ctx.body)):
      body.append(self.visit(ctx.body[i]))

    return {
      "function_declaration": {
        "name": ctx.name,
        "arg_list": ctx.arg_list,
        "body": body
      }
    }

  def astVisitStatement(self, ctx:Statement):
    return {
      "statement": self.visit(ctx.statement)
    }

  def astVisitFunction_call(self, ctx:Function_call):
    return {
      "function_call": {
        "name": ctx.name,
        "arg_list": ctx.arg_list
      }
    }

  def astVisitMethod_call(self, ctx:Method_call):
    return {
      "method_call": {
        "object_name": ctx.object_name,
        "method_name": ctx.method_name,
        "arg_list": ctx.arg_list
      }
    }