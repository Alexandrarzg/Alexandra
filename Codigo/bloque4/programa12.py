# P-12 Ciclo infinito programa que se repite hasta que ingrese la palabra salir.
# 8/11/24
# Alexandra Rodriguez Gomez

# Inicializacion de variables
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() # Convierte la palabra a nimusculas
    print("usted ingreso: ",palabra)
    if palabra == "salir":
        break
print("Fin del programa \U0001F601 \n\n") # imprime un emoji feliz
print("¡HASTA LUEGO! \U0001F44B \n") #imprime un emoji de saludo
