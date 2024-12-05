# P-6 programa que utiliza una funcion para realizar operaciones matematicas basicas
# 14/11/24
# Alexandra Rodriguez Gomez

# Funcion que realiza operaciones matematicas basicas
def operaciones(num1, num2, digitos): 
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = float(num1 / num2)
    modulo = num1 % num2
    print(f'La suma de {num1} + {num2} es: {suma}')
    print(f'La resta de {num1} - {num2} es: {resta}')
    print(f'La multiplicacion de {num1} * {num2} es: {multiplicacion}')
    print(f'La division de {num1} / {num2} es: {division:.{digitos}f}')
    print(f'El modulo de {num1} % {num2} es: {modulo:}\n\n')

# Solicitar datos al usuario
num2 = int(input('Ingrese el segundo numero: '))
num1 = int(input('Ingrese el primer numero: '))
digitos = int(input('''Ingrese la cantidad de decimales a mostrar en la division modulo: '''))

operaciones(num1,num2,digitos)
operaciones(140,8,5)
