# Generated from JSLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\2\3\2\3")
        buf.write("\3\6\3\34\n\3\r\3\16\3\35\3\3\5\3!\n\3\3\4\6\4$\n\4\r")
        buf.write("\4\16\4%\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\5\5\66\n\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7>\n\7")
        buf.write("\f\7\16\7A\13\7\3\7\3\7\3\7\3\7\3\7\7\7H\n\7\f\7\16\7")
        buf.write("K\13\7\3\7\3\7\3\7\5\7P\n\7\3\b\6\bS\n\b\r\b\16\bT\3\b")
        buf.write("\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\b\5\2\f\f")
        buf.write("\17\17$$\6\2&&C\\aac|\3\2\62;\7\2*+--==?}\177\177\6\2")
        buf.write("\13\f\17\17\"\"$$\5\2\13\f\17\17\"\"\2`\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5\33\3\2\2\2\7#\3\2\2")
        buf.write("\2\t\65\3\2\2\2\13\67\3\2\2\2\rO\3\2\2\2\17R\3\2\2\2\21")
        buf.write("\25\7$\2\2\22\24\n\2\2\2\23\22\3\2\2\2\24\27\3\2\2\2\25")
        buf.write("\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2")
        buf.write("\30\31\7$\2\2\31\4\3\2\2\2\32\34\t\3\2\2\33\32\3\2\2\2")
        buf.write("\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2")
        buf.write("\37!\t\4\2\2 \37\3\2\2\2 !\3\2\2\2!\6\3\2\2\2\"$\t\4\2")
        buf.write("\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\b\3\2\2\2")
        buf.write("\'(\7e\2\2()\7q\2\2)*\7p\2\2*+\7u\2\2+,\7q\2\2,-\7n\2")
        buf.write("\2-.\7g\2\2./\7\60\2\2/\60\7n\2\2\60\61\7q\2\2\61\66\7")
        buf.write("i\2\2\62\63\7n\2\2\63\64\7g\2\2\64\66\7v\2\2\65\'\3\2")
        buf.write("\2\2\65\62\3\2\2\2\66\n\3\2\2\2\678\t\5\2\28\f\3\2\2\2")
        buf.write("9:\7\61\2\2:;\7\61\2\2;?\3\2\2\2<>\n\2\2\2=<\3\2\2\2>")
        buf.write("A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@P\3\2\2\2A?\3\2\2\2BC\7")
        buf.write("\61\2\2CD\7,\2\2DE\7\"\2\2EI\3\2\2\2FH\n\6\2\2GF\3\2\2")
        buf.write("\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JL\3\2\2\2KI\3\2\2\2L")
        buf.write("M\7\"\2\2MN\7,\2\2NP\7\61\2\2O9\3\2\2\2OB\3\2\2\2P\16")
        buf.write("\3\2\2\2QS\t\7\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2")
        buf.write("\2\2UV\3\2\2\2VW\b\b\2\2W\20\3\2\2\2\f\2\25\35 %\65?I")
        buf.write("OT\3\b\2\2")
        return buf.getvalue()


class JSLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRING = 1
    ID = 2
    INT = 3
    CONST = 4
    OP = 5
    COM = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "STRING", "ID", "INT", "CONST", "OP", "COM", "WS" ]

    ruleNames = [ "STRING", "ID", "INT", "CONST", "OP", "COM", "WS" ]

    grammarFileName = "JSLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


