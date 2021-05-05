import sys
sys.path.append('src/parser/symtab')
from build_antlr.JSParser import JSParser
from ast_tree import *
from antlr4 import *
from semantic import Semantic
from sym import Symbol
from scope import Scope

class Symtab:
  def __init__(self, errors):
    self.scope_stack = []
    self.errors = errors
    self.types_table = {}

  def visit(self, tree):
    return tree.accept(self)

  def print_stack(self):
    for scope in self.scope_stack:
      print(scope.name, scope.hash_table)

  def set_scope_name(self, name, line, column):
    return f'{name} {line}:{column}'

  def astVisitProgram(self, ctx:Program): # Глобальная область видимости
    scope = Scope('global', None)
    self.scope_stack.append(scope)

    for child in ctx.children:
      self.visit(child)

    return self.types_table

  def astVisitFunction_declaration(self, ctx:Function_declaration): # Область видимости - Объявление функции 
    scope_name = self.set_scope_name(ctx.name, ctx.token_scope.line, ctx.token_scope.column)
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    parent.func_args[ctx.name] = ctx.arg_list
    scope.func_args[ctx.name] = ctx.arg_list

    for child in ctx.body:
      self.visit(child)
    
    self.scope_stack.pop()

  def astVisitFor_loop(self, ctx:For_loop): # Область видимости - Цикл for
    scope_name = self.set_scope_name('for', ctx.token_scope.line, ctx.token_scope.column)
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    self.visit(ctx.start)
    self.visit(ctx.condition)
    self.visit(ctx.step)

    for child in ctx.body:
      self.visit(child)

    self.scope_stack.pop()

  def astVisitWhile_loop(self, ctx:While_loop): # Область видимости - Цикл while
    scope_name = self.set_scope_name('while', ctx.token_scope.line, ctx.token_scope.column)
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    self.visit(ctx.condition)
    for child in ctx.body:
      self.visit(child)
    
    self.scope_stack.pop()

  def astVisitInstruction_if(self, ctx:Instruction_if): # Область видимости - Конструкция If
    scope_name = self.set_scope_name('if', ctx.token_scope.line, ctx.token_scope.column)

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

  def astVisitInstruction_elseif(self, ctx:Instruction_elseif): # Область видимости - Конструкция else if
    scope_name = self.set_scope_name('else if', ctx.token_scope.line, ctx.token_scope.column)
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    self.visit(ctx.condition)
    for child in ctx.body:
      self.visit(child)

    self.scope_stack.pop()

  def astVisitInstruction_else(self, ctx:Instruction_else): # Область видимости - Констркуция else
    scope_name = self.set_scope_name('else', ctx.token_scope.line, ctx.token_scope.column)
    parent = self.scope_stack.copy().pop()

    scope = Scope(scope_name, parent)
    self.scope_stack.append(scope)

    for child in ctx.body:
      self.visit(child)

    self.scope_stack.pop()

  def astVisitDeclaration(self, ctx:Declaration): # Объявление переменной
    position = f'{ctx.token.line}:{ctx.token.column}'
    scope = self.scope_stack.copy().pop()

    type = Semantic(self.errors, ctx.token).get_type(ctx.value, scope)
    symbol = Symbol(ctx.name, type, position)
    self.types_table[ctx] = symbol.type # Хеш таблица, в который ключ - узел ast, значение - тип

    scope.define(symbol, position, self.errors)

    if not isinstance(ctx.value, str) and not isinstance(ctx.value, list):
      self.visit(ctx.value) 

  def astVisitId(self, ctx:Id): # Идентификаторы
    position = f'{ctx.token.line}:{ctx.token.column}'
    scope = self.scope_stack.copy().pop()
    symbol = scope.resolve(ctx.name, position, self.errors)
    # print(symbol.name, symbol.type, position)
    if symbol:
      return symbol.type

  def astVisitAssign(self, ctx:Assign): # Присваивание
    scope = self.scope_stack.copy().pop()

    left_type = self.visit(ctx.name)
    right_type = Semantic(self.errors, ctx.token).get_type(ctx.value, scope)

    Semantic(self.errors, ctx.token).compare_types(left_type, right_type, ctx.operation)

    if not isinstance(ctx.value, str) and not isinstance(ctx.value, list): 
      self.visit(ctx.value) 

  def astVisitFunction_call(self, ctx:Function_call): # Вызов функции
    scope = self.scope_stack.copy().pop()

    Semantic(self.errors, ctx.token).compare_func_args(ctx.name, ctx.arg_list, scope.func_args)

    for arg in ctx.arg_list:
      if isinstance(arg, Id):
        self.visit(arg)

#########################################

  def astVisitArray_element(self, ctx:Array_element): # Элемент массива
    self.visit(ctx.name)
    if isinstance(ctx.body, Expression):
      self.visit(ctx.body)

  def astVisitStatement(self, ctx:Statement): # Statement
    self.visit(ctx.statement)

  def astVisitMethod_call(self, ctx:Method_call): # Вызов метода
    for arg in ctx.arg_list:
      if isinstance(arg, Id):
        self.visit(arg)

  def astVisitBinaryExpression(self, ctx:BinaryExpression):
    if not isinstance(ctx.left, str):
      self.visit(ctx.left)
    if not isinstance(ctx.right, str):
      self.visit(ctx.right)

  def astVisitReturn_statement(self, ctx:Return_statement): # Return
    self.visit(ctx.value) 

  def astVisitCondition(self, ctx:Condition): # Условие в циклах
    if not isinstance(ctx.left_argument, str): 
      self.visit(ctx.left_argument)  
    if not isinstance(ctx.right_argument, str): 
      self.visit(ctx.right_argument) 

  def astVisitObject_property(self, ctx:Object_property): # Свойство объекта
    pass

  def astVisitorArray(self, ctx:Array):
    return ctx.type

  def astVisitorInteger_literal(self, ctx:Integer_literal): # Идентификаторы
    return ctx.type

  def astVisitorString_literal(self, ctx:String_literal): # Идентификаторы
    return ctx.type