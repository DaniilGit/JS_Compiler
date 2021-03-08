lexer grammar JSLexer;

CONST: 'console' | 'let' | 'for' | 'while' | 'if' | 'else' | 'log' | 'const'; 
STRING: '"' ~ ["\n\r]* '"';
ID: ([a-z]|[A-Z]|[_$])(([0-9]|[a-z]|[A-Z])+)? ;
INT: [0-9]+;
OP: ([;()+=-{}.<>]) | '<=' | '>=' | '!=' | '++' | '--' | '+='; 
COM: ('//' ~ ["\n\r]*) | ('/* ' ~ ["\n\r\t]*  '*/'); 

WS: [ \n\t\r]+ -> skip;