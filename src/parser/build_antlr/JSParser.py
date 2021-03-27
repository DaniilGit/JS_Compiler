# Generated from JS.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("#\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\36\2\n")
        buf.write("\3\2\2\2\4\r\3\2\2\2\6\22\3\2\2\2\b \3\2\2\2\n\13\5\6")
        buf.write("\4\2\13\f\5\4\3\2\f\3\3\2\2\2\r\16\7\20\2\2\16\17\7\22")
        buf.write("\2\2\17\20\7\23\2\2\20\21\7 \2\2\21\5\3\2\2\2\22\23\7")
        buf.write("\n\2\2\23\24\7\20\2\2\24\25\7\22\2\2\25\26\7\23\2\2\26")
        buf.write("\27\7\24\2\2\27\30\7\20\2\2\30\31\7\36\2\2\31\32\7\20")
        buf.write("\2\2\32\33\7\22\2\2\33\34\5\b\5\2\34\35\7\23\2\2\35\36")
        buf.write("\7 \2\2\36\37\7\25\2\2\37\7\3\2\2\2 !\7\17\2\2!\t\3\2")
        buf.write("\2\2\2")
        return buf.getvalue()


class JSParser ( Parser ):

    grammarFileName = "JS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'const'", "'let'", "'var'", "'for'", 
                     "'while'", "'do'", "'return'", "'function'", "'if'", 
                     "'else'", "'true'", "'false'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "'+'", "'-'", "'='", "'*'", "'/'", "'%'", "'.'", "','", 
                     "';'", "'<'", "'>'", "'<='", "'>='", "'!='", "'=='", 
                     "'++'", "'--'", "<INVALID>", "'&&'", "'||'", "'!'", 
                     "'|'", "'&'", "'+='", "'-='", "'*='", "'/='", "'%='" ]

    symbolicNames = [ "<INVALID>", "CONST", "LET", "VAR", "FOR", "WHILE", 
                      "DO", "RETURN", "FUNCTION", "IF", "ELSE", "TRUE", 
                      "FALSE", "STRING", "ID", "INT", "L_ROUND", "R_ROUND", 
                      "L_FIGURE", "R_FIGURE", "L_SQUARE", "R_SQUARE", "PLUS", 
                      "MINUS", "ASSIGN", "MULTI", "DIV", "REM", "DOT", "COMMA", 
                      "SEMI", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", 
                      "NOT_EQUAL", "EQUAL", "INCREMENT", "DECREMENT", "TERNAR", 
                      "LOG_AND", "LOG_OR", "LOG_NOT", "BIT_OR", "BIT_AND", 
                      "PLUS_ASSIGN", "MINUS_ASSIGN", "MULTI_ASSIGN", "DIV_ASSIGN", 
                      "REM_ASSIGN", "COM", "WS" ]

    RULE_program = 0
    RULE_call_function = 1
    RULE_function = 2
    RULE_string = 3

    ruleNames =  [ "program", "call_function", "function", "string" ]

    EOF = Token.EOF
    CONST=1
    LET=2
    VAR=3
    FOR=4
    WHILE=5
    DO=6
    RETURN=7
    FUNCTION=8
    IF=9
    ELSE=10
    TRUE=11
    FALSE=12
    STRING=13
    ID=14
    INT=15
    L_ROUND=16
    R_ROUND=17
    L_FIGURE=18
    R_FIGURE=19
    L_SQUARE=20
    R_SQUARE=21
    PLUS=22
    MINUS=23
    ASSIGN=24
    MULTI=25
    DIV=26
    REM=27
    DOT=28
    COMMA=29
    SEMI=30
    LESS=31
    GREATER=32
    LESS_EQUAL=33
    GREATER_EQUAL=34
    NOT_EQUAL=35
    EQUAL=36
    INCREMENT=37
    DECREMENT=38
    TERNAR=39
    LOG_AND=40
    LOG_OR=41
    LOG_NOT=42
    BIT_OR=43
    BIT_AND=44
    PLUS_ASSIGN=45
    MINUS_ASSIGN=46
    MULTI_ASSIGN=47
    DIV_ASSIGN=48
    REM_ASSIGN=49
    COM=50
    WS=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(JSParser.FunctionContext,0)


        def call_function(self):
            return self.getTypedRuleContext(JSParser.Call_functionContext,0)


        def getRuleIndex(self):
            return JSParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = JSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.function()
            self.state = 9
            self.call_function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JSParser.ID, 0)

        def L_ROUND(self):
            return self.getToken(JSParser.L_ROUND, 0)

        def R_ROUND(self):
            return self.getToken(JSParser.R_ROUND, 0)

        def SEMI(self):
            return self.getToken(JSParser.SEMI, 0)

        def getRuleIndex(self):
            return JSParser.RULE_call_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_function" ):
                return visitor.visitCall_function(self)
            else:
                return visitor.visitChildren(self)




    def call_function(self):

        localctx = JSParser.Call_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_call_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(JSParser.ID)
            self.state = 12
            self.match(JSParser.L_ROUND)
            self.state = 13
            self.match(JSParser.R_ROUND)
            self.state = 14
            self.match(JSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(JSParser.FUNCTION, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(JSParser.ID)
            else:
                return self.getToken(JSParser.ID, i)

        def L_ROUND(self, i:int=None):
            if i is None:
                return self.getTokens(JSParser.L_ROUND)
            else:
                return self.getToken(JSParser.L_ROUND, i)

        def R_ROUND(self, i:int=None):
            if i is None:
                return self.getTokens(JSParser.R_ROUND)
            else:
                return self.getToken(JSParser.R_ROUND, i)

        def L_FIGURE(self):
            return self.getToken(JSParser.L_FIGURE, 0)

        def DOT(self):
            return self.getToken(JSParser.DOT, 0)

        def string(self):
            return self.getTypedRuleContext(JSParser.StringContext,0)


        def SEMI(self):
            return self.getToken(JSParser.SEMI, 0)

        def R_FIGURE(self):
            return self.getToken(JSParser.R_FIGURE, 0)

        def getRuleIndex(self):
            return JSParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = JSParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(JSParser.FUNCTION)
            self.state = 17
            self.match(JSParser.ID)
            self.state = 18
            self.match(JSParser.L_ROUND)
            self.state = 19
            self.match(JSParser.R_ROUND)
            self.state = 20
            self.match(JSParser.L_FIGURE)
            self.state = 21
            self.match(JSParser.ID)
            self.state = 22
            self.match(JSParser.DOT)
            self.state = 23
            self.match(JSParser.ID)
            self.state = 24
            self.match(JSParser.L_ROUND)
            self.state = 25
            self.string()
            self.state = 26
            self.match(JSParser.R_ROUND)
            self.state = 27
            self.match(JSParser.SEMI)
            self.state = 28
            self.match(JSParser.R_FIGURE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(JSParser.STRING, 0)

        def getRuleIndex(self):
            return JSParser.RULE_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = JSParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(JSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





