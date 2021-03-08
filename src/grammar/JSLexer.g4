lexer grammar JSLexer;

STRING: '"' ~ ["\n\r]* '"';
ID: [_$a-zA-Z] + [0-9] ?;
INT: [0-9]+;
CONST: 'console.log' | 'let'; 
OP: [;()+=-{}]; 
COM: ('//' ~ ["\n\r]*) | ('/* ' ~ [" \n\r\t]* ' */'); 

WS: [ \n\t\r]+ -> skip;