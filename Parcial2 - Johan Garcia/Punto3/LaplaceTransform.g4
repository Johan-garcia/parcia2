grammar LaplaceTransform;

// Reglas del analizador
program: statement+ EOF;

statement
    : functionDeclaration
    | expression
    ;

functionDeclaration
    : 'function' ID '(' parameter? (',' parameter)* ')' '=' expression
    ;

expression
    : laplaceTransform
    | additionExpression
    ;

laplaceTransform
    : 'L' '{' additionExpression '}'
    ;

additionExpression
    : multiplicationExpression ((PLUS | MINUS) multiplicationExpression)*
    ;

multiplicationExpression
    : powerExpression ((MUL | DIV) powerExpression)*
    ;

powerExpression
    : atom (POW atom)?
    ;

atom
    : NUMBER
    | ID
    | '(' additionExpression ')'
    | functionCall
    | MINUS atom
    ;

functionCall
    : ID '(' additionExpression? (',' additionExpression)* ')'
    ;

parameter: ID;

// Reglas del lexer
ID: [a-zA-Z]+;
NUMBER: [0-9]+ ('.' [0-9]+)?;
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
POW: '^';
WS: [ \t\r\n]+ -> skip;
