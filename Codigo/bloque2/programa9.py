# P.9 programa que calcule el costo total de un numero de articulos si son 3 articulos o menos precio unitario $45, mas de 3 artuculos precio unitario $30 al final mostrar un mensaje
# 24/10/2024
# Alexandra Rodriguez Gomez
articulos = int(input("Cantidad de articulos: "))
if articulos > 3:
   total = articulos * 30
   
else:
    total = articulos * 45

print("El total a pagar es $" + str(total))
