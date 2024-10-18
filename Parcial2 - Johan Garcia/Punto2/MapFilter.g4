grammar MapFilter;

// Parser rules
program: statement+ EOF;

statement: mapStatement | filterStatement | expressionStatement;

mapStatement: 'MAP' '(' function ',' iterable ')';

filterStatement: 'FILTER' '(' function ',' iterable ')';

expressionStatement: expression;

function: IDENTIFIER;

iterable: list | tuple | IDENTIFIER;

list: '[' (expression (',' expression)*)? ']';

tuple: '(' (expression (',' expression)*)? ')';

expression: NUMBER | STRING | BOOLEAN | list | tuple | IDENTIFIER;

// Lexer rules
MAP: 'MAP';
FILTER: 'FILTER';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+('.'[0-9]+)?;
STRING: '"' .*? '"' | '\'' .*? '\'';
BOOLEAN: 'True' | 'False';
WS: [ \t\r\n]+ -> skip;
