# P.10A Revisar si puedes ver una pelicula en Netflix. La condicion para esto es que seas mayor de edad y que hayas comprado la pelicula (Anidados)
# 24/10/2024
# Alexandra Rodriguez Gomez
# SOLUCION 1 if, AND
edad = int(input("Cuantos años tienes: "))

if edad >= 18:
    compra = int(input("Compraste la pelicula \n 1 significa si \n 0 significa no \n "))
    if compra == 1:
        
        print("Puede ver la pelicula")
else:
    print("No puede ver la pelicula, vete a hacer la tarea")
    
print("Gracias por usar Netflix")
