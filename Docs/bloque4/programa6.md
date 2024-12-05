# programa que permita crear una lista de todos los numeros menores a 50.

Crear una lista de números llamada `numeros`
```python
numeros = [10 , 50 , 25 , 15 , 10 , 28 , 100 , 500 , 24 , 24]
```
Crear una lista vacía llamada `menores_50`, donde se almacenarán los números de la lista original que sean menores que 50.
```python
menores_50 = []
```
El bucle recorre cada elemento de la lista numeros. 
Si el número es menor que 50, se agrega a la lista `menores_50` utilizando el método `append()`.
```python
for numero in numeros:
    if numero < 50:
        menores_50.append(numero)
```
Al final, se imprimen ambas listas, la lista original y la nueva lista que contiene solo los números menores que 50.

La lista original es:  [10, 50, 25, 15, 10, 28, 100, 500, 24, 24]

La nueva lista es:  [10, 25, 15, 10, 28, 24, 24]

