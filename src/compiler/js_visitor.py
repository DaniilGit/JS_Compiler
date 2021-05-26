from antlr4 import *

from build_antlr.JSParser import JSParser
from ast_tree import *

class JSVisitor(ParseTreeVisitor):
  def visitProgram(self, ctx:JSParser.ProgramContext):
    children = []

    for child in ctx.children:
      if self.visit(child) == None:
        continue
      children.append(self.visit(child))

    return Program(children)

  def visitFunction_declaration(self, ctx:JSParser.Function_declarationContext): # Объявление функции
    name = ctx.ID(0).getText()
    token_scope = ctx.ID(0).getSymbol()
    arg_list = []
    body = []

    for i in range(1, len(ctx.ID())):
      arg_list.append(Id(ctx.ID(i).getText(), ctx.ID(i).getSymbol()))  

    for child in ctx.statement():
      body.append(self.visit(child))

    return Function_declaration(name, body, arg_list, token_scope)

  def visitStatement(self, ctx:JSParser.StatementContext): # Statement
    statement = self.visit(ctx.getChild(0))

    return Statement(statement)

  def visitFunction_call(self, ctx:JSParser.Function_callContext): # Вызов функции 
    name = ctx.ID().getText()
    token = ctx.ID().getSymbol()
    arg_list = []

    for arg in ctx.expression():
      arg_list.append(self.visit(arg)) 

    return Function_call(name, arg_list, token)

  def visitMethod_call(self, ctx:JSParser.Method_callContext): # Вызов метода
    object_name = ctx.ID(0).getText()
    method_name = ctx.ID(1).getText()
    arg_list = []

    if ctx.argument() != []:
      for arg in ctx.argument():
        arg_list.append(self.visit(arg))

    return Method_call(object_name, method_name, arg_list)

  def visitDeclaration(self, ctx:JSParser.DeclarationContext): # Объявление переменной
    type_value = ctx.getChild(0).getText()
    name = ctx.ID().getText()
    token = ctx.ID().getSymbol()

    if ctx.function_call() != None:
      value = self.visit(ctx.function_call())
    if ctx.expression() != None:
      value = self.visit(ctx.expression())
    elif ctx.array() != None:
      value = self.visit(ctx.array())
    
    return Declaration(type_value, name, value, token)

  def visitAssign(self, ctx:JSParser.AssignContext): # Присваивание
    if (ctx.ID() != None):
      name = Id(ctx.ID().getText(), ctx.ID().getSymbol())
    else:
      name = self.visit(ctx.getChild(0))

    token = ctx.ID().getSymbol()
    operation = ctx.getChild(1).getText()
  
    if ctx.function_call() != None:
      value = self.visit(ctx.function_call())
    if ctx.expression() != None:
      value = self.visit(ctx.expression())
    elif ctx.array() != None:
      value = self.visit(ctx.array())

    return Assign(name, operation, value, token)

  def visitExpression(self, ctx:JSParser.ExpressionContext): # Выражение
    if ctx.operation == None and ctx.argument() == None:
      return self.visit(ctx.expression(0))
    elif ctx.operation == None:
      return self.visit(ctx.argument())

    operation = ctx.operation.text
    left = self.visit(ctx.expression(0))
    right = self.visit(ctx.expression(1))

    expression = BinaryExpression(operation, left, right)
  
    return expression

  def visitReturn_statement(self, ctx:JSParser.Return_statementContext): # Return
    value = self.visit(ctx.expression())

    return Return_statement(value)

  def visitFor_loop(self, ctx:JSParser.For_loopContext): # Цикл for
    start = self.visit(ctx.for_start())
    condition = self.visit(ctx.condition())
    step = self.visit(ctx.for_step())
    body = []
    token_scope = ctx.FOR().getSymbol()

    for child in ctx.statement():
      body.append(self.visit(child))

    return For_loop(start, condition, step, body, token_scope)

  def visitWhile_loop(self, ctx:JSParser.While_loopContext): # Цикл while
    condition = self.visit(ctx.condition())
    body = []
    token_scope = ctx.WHILE().getSymbol()

    for child in ctx.statement():
      body.append(self.visit(child))

    return While_loop(condition, body, token_scope)

  def visitInstruction_if(self, ctx:JSParser.Instruction_ifContext): # Конструкция If
    condition = self.visit(ctx.condition())
    body = []
    instr_elseif = []
    instr_else = ''
    token_scope = ctx.IF().getSymbol()

    for child in ctx.statement():
      body.append(self.visit(child))

    if ctx.instruction_elseif() != None:
      for child in ctx.instruction_elseif():
        instr_elseif.append(self.visit(child))

    if ctx.instruction_else() != None:
      instr_else = self.visit(ctx.instruction_else())

    return Instruction_if(condition, body, instr_elseif, instr_else, token_scope)

  def visitInstruction_elseif(self, ctx:JSParser.Instruction_elseifContext): # Конструкция else if
    condition = self.visit(ctx.condition())
    body = []
    token_scope = ctx.ELSE().getSymbol()

    for child in ctx.statement():
      body.append(self.visit(child))

    return Instruction_elseif(condition, body, token_scope)

  def visitInstruction_else(self, ctx:JSParser.Instruction_elseContext): # Констркуция else
    body = []
    token_scope = ctx.ELSE().getSymbol()

    for child in ctx.statement():
      body.append(self.visit(child))

    return Instruction_else(body, token_scope)

  def visitCondition(self, ctx:JSParser.ConditionContext): # Условие в циклах
    left_argument = self.visit(ctx.getChild(0))
    operation = ctx.getChild(1).getText()
    right_argument = self.visit(ctx.getChild(2))

    return Condition(left_argument, operation, right_argument)

  def visitArgument(self, ctx:JSParser.ArgumentContext): # Аргумент передаваемый в метод или функцию
    if (ctx.getChild(0) == ctx.array_element() 
        or ctx.getChild(0) == ctx.object_property() 
          or ctx.getChild(0) == ctx.method_call()
            or ctx.getChild(0) == ctx.integer_literal()
              or ctx.getChild(0) == ctx.string_literal()
                or ctx.getChild(0) == ctx.function_call()):
      return self.visit(ctx.getChild(0))
    elif (ctx.ID() != None):
      return Id(ctx.ID().getText(), ctx.ID().getSymbol())
    else:
      return ctx.getChild(0).getText()

  def visitArray_element(self, ctx:JSParser.Array_elementContext): # Элемент массива
    name = Id(ctx.ID(0).getText(), ctx.ID(0).getSymbol())

    if ctx.getChild(2) == ctx.expression() or ctx.getChild(2) == ctx.integer_literal():
      body = self.visit(ctx.getChild(2))
    else:
      body = ctx.getChild(2).getText()
    
    return Array_element(name, body)

  def visitObject_property(self, ctx:JSParser.Object_propertyContext): # Свойство объекта
    object_name = ctx.ID(0).getText()
    object_property = ctx.ID(1).getText()

    return Object_property(object_name, object_property)

  def visitArray(self, ctx:JSParser.ArrayContext):
    list_value = []

    for elem in ctx.array_value():
      list_value.append(self.visit(elem))

    return Array(list_value)

  def visitFor_start(self, ctx:JSParser.For_startContext):
    return self.visit(ctx.getChild(0))

  def visitFor_step(self, ctx:JSParser.For_stepContext):
    return self.visit(ctx.getChild(0))
  
  def visitArray_value(self, ctx:JSParser.Array_valueContext):
    return self.visit(ctx.getChild(0))

  def visitString_literal(self, ctx:JSParser.String_literalContext):
    value = ctx.getChild(0).getText()
    return String_literal(value)

  def visitInteger_literal(self, ctx:JSParser.Integer_literalContext):
    value = ctx.getChild(0).getText()
    return Integer_literal(value)
