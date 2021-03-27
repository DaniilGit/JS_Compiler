import sys
import argparse
from build_antlr.JSParser import JSParser
from antlr4 import *

class JSVisitor(ParseTreeVisitor):
  def visitProgram(self, ctx:JSParser.ProgramContext):
    return self.visitChildren(ctx)

  def visitCall_function(self, ctx:JSParser.Call_functionContext):
    print(ctx.getRuleIndex)
    return self.visitChildren(ctx)

  def visitFunction(self, ctx:JSParser.FunctionContext):
    print(ctx.getRuleIndex)
    return self.visitChildren(ctx)
      
  def visitString(self, ctx:JSParser.StringContext):
    print(JSParser.StringContext.STRING)
    print(ctx.getText)
    return self.visitChildren(ctx)