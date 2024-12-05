# Uso de comandos "break y continue"
```python
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print("Fin del programa")
```
comienza con una variable `i` que es igual a 1 y sigue hasta que `i` sea mayor que 10.
La condición `if i == 5:` verifica si el valor de `i` es 5. 
Si es verdad, se ejecuta `break`, lo que detiene el bucle inmediatamente, 
sin imprimir el número 5 ni continuar con el resto del bucle.
Si el valor de `i` no es 5, imprime el valor de `i` y luego incrementa `i` en 1.
Cuando `i` llega a 5, se ejecuta `break` y el bucle termina. Luego, se imprime `Fin del programa`.

```python
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
print("Fin del programa")
```
comienza con `i` que es igual a 1 y sigue hasta que `i` sea mayor que 10.
La condición `if i == 5:` verifica si el valor de `i` es 5. 
Si es verdad, se ejecuta `i += 1` y luego se ejecuta `continue`.
`continue` hace que el bucle salte la iteración actual en este caso 5 y pase a la siguiente iteración, 
sin ejecutar el resto del código dentro del bucle para ese valor.
Si el valor de `i` no es 5, imprime el valor de `i` y luego incrementa `i` en 1.
Cuando `i` es 5, se incrementa en 1 y se salta la impresión de ese número,
pero el bucle continúa ejecutándose para los demás valores.
