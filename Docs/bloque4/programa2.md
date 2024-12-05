# Introduccion al Ciclo FOR

Se crea una lista llamada `nombres` que contiene cinco nombres de personas.
```python
nombres = ["Luis" , "Juan" , "Eduardo" , "Chuy" , "Marcos"]
```
Bucle `for`
```python
for nombre in nombres:
    print("El nombre es " , nombre)
```
`for nombre in nombres:`
Este línea inicia un bucle for que iterará sobre cada elemento de la lista nombres. En cada iteración,
la variable nombre tomará el valor del siguiente elemento de la lista.
`print("El nombre es " , nombre)` Dentro del bucle, se imprime un mensaje en la consola, 
reemplazando nombre por el valor actual de la variable en cada iteración.

| iteración  | nombre | nombres  |
| ------------- | ------------- | -------------- |
| 1 | 0  | Luis |
| 2 | 1  | Juan |
| 3 | 2  | Eduardo |
| 4 | 3  | Chuy |
| 5 | 4  | Marcos |

Se crea una lista llamada `frutas` que contiene el nombre de tres frutas
```python
frutas = ["Manzana" , "Piña" , "Platano"]
```
Se utiliza el bucle `for` para imprimir el nombre de cada fruta
```python
for fruta in frutas:
    print("La fruta es: ",fruta)
```
| iteración  | fruta | frutas  |
| ------------- | ------------- | -------------- |
| 1 | 0  | Manzana |
| 2 | 1  | Piña |
| 3 | 2  | Platano |

