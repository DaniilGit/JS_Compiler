lexer grammar JSLexer;

CONST: 'console' | 'let' | 'for' | 'while' | 'if' | 'else' | 'log' | 'const'; 
STRING: '"' ~ ["\n\r]* '"';
ID: [_$a-zA-Z]+ [0-9] ?;
INT: [0-9]+;
OP: ([;()+=-{}.<>]) | '<=' | '>=' | '!=' | '++' | '--' | '+='; 
COM: ('//' ~ ["\n\r]*) | ('/* ' ~ [" \n\r\t]* ' */'); 

WS: [ \n\t\r]+ -> skip;