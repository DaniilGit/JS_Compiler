from ast import operator
import sys
sys.path.append('src/compiler')

from build_antlr.JSParser import JSParser
from ast_tree import *
from ast_visitor import AstVisitor
from antlr4 import *

class IRVisitor(AstVisitor):
  def __init__(self, symtab):
    self.symtab = symtab
    self.main_scope = ""
    self.buffer_scope = ""
    self.global_scope = ""
    self.exp_buffer = ""
    self.symbol_to_var = {}
    self.node_to_op = {}
    self.id = 0
    self.id_mark = 0
    self.check_stdin = True
    self.check_stdout = True
    self.var_stack = []
    self.func_stack = []

  def visit(self, tree):
    return tree.accept(self)

  def opExpression(self, operation, first_arg, second_arg):
    if operation == '+':
      str_op = 'add nsw'
    if operation == '*':
      str_op = 'mul nsw'
    if operation == '-':
      str_op = 'sub'
    if operation == '/':
      str_op = 'sdiv'

    operation = f'  %op_{self.id} = {str_op} i32 {first_arg}, {second_arg}\n'
    self.id += 1
    self.exp_buffer += operation

  def opCondition(self, operation, first_arg, second_arg):
    if operation == '<':
      str_op = 'icmp slt'
    if operation == '>':
      str_op = 'icmp sgt'
    if operation == '<=':
      str_op = 'icmp sle'
    if operation == '>=':
      str_op = 'icmp sge'
    if operation == '==':
      str_op = 'icmp eq'
    if operation == '!=':
      str_op = 'icmp ne'

    operation = f'  %op_{self.id} = {str_op} i32 {first_arg}, {second_arg}\n'
    self.id += 1
    return operation

  def stdin(self, type):
    if type == 'int':
      stdin_type = 'd'
      ir_type = 'i32'

    name_var = f'stdin_{self.id}'
    self.id += 1
    self.global_scope += f'@.{name_var} = private unnamed_addr constant [3 x i8] c"%{stdin_type}\\00"\n'
    readln = f'  %read_{name_var} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr ([3 x i8], [3 x i8]* @.{name_var}, i64 0, i64 0), {ir_type}* %{self.var_stack.pop()})\n\n'
    return readln

  def stdout(self, type, arg, name_var_load):
    if type == 'int':
      stdout_type = 'd'
      ir_type = 'i32'
    if type == 'str':
      stdout_type = 's'
      ir_type = 'i8*'

    if isinstance(arg, Id):
      name_var = f'{arg.name}{arg.token.line}{arg.token.column}'
      self.global_scope += f'@.{name_var} = private unnamed_addr constant [4 x i8] c"%{stdout_type}\\0A\\00"\n'
      load = f'  %tmp_{name_var} = load {ir_type}, {ir_type}* %{name_var_load}\n'
      writeln = f'  %write_{name_var} = call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.{name_var}, i64 0, i64 0), {ir_type} %tmp_{name_var})\n\n'
      return (load + writeln)
    if isinstance(arg, Integer_literal):
      name_var = f'str_{self.id}'
      self.id += 1
      self.global_scope += f'@.{name_var} = private unnamed_addr constant [4 x i8] c"%{stdout_type}\\0A\\00"\n'
      writeln = f'  %write_{name_var} = call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.{name_var}, i64 0, i64 0), {ir_type} {arg.value})\n\n'
      return writeln
    if isinstance(arg, String_literal):
      string = arg.value.split('"')[1]
      length = len(string) + 1
      name_var = f'str_{self.id}'
      self.id += 1
      self.global_scope += f'@.{name_var} = private unnamed_addr constant [4 x i8] c"%{stdout_type}\\0A\\00"\n'
      self.global_scope += f'@.literal_{name_var} = private unnamed_addr constant [{length} x i8] c"{string}\\00"\n'
      writeln = f'  %write_{name_var} = call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @.{name_var}, i64 0, i64 0), i8* getelementptr ([{length} x i8], [{length} x i8]* @.literal_{name_var}, i64 0, i64 0))\n\n'
      return writeln

  def astVisitProgram(self, ctx:Program):
    self.global_scope = f'target triple = "x86_64-pc-linux-gnu"\n'
    self.main_scope = f'\ndefine dso_local i32 @main() {{\n'

    for child in ctx.children:
      self.visit(child)

    self.main_scope += (self.buffer_scope + '  ret i32 0\n}')
    self.global_scope += self.main_scope

    return self.global_scope

  def astVisitDeclaration(self, ctx:Declaration):
    name_var = f'{ctx.name}{ctx.token.line}{ctx.token.column}'
    self.var_stack.append(name_var)
    if not isinstance(ctx.value, str) and not isinstance(ctx.value, list):
      right = self.visit(ctx.value) 

    symbol = self.symtab[ctx]
    self.symbol_to_var[symbol] = name_var

    if isinstance(right, Integer_literal):
      declr = f'  %{name_var} = alloca i32\n'
      store = f'  store i32 {right.value}, i32* %{name_var}\n\n'
      self.buffer_scope += (declr + store)

    if isinstance(right, String_literal):
      string = right.value.split('"')[1]
      length = len(string) + 1

      declr = f'  %{name_var} = alloca i8*\n'
      declr_global = f'@.{name_var} = private unnamed_addr constant [{length} x i8] c"{string}\\00"\n'
      store = f'  store i8* getelementptr inbounds ([{length} x i8], [{length} x i8]* @.{name_var}, i64 0, i64 0), i8** %{name_var}\n\n'

      self.global_scope += declr_global
      self.buffer_scope += (declr + store)

    if isinstance(right, Id):
      type_var = symbol.type
      symbol = self.symtab[right]
      name_var_load = self.symbol_to_var[symbol]

      if type_var == 'int':
        declr = f'  %{name_var} = alloca i32\n'
        load = f'  %tmp_{name_var} = load i32, i32* %{name_var_load}\n'
        store = f'  store i32 %tmp_{name_var}, i32* %{name_var}\n\n'
        self.buffer_scope += (declr + load + store)
      if type_var == 'str':
        declr = f'  %{name_var} = alloca i8*\n'
        load = f'  %tmp_{name_var} = load i8*, i8** %{name_var_load}\n'
        store = f'  store i8* %tmp_{name_var}, i8** %{name_var}\n\n'
        self.buffer_scope += (declr + load + store)
    
    if isinstance(right, BinaryExpression):
      type_var = symbol.type

      if type_var == 'int':
        declr = f'  %{name_var} = alloca i32\n'
      if type_var == 'str':
        declr = f'  %{name_var} = alloca i8*\n'

      store = f'  store i32 %op_{self.id - 1}, i32* %{name_var}\n\n'  
      self.buffer_scope += (declr + self.exp_buffer + store)
      self.exp_buffer = ''

    if isinstance(right, Method_call):
      if right.method_name == 'read_int':
        declr = f'  %{name_var} = alloca i32\n' 
        self.buffer_scope += (declr + self.exp_buffer)
      
      self.exp_buffer = ''

    if isinstance(right, Function_call):
      func_name = self.func_stack.pop()
      declr = f'  %{name_var} = alloca i32\n'
      store = f'  store i32 %func_{func_name}, i32* %{name_var}\n\n'
      self.buffer_scope += (declr + store)

  def astVisitAssign(self, ctx:Assign): 
    if not isinstance(ctx.value, str) and not isinstance(ctx.value, list):
      right = self.visit(ctx.value)

    symbol = self.symtab[ctx.name]
    name_var = self.symbol_to_var[symbol]
  
    if isinstance(right, Integer_literal):
      store = f'  store i32 {right.value}, i32* %{name_var}\n\n'
      self.buffer_scope += store

    if isinstance(right, String_literal):
      string = right.value.split('"')[1]
      length = len(string) + 1

      declr_global = f'@.{name_var} = private unnamed_addr constant [{length} x i8] c"{string}\\00"\n'
      store = f'  store i8* getelementptr inbounds ([{length} x i8], [{length} x i8]* @.{name_var}, i64 0, i64 0), i8** %{name_var}\n\n'

      self.global_scope += declr_global
      self.buffer_scope += store

    if isinstance(right, Id):
      type_var = symbol.type
      symbol = self.symtab[right]
      name_var_load = self.symbol_to_var[symbol]

      if type_var == 'int':
        load = f'  %tmp_{name_var}_{self.id} = load i32, i32* %{name_var_load}\n'
        store = f'  store i32 %tmp_{name_var}_{self.id}, i32* %{name_var}\n\n'
        self.id += 1
        self.buffer_scope += (load + store)
      if type_var == 'str':
        load = f'  %tmp_{name_var}_{self.id} = load i8*, i8** %{name_var_load}\n'
        store = f'  store i8* %tmp_{name_var}_{self.id}, i8** %{name_var}\n\n'
        self.id += 1
        self.buffer_scope += (load + store)
    
    if isinstance(right, BinaryExpression):
      store = f'  store i32 %op_{self.id - 1}, i32* %{name_var}\n\n'  
      self.buffer_scope += (self.exp_buffer + store)
      self.exp_buffer = ''

    if isinstance(right, Method_call):
      if right.method_name == 'read_int':
        self.buffer_scope += self.exp_buffer
      
      self.exp_buffer = ''
    
    if isinstance(right, Function_call):
      func_name = self.func_stack.pop()
      store = f'  store i32 %func_{func_name}, i32* %{name_var}\n\n'
      self.buffer_scope += store

  def astVisitBinaryExpression(self, ctx:BinaryExpression):
    self.visit(ctx.left)
    self.visit(ctx.right)

    if isinstance(ctx.left, Id):
      symbol = self.symtab[ctx.left]
      left_var_load = self.symbol_to_var[symbol]
      left_name_var = f'{ctx.left.name}{ctx.left.token.line}{ctx.left.token.column}'

      load = f'  %tmp_{left_name_var} = load i32, i32* %{left_var_load}\n'
      self.exp_buffer += load

      if isinstance(ctx.right, Id):
        symbol = self.symtab[ctx.right]
        right_var_load = self.symbol_to_var[symbol]
        right_name_var = f'{ctx.right.name}{ctx.right.token.line}{ctx.right.token.column}'
        first = f'%tmp_{left_name_var}'
        second = f'%tmp_{right_name_var}'

        load = f'  %tmp_{right_name_var} = load i32, i32* %{right_var_load}\n'
        self.exp_buffer += load

        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)

      if isinstance(ctx.right, Integer_literal):
        first = f'%tmp_{left_name_var}'
        second = ctx.right.value
        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)

      if isinstance(ctx.right, BinaryExpression):
        first = f'%tmp_{left_name_var}' 
        second = f'%op_{self.id - 1}'
        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)

      if isinstance(ctx.right, Function_call):
        func_name = self.func_stack.pop()
        first = f'%tmp_{left_name_var}' 
        second = f'%func_{func_name}'
        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)
      
      return ctx

    if isinstance(ctx.right, Id):
      symbol = self.symtab[ctx.right]
      right_var_load = self.symbol_to_var[symbol]
      right_name_var = f'{ctx.right.name}{ctx.right.token.line}{ctx.right.token.column}'

      load = f'  %tmp_{right_name_var} = load i32, i32* %{right_var_load}\n'
      self.exp_buffer += load

      if isinstance(ctx.left, Id):
        symbol = self.symtab[ctx.left]
        left_var_load = self.symbol_to_var[symbol]
        left_name_var = f'{ctx.left.name}{ctx.left.token.line}{ctx.left.token.column}'
        first = f'%tmp_{right_name_var}'
        second = f'%tmp_{left_name_var}'

        load = f'  %tmp_{left_name_var} = load i32, i32* %{left_var_load}\n'
        self.exp_buffer += load

        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)

      if isinstance(ctx.left, Integer_literal):
        first = ctx.left.value
        second = f'%tmp_{right_name_var}'
        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)

      if isinstance(ctx.left, BinaryExpression):
        first = f'%op_{self.id - 1}'
        second = f'%tmp_{right_name_var}'
        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)

      if isinstance(ctx.left, Function_call):
        func_name = self.func_stack.pop()
        first = f'%func_{func_name}'
        second = f'%tmp_{right_name_var}'
        self.node_to_op[ctx] = self.id
        self.opExpression(ctx.operation, first, second)
      
      return ctx

    if isinstance(ctx.left, BinaryExpression) and isinstance(ctx.right, BinaryExpression):
      first = f'%op_{self.node_to_op[ctx.left]}'
      second = f'%op_{self.node_to_op[ctx.right]}'
      self.node_to_op[ctx] = self.id
      self.opExpression(ctx.operation, first, second)

    if isinstance(ctx.left, Integer_literal) and isinstance(ctx.right, Integer_literal):
      first = ctx.left.value
      second = ctx.right.value
      self.node_to_op[ctx] = self.id
      self.opExpression(ctx.operation, first, second)
      
    if isinstance(ctx.left, BinaryExpression) and isinstance(ctx.right, Integer_literal):
      first = f'%op_{self.id - 1}'
      second = ctx.right.value
      self.node_to_op[ctx] = self.id
      self.opExpression(ctx.operation, first, second)

    if isinstance(ctx.right, BinaryExpression) and isinstance(ctx.left, Integer_literal):
      first = ctx.left.value
      second = f'%op_{self.id - 1}'
      self.node_to_op[ctx] = self.id
      self.opExpression(ctx.operation, first, second)

    if isinstance(ctx.left, Function_call) and isinstance(ctx.right, Integer_literal):
      func_name = self.func_stack.pop()
      first = f'%func_{func_name}'
      second = ctx.right.value
      self.node_to_op[ctx] = self.id
      self.opExpression(ctx.operation, first, second)

    if isinstance(ctx.right, Function_call) and isinstance(ctx.left, Integer_literal):
      func_name = self.func_stack.pop()
      first = ctx.left.value
      second = f'%func_{func_name}'
      self.node_to_op[ctx] = self.id
      self.opExpression(ctx.operation, first, second)

    return ctx

  def astVisitMethod_call(self, ctx:Method_call):
    args = []

    for arg in ctx.arg_list:
      args.append(self.visit(arg))

    if ctx.object_name == 'console' and ctx.method_name == 'log':
      if self.check_stdout:
        self.global_scope += f'declare i32 @printf(i8*, ...)\n'
        self.check_stdout = False

      for arg in args:
        if isinstance(arg, Id):
          symbol = self.symtab[arg]
          name_var_load = self.symbol_to_var[symbol]
          self.buffer_scope += self.stdout(symbol.type, arg, name_var_load)
        if isinstance(arg, Integer_literal):
          self.buffer_scope += self.stdout('int', arg, '')
        if isinstance(arg, String_literal):
          self.buffer_scope += self.stdout('str', arg, '')

    if ctx.method_name == 'read_int':
      if self.check_stdin:
        self.global_scope += f'declare i32 @__isoc99_scanf(i8*, ...)\n'
        self.check_stdin = False

      self.exp_buffer += self.stdin('int')

    if ctx.method_name == 'read_str':
      if self.check_stdin:
        self.global_scope += f'declare i32 @__isoc99_scanf(i8*, ...)\n'
        self.check_stdin = False

      self.exp_buffer += self.stdin('str')

    return ctx 

  def astVisitFunction_declaration(self, ctx:Function_declaration):
    self.main_scope += self.buffer_scope
    self.buffer_scope = ''
    args = ''
    type_func = ''
    return_val = ''

    for arg in ctx.arg_list:
      args += f'i32 %arg_{arg.name}, '
      name_var = f'{arg.name}_{arg.token.line}{arg.token.column}'
      self.buffer_scope += f'  %{name_var} = alloca i32\n'
      self.buffer_scope += f'  store i32 %arg_{arg.name}, i32* %{name_var}\n\n'
      symbol = self.symtab[arg]
      self.symbol_to_var[symbol] = name_var
      
    args = args.rstrip(', ')

    for child in ctx.body:
      val = self.visit(child)
      if isinstance(val, str):
        type_func = val

    if type_func == '':
      type_func = 'i32'
      return_val = f'  ret i32 0\n'

    declr = f'define dso_local {type_func} @{ctx.name}({args}) {{\n{self.buffer_scope}{return_val}}}\n'
    self.buffer_scope = ''

    self.global_scope += declr

  def astVisitFunction_call(self, ctx:Function_call):
    args = ''
    call = f'  %func_{ctx.name}_{ctx.token.line}{ctx.token.column} = call i32 @{ctx.name}'
    self.func_stack.append(f'{ctx.name}_{ctx.token.line}{ctx.token.column}')

    for arg in ctx.arg_list:
      if isinstance(arg, BinaryExpression):
        arg = self.visit(arg)
        self.buffer_scope += self.exp_buffer
        self.exp_buffer = ''
        op = f'%op_{self.id - 1}'
        args += f'i32 {op},'
      if isinstance(arg, Id):
        arg = self.visit(arg)
        symbol = self.symtab[arg]
        name_var_load = self.symbol_to_var[symbol]
        load = f'  %arg_{name_var_load}_{self.id} = load i32, i32* %{name_var_load}\n'
        self.buffer_scope += load
        args += f'i32 %arg_{name_var_load}_{self.id}, '
        self.id += 1
      if isinstance(arg, Integer_literal):
        args += f'i32 {arg.value}, '

    args = args.rstrip(', ')
      
    call += f'({args})\n'
    self.buffer_scope += call

    return ctx

  def astVisitReturn_statement(self, ctx:Return_statement):
    return_val = self.visit(ctx.value)

    if isinstance(return_val, Id):
      symbol = self.symtab[return_val]
      left_var_load = self.symbol_to_var[symbol]
      if symbol.type == 'int':
        self.buffer_scope += f'  %tmp_{return_val.name} = load i32, i32* %{left_var_load}\n'
        self.buffer_scope += f'  ret i32 %tmp_{return_val.name}\n'
        return 'i32'
      # else:
      #   return 'i8*'
    if isinstance(return_val, Integer_literal):
      self.buffer_scope += f'  ret i32 {return_val.value}\n'
      return 'i32'
    # if isinstance(return_val, String_literal):
    #   string = return_val.value.split('"')[1]
    #   length = len(string) + 1
    #   self.global_scope += f'@.{string}_{self.id} = private unnamed_addr constant [{length} x i8] c"{string}\\00"\n'
    #   self.buffer_scope += f'  ret i8* getelementptr inbounds ([{length} x i8], [{length} x i8]* @.{string}_{self.id}, i64 0, i64 0)\n'
    #   return 'i8*'

  def astVisitFor_loop(self, ctx:For_loop): 
    self.visit(ctx.start)
    enter = f'  br label %mark_{self.id_mark}\n\n'
    condition = self.visit(ctx.condition)
    body = f'mark_{self.id_mark}:\n'
    self.id_mark += 1
    self.buffer_scope += (enter + condition + body)

    self.visit(ctx.step)

    for child in ctx.body:
      self.visit(child)

    exit = f'  br label %mark_{self.id_mark - 2}\n\n'
    next = f'mark_{self.id_mark}:\n'
    self.id_mark += 1
    self.buffer_scope += (exit + next)

  def astVisitWhile_loop(self, ctx:While_loop):
    enter = f'  br label %mark_{self.id_mark}\n\n'
    condition = self.visit(ctx.condition)
    body = f'mark_{self.id_mark}:\n'
    self.id_mark += 1
    self.buffer_scope += (enter + condition + body)

    for child in ctx.body:
      self.visit(child)

    exit = f'  br label %mark_{self.id_mark - 2}\n\n'
    next = f'mark_{self.id_mark}:\n'
    self.id_mark += 1
    self.buffer_scope += (exit + next)

  def astVisitInstruction_if(self, ctx:Instruction_if):
    enter = f'  br label %mark_{self.id_mark}\n\n'
    condition = self.visit(ctx.condition)
    body = f'mark_{self.id_mark}:\n'
    self.id_mark += 1
    self.buffer_scope += (enter + condition + body)

    for child in ctx.body:
      self.visit(child)

    if ctx.instuction_elseif != []:
      el = 0
      if ctx.instuction_else != '':
        el = 1
      length = len(ctx.instuction_elseif) * 2 + el
      exit = f'  br label %mark_{self.id_mark + length}\n\n'
    if ctx.instuction_else != '' and ctx.instuction_elseif == []:
      exit = f'  br label %mark_{self.id_mark + 1}\n\n'
    if ctx.instuction_elseif == [] and ctx.instuction_else == '':
      exit = f'  br label %mark_{self.id_mark}\n\n'

    self.buffer_scope += exit

    for child in ctx.instuction_elseif:
      self.visit(child)

    if ctx.instuction_else != '':
      self.visit(ctx.instuction_else)


    next = f'mark_{self.id_mark}:\n'
    self.id_mark += 1
    self.buffer_scope += next

  def astVisitInstruction_elseif(self, ctx:Instruction_elseif):
    condition = self.visit(ctx.condition)
    body = f'mark_{self.id_mark}:\n'
    self.id_mark += 1

    self.buffer_scope += (condition + body)

    for child in ctx.body:
      self.visit(child)

    exit = f'  br label %mark_{self.id_mark}\n\n'
    self.buffer_scope += exit

  def astVisitInstruction_else(self, ctx:Instruction_else):
    body = f'mark_{self.id_mark}:\n'
    self.id_mark += 1
    self.buffer_scope += body

    for child in ctx.body:
      self.visit(child)

    exit = f'  br label %mark_{self.id_mark}\n\n'
    self.buffer_scope += exit

  def astVisitCondition(self, ctx:Condition):
    mark = f'mark_{self.id_mark}:\n'
    self.id_mark += 1

    if isinstance(ctx.left_argument, Id):
      symbol = self.symtab[ctx.left_argument]
      name_var_load = self.symbol_to_var[symbol]
      first = f'%tmp_{name_var_load}_{self.id}'
      load = f'  {first} = load i32, i32* %{name_var_load}\n'
      mark += load
      self.id += 1
    if isinstance(ctx.left_argument, BinaryExpression):
      self.visit(ctx.left_argument)
      first = f'%op_{self.id - 1}'
      mark += self.exp_buffer
      self.exp_buffer = ''

    if isinstance(ctx.right_argument, Id):
      symbol = self.symtab[ctx.right_argument]
      name_var_load = self.symbol_to_var[symbol]
      second = f'%tmp_{name_var_load}_{self.id}'
      self.id += 1

      load = f'  {second} = load i32, i32* %{name_var_load}\n'
      mark += load
      operation = self.opCondition(ctx.operation, first, second)
      mark += operation

    if isinstance(ctx.right_argument, Integer_literal):
      second = f'{ctx.right_argument.value}'
      print(second)
      operation = self.opCondition(ctx.operation, first, second)
      mark += operation
    
    if isinstance(ctx.right_argument, BinaryExpression):
      self.visit(ctx.right_argument)
      second = f'%op_{self.id - 1}'
      operation = self.opCondition(ctx.operation, first, second)
      mark += (self.exp_buffer + operation)
      self.exp_buffer = ''

    mark += f'  br i1 %op_{self.id - 1}, label %mark_{self.id_mark}, label %mark_{self.id_mark + 1}\n\n'
    return mark

  def astVisitId(self, ctx:Id): 
    return ctx

  def astVisitArray_element(self, ctx:Array_element):
    self.visit(ctx.name)
    if isinstance(ctx.body, Expression):
      self.visit(ctx.body)

  def astVisitStatement(self, ctx:Statement): 
    return self.visit(ctx.statement)

  def astVisitorArray(self, ctx:Array):
    return ctx.type

  def astVisitorInteger_literal(self, ctx:Integer_literal): 
    return ctx

  def astVisitorString_literal(self, ctx:String_literal):
    return ctx
  
  def astVisitObject_property(self, ctx:Object_property):
    pass