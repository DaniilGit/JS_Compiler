grammar JS;

program
  : function_declaration* statement*
  ;

function_declaration
  : FUNCTION ID L_ROUND (ID COMMA?)* R_ROUND L_FIGURE statement+ R_FIGURE
  ;

statement
  : function_call
  | method_call
  | declaration
  | assign
  | expression
  | return_statement
  | for_loop
  | while_loop
  | instruction_if
  ;

function_call
  : ID L_ROUND ((argument) COMMA?)* R_ROUND SEMI?
  ;

method_call
  : ID DOT ID L_ROUND ((argument) COMMA?)* R_ROUND SEMI?
  ;

declaration
  : (LET|VAR|CONST) ID SEMI?
  | (LET|VAR|CONST) ID ASSIGN argument SEMI?
  | (LET|VAR|CONST) ID ASSIGN expression SEMI?
  | (LET|VAR|CONST) ID ASSIGN L_SQUARE ((array_value COMMA?)*) R_SQUARE SEMI?
  ;

assign
  : (ID|array_element) (ASSIGN|PLUS_ASSIGN|MINUS_ASSIGN|MULTI_ASSIGN|DIV_ASSIGN|REM_ASSIGN) (argument|expression|(L_SQUARE ((array_value COMMA?)*) R_SQUARE)) SEMI?
  ;

expression
  : expression (operation expression)+
  | argument (operation argument)+
  | ID (INCREMENT|DECREMENT)
  ;

return_statement
  : RETURN argument SEMI?
  ;

for_loop
  : FOR L_ROUND for_start SEMI condition SEMI for_step R_ROUND L_FIGURE statement+ R_FIGURE
  | FOR L_ROUND for_start SEMI condition SEMI for_step R_ROUND statement
  ;

while_loop
  : WHILE L_ROUND condition R_ROUND L_FIGURE statement+ R_FIGURE
  | WHILE L_ROUND condition R_ROUND statement
  ;

instruction_if
  : IF L_ROUND condition R_ROUND L_FIGURE statement+ R_FIGURE instruction_elseif* instruction_else?
  | IF L_ROUND condition R_ROUND statement instruction_elseif* instruction_else?
  ;

instruction_elseif
  : ELSE IF L_ROUND condition R_ROUND L_FIGURE statement+ R_FIGURE
  | ELSE IF L_ROUND condition R_ROUND statement
  ;

instruction_else
  : ELSE L_FIGURE statement+ R_FIGURE
  | ELSE statement
  ;

for_start
  : assign|declaration
  ;

condition
  : (argument|expression) (LESS|GREATER|LESS_EQUAL|GREATER_EQUAL|NOT_EQUAL|EQUAL) (argument|expression)
  ;

for_step
  : expression
  ;

argument
  : ID|INT|STRING|TRUE|FALSE|array_element|object_property|method_call
  ;

array_element
  : ID L_SQUARE (ID|INT|expression) R_SQUARE
  ;

object_property
  : ID DOT ID
  ;

array_value
  : INT|STRING
  ;

operation
  : PLUS|MINUS|MULTI|DIV|REM
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
TERNAR: '?'|':';
DECREMENT: '--';
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