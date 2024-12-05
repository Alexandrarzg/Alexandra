# Funcion rango

## imprime los números del 0 al 9
```python
x = range(10)
for num in x:
    print(num)
```
La función `range(10)` crea una secuencia de números del 0 al 9 (el rango va desde 0 hasta 9, ya que range() genera números hasta
uno menos que el número final).
El bucle `for` recorre cada número en el `rango` y lo imprime.

| iteración  | num | x |
| ------------- | ------------- | ------------- |
| 1 | 0 | 0 |
| 2 | 1 | 1 |
| 3 | 2 | 2 |
| 4 | 3 | 3 |
| 5 | 4 | 4 |
| 6 | 5 | 5 |
| 7 | 6 | 6 |
| 8 | 7 | 7 |
| 9 | 8 | 8 |
| 10 | 9 | 9 |

## Imprime los números del 5 al 15
```python
print("\n Imprime los valores del 5 al 15")    
x1 = range(5, 16)
for num in x1:
    print(num)
```
La función `range(5, 16)` crea una secuencia de números del 5 al 15 (el número 16 no se incluye).
El bucle `for` recorre y imprime cada número en este rango.

| iteración  | num | x1 |
| ------------- | ------------- | ------------- |
| 1 | 0 | 5 |
| 2 | 1 | 6 |
| 3 | 2 | 7 |
| 4 | 3 | 8 |
| 5 | 4 | 9 |
| 6 | 5 | 10 |
| 7 | 6 | 11 |
| 8 | 7 | 12 |
| 9 | 8 | 13 |
| 10 | 9 | 14 |
| 11 | 10 | 15 |

## Imprime los números pares del 10 al 20
```python
print("\n Imprime los pares del del 10 al 20")
x2 = range(10, 21, 2)
for num in x2:
    print(num)
```
La función `range(10, 21, 2)` crea una secuencia de números que comienza en 10, termina en 20 y avanza de 2 en 2, selecciona los números pares entre 10 y 20.
El bucle `for` recorre los números pares y los imprime.

| iteración  | num | x2 |
| ------------- | ------------- | ------------- |
| 1 | 0 | 10 |
| 2 | 1 | 12 |
| 3 | 2 | 14 |
| 4 | 3 | 16 |
| 5 | 4 | 18 |
| 6 | 5 | 20 |

## Imprime los números impares del 11 al 21
```python
print("\n Imprime los impares del del 11 al 21")
x3 = range(11, 22, 2)
for num in x3:
    print(num)
```
La función `range(11, 22, 2)` crea una secuencia de números que comienza en 11, termina en 21 y avanza de 2 en 2, es decir, selecciona los números impares entre 11 y 21.
El bucle `for` recorre los números impares y los imprime.

| iteración  | num | x3 |
| ------------- | ------------- | ------------- |
| 1 | 0 | 11 |
| 2 | 1 | 13 |
| 3 | 2 | 15 |
| 4 | 3 | 17 |
| 5 | 4 | 19 |
| 6 | 5 | 21 |

