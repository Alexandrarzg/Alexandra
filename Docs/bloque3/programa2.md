#  el primero numero  es mayor, igual o menor que el segundo
```python
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
```
Estas líneas solicitan al usuario que ingrese dos números.
La función `input()` captura lo que el usuario escribe y la función `int()` 
convierte ese valor de texto en un número entero para poder realizar operaciones matemáticas con ellos.

```python
if num1 > num2:
```
Esta línea inicia una condición: si el número __num1__ es mayor que __num2__, se ejecutará el bloque de código indentado debajo.

Si la condición anterior es verdadera, se imprime un mensaje indicando que __num1__ es mayor que __num2__. 
La función `str()` convierte los números __num1__ y __num2__ nuevamente en texto para poder concatenarlos con el resto del mensaje.

```python
elif num1 == num2:
```
Si la primera condición no se cumple (es decir, num1 no es mayor que num2), se verifica si ambos números son iguales.
Si la condición anterior es verdadera, se imprime un mensaje indicando que ambos números son iguales.

Si ninguna de las condiciones anteriores se cumple (es decir, num1 no es mayor ni igual a num2), se ejecuta la condicion `else`
