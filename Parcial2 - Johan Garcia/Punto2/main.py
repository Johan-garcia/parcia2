from antlr4 import *
from MapFilterLexer import MapFilterLexer
from MapFilterParser import MapFilterParser
from MapFilterVisitor import MapFilterVisitor

class MapFilterInterpreter(MapFilterVisitor):
    def __init__(self, functions):
        self.variables = {}
        self.functions = functions

    def visitProgram(self, ctx):
        return [self.visit(stmt) for stmt in ctx.statement()]

    def visitMapStatement(self, ctx):
        func_name = ctx.function().getText()
        iterable = self.visit(ctx.iterable())
        
        if func_name not in self.functions:
            raise NameError(f"Function '{func_name}' is not defined")
        
        func = self.functions[func_name]
        return list(map(func, iterable))

    def visitFilterStatement(self, ctx):
        func_name = ctx.function().getText()
        iterable = self.visit(ctx.iterable())
        
        if func_name not in self.functions:
            raise NameError(f"Function '{func_name}' is not defined")
        
        func = self.functions[func_name]
        return list(filter(func, iterable))

    def visitList(self, ctx):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitTuple(self, ctx):
        return tuple(self.visit(expr) for expr in ctx.expression())

    def visitExpression(self, ctx):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove quotes
        elif ctx.BOOLEAN():
            return ctx.BOOLEAN().getText() == 'True'
        elif ctx.IDENTIFIER():
            return self.variables.get(ctx.IDENTIFIER().getText())
        else:
            return self.visit(ctx.getChild(0))

def main():
    # Definimos algunas funciones de ejemplo
    def double(x):
        return x * 2

    def triple(x):
        return x * 3

    def is_even(x):
        return x % 2 == 0

    def is_positive(x):
        return x > 0

    # Creamos un diccionario con las funciones
    functions = {
        'double': double,
        'triple': triple,
        'is_even': is_even,
        'is_positive': is_positive
    }

    print("Bienvenido al intérprete de MAP y FILTER")
    print("Funciones disponibles: double, triple, is_even, is_positive")
    print("Formato de entrada:")
    print("  MAP(función, [lista de números separados por comas])")
    print("  FILTER(función, [lista de números separados por comas])")
    print("Ejemplo: MAP(double, [1, 2, 3, 4, 5])")
    print("Escribe 'salir' para terminar el programa")

    interpreter = MapFilterInterpreter(functions)

    while True:
        user_input = input("\nIngrese una operación MAP o FILTER (o 'salir' para terminar): ")
        
        if user_input.lower() == 'salir':
            break

        try:
            input_stream = InputStream(user_input)
            lexer = MapFilterLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = MapFilterParser(token_stream)
            tree = parser.program()

            results = interpreter.visit(tree)
            
            for result in results:
                print("Resultado:", result)
        except Exception as e:
            print(f"Error: {str(e)}")

    print("Gracias por usar el intérprete de MAP y FILTER")

if __name__ == '__main__':
    main()
