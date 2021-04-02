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



del JSParser