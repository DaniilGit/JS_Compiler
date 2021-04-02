# Generated from JS.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\66\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16")
        buf.write("\n\2\f\2\16\2\21\13\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\6\3\37\n\3\r\3\16\3 \3\3\3\3")
        buf.write("\3\4\3\4\5\4\'\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2\64\2\17\3\2")
        buf.write("\2\2\4\30\3\2\2\2\6&\3\2\2\2\b(\3\2\2\2\n-\3\2\2\2\f\16")
        buf.write("\5\4\3\2\r\f\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20")
        buf.write("\3\2\2\2\20\25\3\2\2\2\21\17\3\2\2\2\22\24\5\6\4\2\23")
        buf.write("\22\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\3\3\2\2\2\27\25\3\2\2\2\30\31\7\n\2\2\31\32\7\20\2")
        buf.write("\2\32\33\7\22\2\2\33\34\7\23\2\2\34\36\7\24\2\2\35\37")
        buf.write("\5\6\4\2\36\35\3\2\2\2\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2")
        buf.write("\2!\"\3\2\2\2\"#\7\25\2\2#\5\3\2\2\2$\'\5\b\5\2%\'\5\n")
        buf.write("\6\2&$\3\2\2\2&%\3\2\2\2\'\7\3\2\2\2()\7\20\2\2)*\7\22")
        buf.write("\2\2*+\7\23\2\2+,\7 \2\2,\t\3\2\2\2-.\7\20\2\2./\7\36")
        buf.write("\2\2/\60\7\20\2\2\60\61\7\22\2\2\61\62\7\17\2\2\62\63")
        buf.write("\7\23\2\2\63\64\7 \2\2\64\13\3\2\2\2\6\17\25 &")
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
    RULE_function_declaration = 1
    RULE_statement = 2
    RULE_function_call = 3
    RULE_method_call = 4

    ruleNames =  [ "program", "function_declaration", "statement", "function_call", 
                   "method_call" ]

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

        def function_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSParser.Function_declarationContext)
            else:
                return self.getTypedRuleContext(JSParser.Function_declarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSParser.StatementContext)
            else:
                return self.getTypedRuleContext(JSParser.StatementContext,i)


        def getRuleIndex(self):
            return JSParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = JSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSParser.FUNCTION:
                self.state = 10
                self.function_declaration()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==JSParser.ID:
                self.state = 16
                self.statement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(JSParser.FUNCTION, 0)

        def ID(self):
            return self.getToken(JSParser.ID, 0)

        def L_ROUND(self):
            return self.getToken(JSParser.L_ROUND, 0)

        def R_ROUND(self):
            return self.getToken(JSParser.R_ROUND, 0)

        def L_FIGURE(self):
            return self.getToken(JSParser.L_FIGURE, 0)

        def R_FIGURE(self):
            return self.getToken(JSParser.R_FIGURE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JSParser.StatementContext)
            else:
                return self.getTypedRuleContext(JSParser.StatementContext,i)


        def getRuleIndex(self):
            return JSParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = JSParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(JSParser.FUNCTION)
            self.state = 23
            self.match(JSParser.ID)
            self.state = 24
            self.match(JSParser.L_ROUND)
            self.state = 25
            self.match(JSParser.R_ROUND)
            self.state = 26
            self.match(JSParser.L_FIGURE)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.statement()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JSParser.ID):
                    break

            self.state = 32
            self.match(JSParser.R_FIGURE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(JSParser.Function_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(JSParser.Method_callContext,0)


        def getRuleIndex(self):
            return JSParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = JSParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_callContext(ParserRuleContext):

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
            return JSParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = JSParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(JSParser.ID)
            self.state = 39
            self.match(JSParser.L_ROUND)
            self.state = 40
            self.match(JSParser.R_ROUND)
            self.state = 41
            self.match(JSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Method_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(JSParser.ID)
            else:
                return self.getToken(JSParser.ID, i)

        def DOT(self):
            return self.getToken(JSParser.DOT, 0)

        def L_ROUND(self):
            return self.getToken(JSParser.L_ROUND, 0)

        def STRING(self):
            return self.getToken(JSParser.STRING, 0)

        def R_ROUND(self):
            return self.getToken(JSParser.R_ROUND, 0)

        def SEMI(self):
            return self.getToken(JSParser.SEMI, 0)

        def getRuleIndex(self):
            return JSParser.RULE_method_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethod_call" ):
                listener.enterMethod_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethod_call" ):
                listener.exitMethod_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = JSParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(JSParser.ID)
            self.state = 44
            self.match(JSParser.DOT)
            self.state = 45
            self.match(JSParser.ID)
            self.state = 46
            self.match(JSParser.L_ROUND)
            self.state = 47
            self.match(JSParser.STRING)
            self.state = 48
            self.match(JSParser.R_ROUND)
            self.state = 49
            self.match(JSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





