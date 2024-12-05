# Identificacion de tipos de datos str, int y float
El programa comienza pidiendo al usuario que ingrese su edad mediante el `input()`
la variable almacena el valor ingresado como un `string`,
el programa usa `type(variable)` para mostrar el tipo de la variable, que será `str` porque `input()` devuelve siempre una cadena de texto.

## Coversion a entero
La función `int()` convierte el valor de la variable en un número entero.
```python
variable = int(variable)
print(type(variable))
```
La variable ahora contiene un número entero, y `type(variable)` imprimirá `int`

## Conversion flotante
La función `float()` convierte la variable, que ahora es un número entero, a un número de tipo flotante (un número con decimales).
Después de esta conversión, type(variable) mostrará float como el tipo de la variable.
```python
variable = float(variable) 
print(type(variable))
```
