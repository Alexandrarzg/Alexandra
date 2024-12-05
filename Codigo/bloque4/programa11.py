# P-11 RepiteWhile Programa que se repite hasta que ingrese la palabra "Salir"
# 08/11/24
# Alexandra Rodriguez Gomez

# Inicializacion de variables
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa uan palbara o 'salir' para ternimar: ")
    palabra = palabra.lower() #Convierte las palabras a minusculas
    print("Usted ingreso:", palabra)
    print("Fin del programa")
