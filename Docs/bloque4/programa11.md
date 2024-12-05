# Programa que se repite hasta que ingrese la palabra "Salir"
Se crea una variable vacía llamada `palabra`
```python
palabra = ""
```
El bucle while continuará ejecutándose mientras la variable `palabra` no sea igual a `salir`. 
Esto significa que el programa se seguira ejecutando continuamente hasta que el usuario ingrese la palabra `salir`.
```python
while palabra != "salir":
```
El programa pide al usuario que ingrese una palabra. El valor ingresado se asigna a la variable`palabra`.
```python
palabra = input("Ingresa una palabra o 'salir' para terminar: ")
```
Convertimos la palabra ingresada en minusculas
```python
palabra = palabra.lower()
```
Imprimimos la palabra ingresada
```python
print("Usted ingreso:", palabra)
```
Si el usuari ingreso la palabra "Salir" se terminara el programa y se mostrara el siguiente mensaje "Fin del programa"
