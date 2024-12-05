# Tpos de mascota
Este código 
```python
nombre = input("Ingrese el tipo de mascota: ")
```
muestra el mensaje `Ingrese el tipo de mascota:` en la pantalla y espera a que el usuario ingrese un texto
El valor que el usuario ingrese se almacena en la variable `nombre`

La instrucción `if` evalúa si la palabra __perro__ está presente en el texto ingresado por el usuario.
Si la palabra __perro__ está en la cadena nombre, se ejecutará el bloque de código dentro del `if` que imprime __es un perro__

Si la palabra __perro__ no está en la entrada, el programa pasa a la siguiente condición `elif`
que verifica si la palabra __gato__ está en la variable nombre.
Si se encuentra la palabra __gato__, se ejecutará el bloque de código dentro del `elif`, y el programa imprimirá `Es un gato`.

Si ni la palabra __perro__ ni la palabra __gato__ están presentes en la variable, se ejecutará el bloque de código dentro del `else`.
En este caso, el programa imprimirá `Mascota desconocida`.
