# P.10B revisar si puedes ver una pelicula en netflix. la condicion para esto es que seas mayor de edad y que hayas comprado la pelicula.
# 25/10/2024
# Alexandra Rodriguez Gomez.
edad = int(input("Que edad tienes: "))
compra = int(input("Compraste la pelicula \n 1 es igual a si \n 0 es igual a no \n "))
if edad >= 18 and compra:
    print("Puedes ver la pelicula")
else:
    print("NO puedes ver la pelicula")
    
print("¡GRACIAS POR USAR NETFLIX!")
