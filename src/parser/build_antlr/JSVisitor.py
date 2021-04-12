# Generated from JS.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JSParser import JSParser
else:
    from JSParser import JSParser

# This class defines a complete generic visitor for a parse tree produced by JSParser.

class JSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JSParser#program.
    def visitProgram(self, ctx:JSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#function_declaration.
    def visitFunction_declaration(self, ctx:JSParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#statement.
    def visitStatement(self, ctx:JSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#function_call.
    def visitFunction_call(self, ctx:JSParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#method_call.
    def visitMethod_call(self, ctx:JSParser.Method_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#declaration.
    def visitDeclaration(self, ctx:JSParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#assign.
    def visitAssign(self, ctx:JSParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#expression.
    def visitExpression(self, ctx:JSParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#return_statement.
    def visitReturn_statement(self, ctx:JSParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#for_loop.
    def visitFor_loop(self, ctx:JSParser.For_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#while_loop.
    def visitWhile_loop(self, ctx:JSParser.While_loopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#instruction_if.
    def visitInstruction_if(self, ctx:JSParser.Instruction_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#instruction_elseif.
    def visitInstruction_elseif(self, ctx:JSParser.Instruction_elseifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#instruction_else.
    def visitInstruction_else(self, ctx:JSParser.Instruction_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#for_start.
    def visitFor_start(self, ctx:JSParser.For_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#condition.
    def visitCondition(self, ctx:JSParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#for_step.
    def visitFor_step(self, ctx:JSParser.For_stepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#argument.
    def visitArgument(self, ctx:JSParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#array_element.
    def visitArray_element(self, ctx:JSParser.Array_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#object_property.
    def visitObject_property(self, ctx:JSParser.Object_propertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#array_value.
    def visitArray_value(self, ctx:JSParser.Array_valueContext):
        return self.visitChildren(ctx)



del JSParser