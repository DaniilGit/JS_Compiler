grammar JS;

program
  : function_declaration* statement*
  ;

function_declaration
  : FUNCTION ID L_ROUND R_ROUND L_FIGURE statement+ R_FIGURE
  ;

statement
  : function_call
  | method_call
  ;

function_call
  : ID L_ROUND R_ROUND SEMI
  ;

method_call
  : ID DOT ID L_ROUND STRING R_ROUND SEMI
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