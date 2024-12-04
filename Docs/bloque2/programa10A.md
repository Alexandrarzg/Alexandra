# Revisar si puedes ver una pelicula en Netflix
## La condicion es que tienes que ser mayor de edad y que hayas comprado la pelicula
pedimos al usuario su edad con `input`
 ```python
edad = int(input("Cuantos años tienes: "))
```
Abrimos un condicional `if` que nos diga que la edad tiene que ser mayor o igual que 18, si la condicion se cumple el programa preguntara si ha comprado la pelicula, 
si no se cumple el programa saltara al bloque `else`
1. Si el usuario tiene 18 años o más, el programa le pide que ingrese 1 si compró la película, o 0 si no la compró.
2. i el usuario ingresó 1, significa que compró la película, por lo que se ejecuta el segundo `if`, y mostrara el mensaje que se puede ver la pelicula

Si no se cumplen los condicionales utilizaremos `else`, si el usuario no tiene 18 o mas se mostrara el mensaje `usted no puede ver la pelicula`

Este mensaje `Gracias por usar Netflix` siempre se imprimirá independientemente de las decisiones anteriores, ya que está fuera de las condiciones.
