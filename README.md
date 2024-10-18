# Proyectos ANTLR: Calculadora Racional, MAP/FILTER y Transformadas de Laplace

Este repositorio contiene tres proyectos que utilizan ANTLR y Python para implementar diferentes funcionalidades matemáticas y de procesamiento de datos.

## Proyectos incluidos

1. Calculadora de Números Racionales
2. Intérprete de MAP y FILTER
3. Evaluador de Transformadas de Laplace

## Requisitos generales

- Python 3.7+
- ANTLR4
- antlr4-python3-runtime
- Java Runtime Environment (JRE) para ejecutar la herramienta ANTLR

## Instalación general

1. Descarga el archivo:
 
2. Crea el entorno virtual; para ejecutar cualquiera de los puntos debemos de abrir el archivo y dirigirse al punto que desea ejecutar, en esa carpeta se debe de abrir uan termianl y ejecutar los sguientes comandos:
```
python3 -m venv antlr-env
```
```
source antlr-env/bin/activate
```
```
pip install antlr4-python3-runtime
```
3. Despues de esto ya se podra ejecutar el punto, en caso de error descargar las librerias necesarias.
4. En caso de querer solo ejecutar los puntos descargue este archivo a traves del siguiente link(para asegurar la correcta ejecucion, habilite el entorno virtual y ejecute el archvo .py unicamente)
 ```
https://drive.google.com/file/d/16cXFUOCco5J6f9he43E-GkjLkqjfqwmH/view?usp=drive_link
```

## Proyecto 1: Calculadora de Números Racionales

### Descripción
Este proyecto implementa un parser que permite realizar operaciones con números racionales.

### Uso
1. Genera los archivos Python de ANTLR:
   ```
    antlr4 -Dlanguage=Python3 -visitor Racionales.g4
   ```
2. Ejecuta el script principal:
   ```
   python3 main.py
   ```
### Ejemplo de uso
```
Ingrese una expresión: 5/7 + 1/3

```

## Proyecto 2: Intérprete de MAP y FILTER

### Descripción
Este proyecto implementa un intérprete simple para operaciones MAP y FILTER en listas de números.

### Uso
1. Genera los archivos Python de ANTLR:
   ```
    antlr4 -Dlanguage=Python3 -visitor MapFilter.g4
   ```
2. Ejecuta el script principal:
   ```
   python3 main.py
   ```

### Ejemplos de uso
- `MAP(double, [1, 2, 3, 4, 5])`
- `FILTER(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`

### Funciones disponibles
- `double`: Multiplica un número por 2
- `triple`: Multiplica un número por 3
- `is_even`: Verifica si un número es par
- `is_positive`: Verifica si un número es positivo

## Proyecto 3: Evaluador de Transformadas de Laplace

### Descripción
Este proyecto implementa un evaluador de expresiones matemáticas con soporte para transformadas de Laplace.

### Uso
1. Genera los archivos de ANTLR:
   ```
   antlr4 -Dlanguage=Python3 -visitor LaplaceTransform.g4
   ```
2. Ejecuta el script principal:
   ```
   python3 main.py
   ```

### Ejemplos de uso
```
Ingrese una expresión: 2 * t + 3
Resultado: ((2 * t) + 3)
Ingrese una expresión: L{t^2}
Resultado: L{(t ^ 2)}
Ingrese una expresión: exp(-a*t) * sin(w*t)
Resultado: (exp((-a * t)) * sin((w * t)))
```

## Estructura del proyecto

- `RationalCalculator.g4`: Gramática ANTLR para la calculadora racional
- `MapFilter.g4`: Gramática ANTLR para el intérprete MAP/FILTER
- `LaplaceTransform.g4`: Gramática ANTLR para el evaluador de Laplace
- `rational_main.py`: Script principal para la calculadora racional
- `map_filter_main.py`: Script principal para el intérprete MAP/FILTER
- `laplace_main.py`: Script principal para el evaluador de Laplace
- Archivos generados por ANTLR4 para cada proyecto
