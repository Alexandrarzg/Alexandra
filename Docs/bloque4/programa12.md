# Ciclo infinito, Programa que se repite hasta que ingrese la palabra salir.

Se crea una varible vacia llamada `Palabra`
```python
palabra = ""
```

El bucle seguira ejecutándose mientras la variable `palabra` no sea igual a "salir". 
Cuando el usuario ingrese "salir", el bucle se detendrá.
```python
while palabra != "salir":
```

El programa solicita al usuario que ingrese una palabra. Lo que se ingresa se asigna a la variable `palabra`.
```python
palabra = input("Ingresa una palabra o 'salir' para terminar: ")
```

Convertir la palabra a minusculas.
```python
palabra = palabra.lower()
```

Imprime la palabra que el usuario ingreso.
```python
print("usted ingreso: ",palabra)
```

Si el usuario ingresa "salir" se ejecuta `break`, lo que hace que el bucle se termine inmediatamente.
```python
if palabra == "salir":
    break
```
Cuando se termie el programa se imprimira el siguiente mensaje "Fin del programa y ¡HASTA LUEGO!")
