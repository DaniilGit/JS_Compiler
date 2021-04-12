# Generated from JS.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSParser import JSParser
else:
    from JSParser import JSParser

# This class defines a complete listener for a parse tree produced by JSParser.
class JSListener(ParseTreeListener):

    # Enter a parse tree produced by JSParser#program.
    def enterProgram(self, ctx:JSParser.ProgramContext):
        pass

    # Exit a parse tree produced by JSParser#program.
    def exitProgram(self, ctx:JSParser.ProgramContext):
        pass


    # Enter a parse tree produced by JSParser#function_declaration.
    def enterFunction_declaration(self, ctx:JSParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by JSParser#function_declaration.
    def exitFunction_declaration(self, ctx:JSParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by JSParser#statement.
    def enterStatement(self, ctx:JSParser.StatementContext):
        pass

    # Exit a parse tree produced by JSParser#statement.
    def exitStatement(self, ctx:JSParser.StatementContext):
        pass


    # Enter a parse tree produced by JSParser#function_call.
    def enterFunction_call(self, ctx:JSParser.Function_callContext):
        pass

    # Exit a parse tree produced by JSParser#function_call.
    def exitFunction_call(self, ctx:JSParser.Function_callContext):
        pass


    # Enter a parse tree produced by JSParser#method_call.
    def enterMethod_call(self, ctx:JSParser.Method_callContext):
        pass

    # Exit a parse tree produced by JSParser#method_call.
    def exitMethod_call(self, ctx:JSParser.Method_callContext):
        pass


    # Enter a parse tree produced by JSParser#declaration.
    def enterDeclaration(self, ctx:JSParser.DeclarationContext):
        pass

    # Exit a parse tree produced by JSParser#declaration.
    def exitDeclaration(self, ctx:JSParser.DeclarationContext):
        pass


    # Enter a parse tree produced by JSParser#assign.
    def enterAssign(self, ctx:JSParser.AssignContext):
        pass

    # Exit a parse tree produced by JSParser#assign.
    def exitAssign(self, ctx:JSParser.AssignContext):
        pass


    # Enter a parse tree produced by JSParser#expression.
    def enterExpression(self, ctx:JSParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JSParser#expression.
    def exitExpression(self, ctx:JSParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JSParser#return_statement.
    def enterReturn_statement(self, ctx:JSParser.Return_statementContext):
        pass

    # Exit a parse tree produced by JSParser#return_statement.
    def exitReturn_statement(self, ctx:JSParser.Return_statementContext):
        pass


    # Enter a parse tree produced by JSParser#for_loop.
    def enterFor_loop(self, ctx:JSParser.For_loopContext):
        pass

    # Exit a parse tree produced by JSParser#for_loop.
    def exitFor_loop(self, ctx:JSParser.For_loopContext):
        pass


    # Enter a parse tree produced by JSParser#while_loop.
    def enterWhile_loop(self, ctx:JSParser.While_loopContext):
        pass

    # Exit a parse tree produced by JSParser#while_loop.
    def exitWhile_loop(self, ctx:JSParser.While_loopContext):
        pass


    # Enter a parse tree produced by JSParser#instruction_if.
    def enterInstruction_if(self, ctx:JSParser.Instruction_ifContext):
        pass

    # Exit a parse tree produced by JSParser#instruction_if.
    def exitInstruction_if(self, ctx:JSParser.Instruction_ifContext):
        pass


    # Enter a parse tree produced by JSParser#instruction_elseif.
    def enterInstruction_elseif(self, ctx:JSParser.Instruction_elseifContext):
        pass

    # Exit a parse tree produced by JSParser#instruction_elseif.
    def exitInstruction_elseif(self, ctx:JSParser.Instruction_elseifContext):
        pass


    # Enter a parse tree produced by JSParser#instruction_else.
    def enterInstruction_else(self, ctx:JSParser.Instruction_elseContext):
        pass

    # Exit a parse tree produced by JSParser#instruction_else.
    def exitInstruction_else(self, ctx:JSParser.Instruction_elseContext):
        pass


    # Enter a parse tree produced by JSParser#for_start.
    def enterFor_start(self, ctx:JSParser.For_startContext):
        pass

    # Exit a parse tree produced by JSParser#for_start.
    def exitFor_start(self, ctx:JSParser.For_startContext):
        pass


    # Enter a parse tree produced by JSParser#condition.
    def enterCondition(self, ctx:JSParser.ConditionContext):
        pass

    # Exit a parse tree produced by JSParser#condition.
    def exitCondition(self, ctx:JSParser.ConditionContext):
        pass


    # Enter a parse tree produced by JSParser#for_step.
    def enterFor_step(self, ctx:JSParser.For_stepContext):
        pass

    # Exit a parse tree produced by JSParser#for_step.
    def exitFor_step(self, ctx:JSParser.For_stepContext):
        pass


    # Enter a parse tree produced by JSParser#argument.
    def enterArgument(self, ctx:JSParser.ArgumentContext):
        pass

    # Exit a parse tree produced by JSParser#argument.
    def exitArgument(self, ctx:JSParser.ArgumentContext):
        pass


    # Enter a parse tree produced by JSParser#array_element.
    def enterArray_element(self, ctx:JSParser.Array_elementContext):
        pass

    # Exit a parse tree produced by JSParser#array_element.
    def exitArray_element(self, ctx:JSParser.Array_elementContext):
        pass


    # Enter a parse tree produced by JSParser#object_property.
    def enterObject_property(self, ctx:JSParser.Object_propertyContext):
        pass

    # Exit a parse tree produced by JSParser#object_property.
    def exitObject_property(self, ctx:JSParser.Object_propertyContext):
        pass


    # Enter a parse tree produced by JSParser#array_value.
    def enterArray_value(self, ctx:JSParser.Array_valueContext):
        pass

    # Exit a parse tree produced by JSParser#array_value.
    def exitArray_value(self, ctx:JSParser.Array_valueContext):
        pass


