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


    # Visit a parse tree produced by JSParser#call_function.
    def visitCall_function(self, ctx:JSParser.Call_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#function.
    def visitFunction(self, ctx:JSParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JSParser#string.
    def visitString(self, ctx:JSParser.StringContext):
        return self.visitChildren(ctx)



del JSParser