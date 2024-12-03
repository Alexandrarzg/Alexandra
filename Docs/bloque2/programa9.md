# calcula el costo total de un numero de articulos
1. Le pedimos al usuario que ingrese la cantidad de articulos adquiridos con la funcion `input`
2. Abrimos un condicional `if`, si la cantidad de articulos es mayor a 3 el precio de cada articulo sera $30
3. Multiplicamos la cantidad de articulos por treinta
```python
if articulos > 3:
   total = articulos * 30
```
4.  si la condicional no se cumple `else` el costo de cada articulo sera de $40
5.  Multiplicamos la cantidad de articulos por cuarenta
```python
else:
    total = articulos * 45
```
5. por ultimo imprimimos el total a pagar
```python
print("El total a pagar es $" + str(total))
```
