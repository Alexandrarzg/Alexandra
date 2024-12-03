# ♠ Calcular el promedio de 5 unidades e indicar si aprobo o reprobo
Pedimos la calificaciòn de las 5 unidades al usuario con la funcion `input`
```python
u1 = int(input("Calificacion de la unidad 1: "))
u2 = int(input("Calificacion de la unidad 2: "))
u3 = int(input("Calificacion de la unidad 3: "))
u4 = int(input("Calificacion de la unidad 4: "))
u5 = int(input("Calificacion de la unidad 5: "))
```
- promediamos todas las calificaciones sumandolas y liego dividiendolas entre 5
```python
promedio = (u1 + u2 + u3 + u4+ u5) / 5
```
- Abrimos una condicional `if`, si la condiciòn comprueba que el promedio es mayor o igual a 7 imprimira `Ustes aprobo`
- Si la condicion no se cumple utilizamos un `else` que imprimira `Usted no aprobo`
```python
if promedio >= 7:
    print("Usted aprobo")
else:
    print("Usted reprobo")
```
