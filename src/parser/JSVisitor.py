import sys
from build_antlr.JSParser import JSParser
from Ast import *
from antlr4 import *

class JSVisitor(ParseTreeVisitor):
  def visitProgram(self, ctx:JSParser.ProgramContext):
    program = Program()

    for i in range(ctx.getChildCount()):
      program.children.append(self.visit(ctx.getChild(i)))

    return program

  def visitFunction_declaration(self, ctx:JSParser.Function_declarationContext):
    function = Function_declaration()
    function.name = ctx.ID().getText()
    function.arg_list = [] # Пока пусто, потом будет цикл

    for i in range(len(ctx.statement())):
      function.body.append(self.visit(ctx.statement(i)))

    return function

  def visitStatement(self, ctx:JSParser.StatementContext):
    statement = Statement()
    statement.statement = self.visit(ctx.getChild(0))

    return statement

  def visitFunction_call(self, ctx:JSParser.Function_callContext):
    function = Function_call()
    function.name = ctx.ID().getText()
    function.arg_list = [] # Пока пусто, потом будет цикл

    return function

  def visitMethod_call(self, ctx:JSParser.Method_callContext):
    method = Method_call()
    method.object_name = ctx.ID(0).getText()
    method.method_name = ctx.ID(1).getText()
    method.arg_list.append(ctx.STRING().getText()) # Здесь пока добавление только 1 аргумента, потом будет цикл

    return method