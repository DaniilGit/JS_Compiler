grammar JS;

program
  : function call_function
  ;

call_function
  : ID L_ROUND R_ROUND SEMI
  ;

function
  : FUNCTION ID L_ROUND R_ROUND L_FIGURE ID DOT ID L_ROUND string R_ROUND SEMI R_FIGURE
  ;

string
  : STRING
  ;

CONST: 'const';
LET: 'let';
VAR: 'var';
FOR: 'for';
WHILE: 'while';
DO: 'do';
RETURN: 'return';
FUNCTION: 'function';
IF: 'if';
ELSE: 'else';
TRUE: 'true';
FALSE: 'false';
STRING: '"' ~ ["\n\r]* '"';
ID: ([a-zA-Z_$])([0-9a-zA-Z])*;
INT: '0' | [1-9][0-9]*;
L_ROUND: '(';
R_ROUND: ')';
L_FIGURE: '{';
R_FIGURE: '}';
L_SQUARE: '[';
R_SQUARE: ']';
PLUS: '+';
MINUS: '-';
ASSIGN: '=';
MULTI: '*';
DIV: '/';
REM: '%';
DOT: '.';
COMMA: ',';
SEMI: ';';
LESS: '<';
GREATER: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
NOT_EQUAL: '!=';
EQUAL: '==';
INCREMENT: '++';
DECREMENT: '--';
TERNAR: '?' | ':';
LOG_AND: '&&';
LOG_OR: '||';
LOG_NOT: '!';
BIT_OR: '|';
BIT_AND: '&';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MULTI_ASSIGN: '*=';
DIV_ASSIGN: '/=';
REM_ASSIGN: '%=';
COM: ('//' ~ ["\n\r]*) | ('/* ' ~ ["\n\r\t]*  '*/'); 

WS: [ \n\t\r]+ -> skip;