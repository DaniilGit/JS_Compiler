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


