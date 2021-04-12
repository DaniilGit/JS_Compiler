import sys
from build_antlr.JSParser import JSParser
from Ast import *
from antlr4 import *

class JSVisitor(ParseTreeVisitor):
  def visitProgram(self, ctx:JSParser.ProgramContext):
    program = Program()

    for child in ctx.children:
      program.children.append(self.visit(child))

    return program

  def visitFunction_declaration(self, ctx:JSParser.Function_declarationContext): # Объявление функции
    function = Function_declaration()
    function.name = ctx.ID(0).getText()

    for i in range(1, len(ctx.ID())):
      function.arg_list.append(ctx.ID(i).getText()) 

    for child in ctx.statement():
      function.body.append(self.visit(child))

    return function

  def visitStatement(self, ctx:JSParser.StatementContext): # Statement
    statement = Statement()
    statement.statement = self.visit(ctx.getChild(0))

    return statement

  def visitFunction_call(self, ctx:JSParser.Function_callContext): # Вызов функции 
    function = Function_call()
    function.name = ctx.ID().getText()

    for arg in ctx.argument():
      function.arg_list.append(arg.getText()) 

    return function

  def visitMethod_call(self, ctx:JSParser.Method_callContext): # Вызов метода
    method = Method_call()
    method.object_name = ctx.ID(0).getText()
    method.method_name = ctx.ID(1).getText()

    if ctx.argument() != []:
      for arg in ctx.argument():
        method.arg_list.append(self.visit(arg))

    return method

  def visitDeclaration(self, ctx:JSParser.DeclarationContext): # Объявление переменной
    declaration = Declaration()
    declaration.type = ctx.getChild(0).getText()
    declaration.name = ctx.ID().getText()

    if ctx.expression() != None:
      declaration.value = self.visit(ctx.expression())
    elif ctx.array_value() != []:
      array = []
      for item in ctx.array_value():
        array.append(self.visit(item))
      declaration.value = array
    elif ctx.argument() != None:
      declaration.value = ctx.argument().getText()
    
    return declaration

  def visitAssign(self, ctx:JSParser.AssignContext): # Присваивание
    assign = Assign()
    assign.name = ctx.getChild(0).getText()
    assign.operation = ctx.getChild(1).getText()

    if ctx.expression() != None:
      assign.value = self.visit(ctx.expression())
    elif ctx.array_value() != []:
      array = []
      for item in ctx.array_value():
        array.append(self.visit(item))
      assign.value = array
    elif ctx.argument() != None:
      assign.value = ctx.argument().getText()

    return assign

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
    return_statement = Return_statement()
    return_statement.value = ctx.argument().getText()

    return return_statement

  def visitFor_loop(self, ctx:JSParser.For_loopContext): # Цикл for
    loop = For_loop()
    loop.start = self.visit(ctx.for_start())
    loop.condition = self.visit(ctx.condition())
    loop.step = self.visit(ctx.for_step())

    for child in ctx.statement():
      loop.body.append(self.visit(child))

    return loop

  def visitWhile_loop(self, ctx:JSParser.While_loopContext): # Цикл while
    loop = While_loop()
    loop.condition = self.visit(ctx.condition())

    for child in ctx.statement():
      loop.body.append(self.visit(child))

    return loop

  def visitInstruction_if(self, ctx:JSParser.Instruction_ifContext): # Конструкция If
    instruction = Instruction_if()
    instruction.condition = self.visit(ctx.condition())

    for child in ctx.statement():
      instruction.body.append(self.visit(child))

    if ctx.instruction_elseif() != None:
      for child in ctx.instruction_elseif():
        instruction.instuction_elseif.append(self.visit(child))

    if ctx.instruction_else() != None:
      instruction.instuction_else = self.visit(ctx.instruction_else())

    return instruction

  def visitInstruction_elseif(self, ctx:JSParser.Instruction_elseifContext): # Конструкция else if
    instruction = Instruction_elseif()
    instruction.condition = self.visit(ctx.condition())

    for child in ctx.statement():
      instruction.body.append(self.visit(child))

    return instruction

  def visitInstruction_else(self, ctx:JSParser.Instruction_elseContext): # Констркуция else
    instruction = Instruction_else()

    for child in ctx.statement():
      instruction.body.append(self.visit(child))

    return instruction

  def visitCondition(self, ctx:JSParser.ConditionContext): # Условие в циклах
    condition = Condition()
    condition.left_argument = self.visit(ctx.getChild(0))
    condition.operation = ctx.getChild(1).getText()
    condition.right_argument = self.visit(ctx.getChild(2))

    return condition

  def visitArgument(self, ctx:JSParser.ArgumentContext): # Аргумент передаваемый в метод или функцию
    if (ctx.getChild(0) == ctx.array_element() 
        or ctx.getChild(0) == ctx.object_property() 
          or ctx.getChild(0) == ctx.method_call()):
      return self.visit(ctx.getChild(0))
    else:
      return ctx.getChild(0).getText()

  def visitArray_element(self, ctx:JSParser.Array_elementContext): # Элемент массива
    array = Array_element()
    array.name = ctx.ID(0).getText()

    if ctx.getChild(2) == ctx.expression():
      array.body = self.visit(ctx.expression())
    else:
      array.body = ctx.getChild(2).getText()
    
    return array

  def visitObject_property(self, ctx:JSParser.Object_propertyContext): # Свойство объекта
    obj = Object_property()
    obj.object_name = ctx.ID(0).getText()
    obj.property = ctx.ID(1).getText()

    return obj

  def visitArray_value(self, ctx:JSParser.Array_valueContext):
    return ctx.getChild(0).getText()

  def visitFor_start(self, ctx:JSParser.For_startContext):
    return self.visit(ctx.getChild(0))

  def visitFor_step(self, ctx:JSParser.For_stepContext):
    return self.visit(ctx.getChild(0))
