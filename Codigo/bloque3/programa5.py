# P5 programa que calcule el nivel de desampeño de un estudiante respecto con su calificacion dada por el usuario.
# 29/10/2024
# Alexandra Rodriguez Gomez
cal = int(input("¿Cual es su calificacion? "))

if cal < 60:
    print("Su nivel de desempeño es insuficiente")
elif cal >= 70 and cal <= 79:
    print("Su nivel de desempeño es suficiente")
elif cal >= 80 and cal <= 89:
    print("Su nivel de desempeño esta muy bien")
elif cal >= 90 and cal <= 95:
    print("Su nivel de desempeño es notable")
else:
    print("Su nivel de desempeño es excelente")
print(" \n ¡Gracias por usar nuestro sistema!")
