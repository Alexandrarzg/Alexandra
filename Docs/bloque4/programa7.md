# listas con cilo for
Se crea una lista edades que contiene diversas edades
```python
edades = [10,15,18,8,18,23,45,67,89,5,12,34,56,16,78,56,25,30]
```
Se crean tres listas vacías: menores_18, adultos y mayores_65, que servirán para almacenar las edades clasificadas.
```python
menores_18 = []
adultos = []
mayores_65 = []
```
Se itera sobre cada elemento de edad de la lista edades. Si la edad es menor que 18 se agrega a la lista `menores_18`.
Si la edad es mayor de 18 pero menor de 65 se agrega a la lista `adultos`.
En cualquier otro caso mayor o igual a 65 se agrega a la lista `mayores_65`.
```python
for edad in edades:
    if edad < 18:
        menores_18.append(edad)
    elif edad > 18 and edad < 65:
        adultos.append(edad)
    else:
        mayores_65.append(edad)
```
Se imprimen las cuatro listas para visualizar la clasificación.
```python
print("La lista de edades es: ",edades)
print("\nLa lista de menores es: ",menores_18)
print("\nLa lista de adultos es: ",adultos)
print("\nLa lista de mayores es: ",mayores_65)
```

La lista de menores es:  [10, 15, 8, 5, 12, 16]

La lista de adultos es:  [23, 45, 34, 56, 56, 25, 30]

La lista de mayores es:  [18, 18, 67, 89, 78]
