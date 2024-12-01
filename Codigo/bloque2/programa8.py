# P.8 programa que calcule el promedio de 5 unidades e indique si aprobo o reprobo la materia.
# 24/10/2024
# Alexandra Rodriguez Gomez.
u1 = int(input("Calificacion de la unidad 1: "))
u2 = int(input("Calificacion de la unidad 2: "))
u3 = int(input("Calificacion de la unidad 3: "))
u4 = int(input("Calificacion de la unidad 4: "))
u5 = int(input("Calificacion de la unidad 5: "))
promedio = (u1 + u2 + u3 + u4+ u5) / 5
if promedio >= 7:
    print("Usted aprobo")
else:
    print("Usted reprobo")
