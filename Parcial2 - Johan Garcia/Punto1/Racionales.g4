grammar Racionales;

// Regla de inicio
expr: expr '+' expr    # Suma
    | expr '-' expr    # Resta
    | expr '*' expr    # Multiplicacion
    | expr '/' expr    # Division
    | '(' expr ')'     # Parentesis
    | RACIONAL         # NumeroRacional
    ;

// Regla para definir números racionales
RACIONAL: NUM '/' NUM;

// Regla para reconocer números enteros
NUM: [0-9]+;

// Ignorar espacios en blanco
WS: [ \t\r\n]+ -> skip;

