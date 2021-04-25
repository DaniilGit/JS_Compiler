import sys
from build_antlr.JSParser import JSParser
from ast_tree import *
from antlr4 import *
from symtab.sym import Symbol
from symtab.scope import Scope

class AstVisitor():
  def visit(self, tree):
    return tree.accept(self)

  def astVisitProgram(self, ctx:Program):
    nodes = []

    for child in ctx.children:
      nodes.append(self.visit(child))

    return {
      "program": nodes,
    }

  def astVisitFunction_declaration(self, ctx:Function_declaration): # Объявление функции 
    body = []

    for child in ctx.body:
      body.append(self.visit(child))

    return {
      "function_declaration": {
        "name": ctx.name,
        "arg_list": ctx.arg_list,
        "body": body
      }
    }

  def astVisitStatement(self, ctx:Statement): # Statement
    return {
      "statement": self.visit(ctx.statement)
    }

  def astVisitFunction_call(self, ctx:Function_call): # Вызов функции
    arg_list = []

    for arg in ctx.arg_list:
      if isinstance(arg, str):
        arg_list.append(arg)
      else:
        arg_list.append(self.visit(arg))

    return {
      "function_call": {
        "name": ctx.name,
        "arg_list": arg_list
      }
    }

  def astVisitMethod_call(self, ctx:Method_call): # Вызов метода
    arg_list = []

    for arg in ctx.arg_list:
      if isinstance(arg, str):
        arg_list.append(arg)
      else:
        arg_list.append(self.visit(arg))

    return {
      "method_call": {
        "object_name": ctx.object_name,
        "method_name": ctx.method_name,
        "arg_list": arg_list
      }
    }
  
  def astVisitDeclaration(self, ctx:Declaration): # Объявление переменной
    value = ''

    if isinstance(ctx.value, str) or isinstance(ctx.value, list):
      value = ctx.value
    else: 
      value = self.visit(ctx.value) 

    return {
      "Declaration": {
        "type": ctx.type,
        "name": ctx.name,
        "value": value
      }
    }

  def astVisitAssign(self, ctx:Assign): # Присваивание
    value = ''

    if isinstance(ctx.value, str) or isinstance(ctx.value, list): 
      value = ctx.value
    else: 
      value = self.visit(ctx.value) 

    return {
      "assign": {
        "name": self.visit(ctx.name),
        "operation": ctx.operation,
        "value": value
      }
    }

  def astVisitBinaryExpression(self, ctx:BinaryExpression):
    left = ''
    right = ''
    operation = ctx.operation

    if isinstance(ctx.left, str):
      left = ctx.left
    else:
      left = self.visit(ctx.left)

    if isinstance(ctx.right, str):
      right = ctx.right
    else:
      right = self.visit(ctx.right)
    
    return {
      "BinaryExpression": {
        "operation": operation,
        "left_argument": left,
        "right_argument": right
      }
    }


  def astVisitReturn_statement(self, ctx:Return_statement): # Return 
    return {
      "return": self.visit(ctx.value)
    }

  def astVisitFor_loop(self, ctx:For_loop): # Цикл for
    body = []

    for child in ctx.body:
      body.append(self.visit(child))

    return {
      "for_loop": {
        "start": self.visit(ctx.start),
        "condition": self.visit(ctx.condition),
        "step": self.visit(ctx.step),
        "body": body
      }
    }

  def astVisitWhile_loop(self, ctx:While_loop): # Цикл while
    body = []

    for child in ctx.body:
      body.append(self.visit(child))

    return {
      "while_loop": {
        "condition": self.visit(ctx.condition),
        "body": body
      }
    }

  def astVisitInstruction_if(self, ctx:Instruction_if): # Конструкция If
    body = []
    instr_elseif = []
    instr_else = ''

    for child in ctx.body:
      body.append(self.visit(child))

    for child in ctx.instuction_elseif:
      instr_elseif.append(self.visit(child))

    if ctx.instuction_else != '':
      instr_else = self.visit(ctx.instuction_else)
  
    return {
      "if": {
        "condition": self.visit(ctx.condition),
        "body": body,
        "else if": instr_elseif,
        "else": instr_else,
      }
    }

  def astVisitInstruction_elseif(self, ctx:Instruction_elseif): # Конструкция else if
    body = []

    for child in ctx.body:
      body.append(self.visit(child))

    return {
      "condition": self.visit(ctx.condition),
      "body": body,
    }

  def astVisitInstruction_else(self, ctx:Instruction_else): # Констркуция else
    body = []

    for child in ctx.body:
      body.append(self.visit(child))

    return {
      "body": body,
    }

  def astVisitArray_element(self, ctx:Array_element): # Элемент массива
    body = ''

    if isinstance(ctx.body, Expression):
      body = self.visit(ctx.body)
    else:
      body = ctx.body

    return {
      "array_element": {
        "name": self.visit(ctx.name),
        "body": body
      }
    }

  def astVisitCondition(self, ctx:Condition): # Условие в циклах
    left = ''
    right = ''

    if isinstance(ctx.left_argument, str): 
      left = ctx.left_argument
    else:
      left = self.visit(ctx.left_argument)  

    if isinstance(ctx.right_argument, str): 
      right = ctx.right_argument
    else:
      right = self.visit(ctx.right_argument) 

    return {
      "left_argument": left,
      "operation": ctx.operation,
      "right_argument": right 
    }

  def astVisitObject_property(self, ctx:Object_property): # Свойство объекта
    return {
      "object_property": {
        "object_name": ctx.object_name,
        "property": ctx.property
      }
    }

  def astVisitId(self, ctx:Id): # Идентификаторы
    return ctx.name