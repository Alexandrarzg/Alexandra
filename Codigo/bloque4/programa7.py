# P-7 listas con cilo for
# 07/11/24
# Alexandra Rodriguez Gomez
edades = [10,15,18,8,18,23,45,67,89,5,12,34,56,16,78,56,25,30]
menores_18 = []
adultos = []
mayores_65 = []

for edad in edades:
    if edad < 18:
        menores_18.append(edad)
    elif edad > 18 and edad < 65:
        adultos.append(edad)
    else:
        mayores_65.append(edad)

print("La lista de edades es: ",edades)
print("\nLa lista de menores es: ",menores_18)
print("\nLa lista de adultos es: ",adultos)
print("\nLa lista de mayores es: ",mayores_65)
