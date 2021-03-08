// Generated from /home/daniil/compiler-DaniilGit/src/grammar/JSLexer.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class JSLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CONST=1, STRING=2, ID=3, INT=4, OP=5, COM=6, WS=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"CONST", "STRING", "ID", "INT", "OP", "COM", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CONST", "STRING", "ID", "INT", "OP", "COM", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public JSLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "JSLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\tw\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\2\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3"+
		"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\62\n\2\3\3\3\3\7\3\66\n\3\f\3\16"+
		"\39\13\3\3\3\3\3\3\4\6\4>\n\4\r\4\16\4?\3\4\5\4C\n\4\3\5\6\5F\n\5\r\5"+
		"\16\5G\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6W\n\6\3"+
		"\7\3\7\3\7\3\7\7\7]\n\7\f\7\16\7`\13\7\3\7\3\7\3\7\3\7\3\7\7\7g\n\7\f"+
		"\7\16\7j\13\7\3\7\3\7\3\7\5\7o\n\7\3\b\6\br\n\b\r\b\16\bs\3\b\3\b\2\2"+
		"\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\b\5\2\f\f\17\17$$\6\2&&C\\aac|\3"+
		"\2\62;\7\2*+--\60\60=}\177\177\6\2\13\f\17\17\"\"$$\5\2\13\f\17\17\"\""+
		"\2\u008b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2"+
		"\2\r\3\2\2\2\2\17\3\2\2\2\3\61\3\2\2\2\5\63\3\2\2\2\7=\3\2\2\2\tE\3\2"+
		"\2\2\13V\3\2\2\2\rn\3\2\2\2\17q\3\2\2\2\21\22\7e\2\2\22\23\7q\2\2\23\24"+
		"\7p\2\2\24\25\7u\2\2\25\26\7q\2\2\26\27\7n\2\2\27\62\7g\2\2\30\31\7n\2"+
		"\2\31\32\7g\2\2\32\62\7v\2\2\33\34\7h\2\2\34\35\7q\2\2\35\62\7t\2\2\36"+
		"\37\7y\2\2\37 \7j\2\2 !\7k\2\2!\"\7n\2\2\"\62\7g\2\2#$\7k\2\2$\62\7h\2"+
		"\2%&\7g\2\2&\'\7n\2\2\'(\7u\2\2(\62\7g\2\2)*\7n\2\2*+\7q\2\2+\62\7i\2"+
		"\2,-\7e\2\2-.\7q\2\2./\7p\2\2/\60\7u\2\2\60\62\7v\2\2\61\21\3\2\2\2\61"+
		"\30\3\2\2\2\61\33\3\2\2\2\61\36\3\2\2\2\61#\3\2\2\2\61%\3\2\2\2\61)\3"+
		"\2\2\2\61,\3\2\2\2\62\4\3\2\2\2\63\67\7$\2\2\64\66\n\2\2\2\65\64\3\2\2"+
		"\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29\67\3\2\2\2:;\7$\2"+
		"\2;\6\3\2\2\2<>\t\3\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3\2"+
		"\2\2AC\t\4\2\2BA\3\2\2\2BC\3\2\2\2C\b\3\2\2\2DF\t\4\2\2ED\3\2\2\2FG\3"+
		"\2\2\2GE\3\2\2\2GH\3\2\2\2H\n\3\2\2\2IW\t\5\2\2JK\7>\2\2KW\7?\2\2LM\7"+
		"@\2\2MW\7?\2\2NO\7#\2\2OW\7?\2\2PQ\7-\2\2QW\7-\2\2RS\7/\2\2SW\7/\2\2T"+
		"U\7-\2\2UW\7?\2\2VI\3\2\2\2VJ\3\2\2\2VL\3\2\2\2VN\3\2\2\2VP\3\2\2\2VR"+
		"\3\2\2\2VT\3\2\2\2W\f\3\2\2\2XY\7\61\2\2YZ\7\61\2\2Z^\3\2\2\2[]\n\2\2"+
		"\2\\[\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_\3\2\2\2_o\3\2\2\2`^\3\2\2\2ab\7\61"+
		"\2\2bc\7,\2\2cd\7\"\2\2dh\3\2\2\2eg\n\6\2\2fe\3\2\2\2gj\3\2\2\2hf\3\2"+
		"\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2\2\2kl\7\"\2\2lm\7,\2\2mo\7\61\2\2nX\3\2"+
		"\2\2na\3\2\2\2o\16\3\2\2\2pr\t\7\2\2qp\3\2\2\2rs\3\2\2\2sq\3\2\2\2st\3"+
		"\2\2\2tu\3\2\2\2uv\b\b\2\2v\20\3\2\2\2\r\2\61\67?BGV^hns\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}