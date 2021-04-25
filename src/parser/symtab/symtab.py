import sys
sys.path.append('src/parser/symtab')
from build_antlr.JSParser import JSParser
from ast_tree import *
from antlr4 import *
from sym import Symbol
from scope import Scope

class Symtab:
  def __init__(self, errors):
    self.scope_stack = []
    self.errors = errors

  def print_stack(self):
    for i in range(0, len(self.scope_stack)):
      print(self.scope_stack[i].hash_table)

  def visit(self, tree):
    return tree.accept(self)

  def astVisitProgram(self, ctx:Program): # Глобальная область видимости
    scope = Scope('global', None)
    self.scope_stack.append(scope)

    for child in ctx.children:
      self.visit(child)

    return None

  def astVisitFunction_declaration(self, ctx:Function_declaration): # Область видимости - Объявление функции 
    scope_name = (ctx.name + ' ' 
      + str(ctx.token_scope.line) + ':' 
        + str(ctx.token_scope.column))
    
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    for child in ctx.body:
      self.visit(child)
    
    self.scope_stack.pop()

    return None

  def astVisitFor_loop(self, ctx:For_loop): # Область видимости - Цикл for
    scope_name = ('for' + ' ' 
      + str(ctx.token_scope.line) + ':' 
        + str(ctx.token_scope.column))
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    self.visit(ctx.start)
    self.visit(ctx.condition)
    self.visit(ctx.step)
    for child in ctx.body:
      self.visit(child)

    self.scope_stack.pop()

    return None

  def astVisitWhile_loop(self, ctx:While_loop): # Область видимости - Цикл while
    scope_name = ('while' + ' ' 
      + str(ctx.token_scope.line) + ':' 
        + str(ctx.token_scope.column))
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    self.visit(ctx.condition)
    for child in ctx.body:
      self.visit(child)
    
    self.scope_stack.pop()

    return None

  def astVisitInstruction_if(self, ctx:Instruction_if): # Область видимости - Конструкция If
    scope_name = ('if' + ' ' 
      + str(ctx.token_scope.line) + ':' 
        + str(ctx.token_scope.column))

    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    self.visit(ctx.condition)
    for child in ctx.body:
      self.visit(child)

    self.scope_stack.pop()

    for child in ctx.instuction_elseif:
      self.visit(child)

    if ctx.instuction_else != '':
      self.visit(ctx.instuction_else)
  
    return None

  def astVisitInstruction_elseif(self, ctx:Instruction_elseif): # Область видимости - Конструкция else if
    scope_name = ('else if' + ' ' 
      + str(ctx.token_scope.line) + ':' 
        + str(ctx.token_scope.column))
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    self.visit(ctx.condition)
    for child in ctx.body:
      self.visit(child)

    self.scope_stack.pop()

    return None

  def astVisitInstruction_else(self, ctx:Instruction_else): # Область видимости - Констркуция else
    scope_name = ('else' + ' ' 
      + str(ctx.token_scope.line) + ':' 
        + str(ctx.token_scope.column))
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    for child in ctx.body:
      self.visit(child)

    self.scope_stack.pop()

    return None

  def astVisitDeclaration(self, ctx:Declaration): # Объявление переменной
    symbol = Symbol(ctx.name)
    scope = self.scope_stack.copy().pop()
    scope.define(symbol, ctx.token, self.errors)
    # print(scope.name, scope.hash_table)

    if not isinstance(ctx.value, str) and not isinstance(ctx.value, list):
      self.visit(ctx.value) 

    return None

  def astVisitId(self, ctx:Id): # Идентификаторы
    scope = self.scope_stack.copy().pop()
    scope.resolve(ctx.name, ctx.token, self.errors)

    return None

# Все что ниже просто обход дерева
###################################################################

  def astVisitAssign(self, ctx:Assign): # Присваивание
    self.visit(ctx.name)
    if not isinstance(ctx.value, str) and not isinstance(ctx.value, list): 
      self.visit(ctx.value) 

    return None

  def astVisitArray_element(self, ctx:Array_element): # Элемент массива
    self.visit(ctx.name)
    if isinstance(ctx.body, Expression):
      self.visit(ctx.body)

    return None

  def astVisitStatement(self, ctx:Statement): # Statement
    self.visit(ctx.statement)
    return None

  def astVisitFunction_call(self, ctx:Function_call): # Вызов функции 
    for arg in ctx.arg_list:
      if isinstance(arg, Id):
        self.visit(arg)
    return None

  def astVisitMethod_call(self, ctx:Method_call): # Вызов метода
    for arg in ctx.arg_list:
      if isinstance(arg, Id):
        self.visit(arg)

    return None

  def astVisitBinaryExpression(self, ctx:BinaryExpression):
    if not isinstance(ctx.left, str):
      self.visit(ctx.left)
    if not isinstance(ctx.right, str):
      self.visit(ctx.right)
    
    return None

  def astVisitReturn_statement(self, ctx:Return_statement): # Return
    self.visit(ctx.value) 

    return None

  def astVisitCondition(self, ctx:Condition): # Условие в циклах
    if not isinstance(ctx.left_argument, str): 
      self.visit(ctx.left_argument)  
    if not isinstance(ctx.right_argument, str): 
      self.visit(ctx.right_argument) 

    return None

  def astVisitObject_property(self, ctx:Object_property): # Свойство объекта
    return None