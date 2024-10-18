from antlr4 import *
from LaplaceTransformLexer import LaplaceTransformLexer
from LaplaceTransformParser import LaplaceTransformParser
from LaplaceTransformListener import LaplaceTransformListener

class LaplaceTransformEvaluator(LaplaceTransformListener):
    def __init__(self):
        self.stack = []

    def exitExpression(self, ctx):
        pass

    def exitAdditionExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return
        result = self.stack.pop()
        for i in range(ctx.getChildCount() - 2, -1, -2):
            op = ctx.getChild(i).getText()
            left = self.stack.pop()
            if op == '+':
                result = f"({left} + {result})"
            elif op == '-':
                result = f"({left} - {result})"
        self.stack.append(result)

    def exitMultiplicationExpression(self, ctx):
        if ctx.getChildCount() == 1:
            return
        result = self.stack.pop()
        for i in range(ctx.getChildCount() - 2, -1, -2):
            op = ctx.getChild(i).getText()
            left = self.stack.pop()
            if op == '*':
                result = f"({left} * {result})"
            elif op == '/':
                result = f"({left} / {result})"
        self.stack.append(result)

    def exitPowerExpression(self, ctx):
        if ctx.getChildCount() == 3:
            right = self.stack.pop()
            left = self.stack.pop()
            self.stack.append(f"({left} ^ {right})")

    def exitAtom(self, ctx):
        if ctx.NUMBER():
            self.stack.append(ctx.NUMBER().getText())
        elif ctx.ID():
            self.stack.append(ctx.ID().getText())
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            pass
        elif ctx.MINUS():
            expr = self.stack.pop()
            self.stack.append(f"(-{expr})")

    def exitFunctionCall(self, ctx):
        func_name = ctx.ID().getText()
        args = [self.stack.pop() for _ in range(ctx.getChildCount() - 3)][::-1]
        self.stack.append(f"{func_name}({', '.join(args)})")

    def exitLaplaceTransform(self, ctx):
        expr = self.stack.pop()
        self.stack.append(f"L{{{expr}}}")

def evaluate(expression):
    input_stream = InputStream(expression)
    lexer = LaplaceTransformLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaplaceTransformParser(stream)
    tree = parser.expression()
    
    evaluator = LaplaceTransformEvaluator()
    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)
    
    return evaluator.stack.pop()

def main():
    print("Bienvenido al evaluador de transformadas de Laplace.")
    print("Ingrese expresiones para evaluar (o 'salir' para terminar).")
    
    while True:
        expr = input("\nIngrese una expresión: ").strip()
        
        if expr.lower() == 'salir':
            print("Gracias por usar el evaluador. ¡Hasta luego!")
            break
        
        try:
            result = evaluate(expr)
            print(f"Resultado: {result}")
        except Exception as e:
            print(f"Error al evaluar '{expr}': {str(e)}")

if __name__ == "__main__":
    main()
