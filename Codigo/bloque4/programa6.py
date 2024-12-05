# P-6 programa que permita crear una lista de todos los numeros menores a 50.
# 06/11/24
# Alexandra Rodriguez Gomez
numeros = [10 , 50 , 25 , 15 , 10 , 28 , 100 , 500 , 24 , 24]
menores_50 = [] # crea un vector vacio
for numero in numeros:
    if numero < 50:
       menores_50.append(numero)  
print("La lista original es: ",numeros)
print("La nueva lista es: ",menores_50)
