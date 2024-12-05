# P-9 Es un programa que demuestra el uso de comandos "break y continue"
# 08/11/24
# Alexandra Rodriguez Gomez

# Ejemplo 1 - break
# Imprimir los numeros del 1 al 10
# pero si el numero es 5, salir de
# ciclo while
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1 # Equivalente a i = i + 1
print("Fin del programa")
    
# Ejemplo 2 - Continue
# I mprimir los numeros del 1 al 10,
# pero si el numero es 5, omitirlo
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
print("Fin del programa")
