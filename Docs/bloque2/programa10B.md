# Revisar si puedes ver una pelicula en netflix
## La condicional es que tengas mas de 18 años y que hayas comprado la pelicula
`edad = int(input("¿Qué edad tienes? ")):` Solicita al usuario su edad

`compra = int(input("¿Compraste la película? \n 1 es igual a sí \n 0 es igual a no \n ")):` Solicita al usuario que si compro la pelicula ingrese 1, o 0 si no la compro

Abrimos un `if` y ponemos las dos cundicionaes `if edad >= 18 and compra:` 
1. `edad >= 18:` Verifica si la edad es mayor o igual a 18.
2. `and compra:` si el valor de compra es 1 se cumple la condicion, si es 0 no se cumple la condicion.
3. Si ambas condiciones son verdaderas se mostrara el siguiente mensaje `print("Puedes ver la película")`

si se cumple una o ninguna de las condiciones utilizamos el `else:` y se mostrara el mensaje `NO puedes ver la película`

El mensaje `print("¡GRACIAS POR USAR NETFLIX!"):` se imprimira independientemente de las condiciones

