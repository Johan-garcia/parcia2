from antlr4 import *
from RacionalesLexer import RacionalesLexer
from RacionalesParser import RacionalesParser
from RacionalesVisitor import RacionalesVisitor
from fractions import Fraction

# Visitante personalizado para evaluar expresiones racionales
class EvaluadorRacionales(RacionalesVisitor):

    def visitSuma(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitResta(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right

    def visitMultiplicacion(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right

    def visitDivision(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left / right

    def visitNumeroRacional(self, ctx):
        partes = ctx.getText().split('/')
        return Fraction(int(partes[0]), int(partes[1]))

    def visitParentesis(self, ctx):
        return self.visit(ctx.expr())

# Función para calcular el resultado de una expresión racional
def calcular_racional(entrada):
    input_stream = InputStream(entrada)
    lexer = RacionalesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RacionalesParser(stream)
    tree = parser.expr()  # Comienza el análisis sintáctico desde la regla expr

    # Usar el visitante para evaluar la expresión
    evaluador = EvaluadorRacionales()
    resultado = evaluador.visit(tree)
    print(f"Resultado: {resultado}")

# Ejemplo de uso con entrada por consola
if __name__ == "__main__":
    expresion = input("Introduce una expresión racional: ")
    calcular_racional(expresion)

