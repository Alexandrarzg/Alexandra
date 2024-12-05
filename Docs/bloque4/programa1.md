# Ciclo For 

```python
lista_num = [10 , 30 , 40 , 20 , 35 , 80]
```
Creamos una lista con 6 numeros y guardamos la lista en la variable `lista_num`

```python
print(lista_num[0])
print(lista_num[1])
print(lista_num[2])
print(lista_num[3])
print(lista_num[4])
print(lista_num[5])
```
En esta parte del código, se accede a cada elemento de la lista `lista_num` mediante sus índices (que van de 0).
El resultado de este bloque es la impresión de cada valor de la lista en el orden en que están almacenados.

```python
for i in lista_num:
    print(i)
```
El bucle `for` recorre todos los elementos de la lista `lista_num` y los imprime uno por uno. la variable `i` toma el valor de cada elemento de la lista en cada iteración.
Este bloque de código es más eficiente y flexible, ya que no necesitas especificar los índices manualmente.

| iteración  | i |
| ------------- | ------------- |
| 1 | 10  |
| 2 | 30  |
| 3 | 40  |
| 4 | 20  |
| 5 | 35  |
| 6 | 80  |
