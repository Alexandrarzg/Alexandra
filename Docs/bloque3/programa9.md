# ♠ igualdad en las listas, compare puntos de todas las demas listas

```python
puntos =[10 , 50 , 20]
puntos_2 =[10 , 50 , 20]
ordenados =[10 , 20 , 50]
puntos_texto =["10" , "50" , "20"]
```
Creamos 4 listas que contengan los mismos numeros, una ordenada diferente y otra de tipo `string`

- `print(puntos == puntos_2)` Compara si __puntos__ y __puntos_2__ son iguales, dado que ambas listas contienen los mismos elementos en el mismo orden, el resultado será __True__.
- `print(puntos == ordenados)` Compara si __puntos__ y __ordenados__ son iguales, dado que en las listas de Python el orden de los elementos es importante, el resultado será __False.__
- `print(puntos_texto == puntos)` Compara si __puntos_texto__ y __puntos__ son iguales, aunque los valores numéricos son los mismos, los tipos son diferentes (strings y enteros), por lo que el resultado será __False.__
- `print(puntos != puntos_2)` Compara si puntos y puntos_2 no son iguales, dado que ambas son iguales, el resultado será __False.__
- `print(puntos != ordenados)` Compara si puntos y ordenados no son iguales, como el orden de los elementos es diferente, el resultado será __True.__
- `print(puntos != puntos_texto)` Compara si puntos y puntos_texto no son iguales, dado que los tipos de los elementos (enteros y string) son diferentes, el resultado será __True.__
