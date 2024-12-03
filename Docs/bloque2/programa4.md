# Calcula los impuestos de un valor
Utlizamos la funcion input para pedirle al usuario que ingrese su salario y con la funcion ``Int` lo convertimos a enteros
````python
salario = int(input("Ingrese su salario: "))
Al salarion ingresado lo multiplicamos por 0.16 para saver sus impuestos
impuestos = salario * 0.16
Utilizamos la funcion print para mostrar el resultado en pantalla, convertimos la variable a cadena de texto con `str`
print("los impuestos son:" + str(impuestos) + " pesos" + "\n ¡Gracias por usar nuestro sistema!")
