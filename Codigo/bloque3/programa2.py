# P2 tercer bloque programa que indique si , de dos numeros enteros ingresados , el primero es mayor, igual i menor que el segundo
# 28/10/2024
# Alexandra Rodriguez Gomez
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))
if num1 > num2:
    print("El numero " + str(num1) + " es mayor que " + str(num2))
elif num1 == num2:
    print("Son numeros iguales")
else:
    print("El numero " + str(num1) + " es menor que " + str(num2))
