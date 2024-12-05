# P-10 crear una funcion
# 15/11/24
# Alexandra Rodriguez Gomez

def es_primo(num):
    # Verificar si el número está en el rango de 10 a 99
    if num < 10 or num > 99:
        return "El número ingresado no está en el rango de 10 a 99."
    

    for i in range(2, num):
        if num % i == 0:
            return f"El número {num} no es primo."
    
    return f"El número {num} es primo."

num = int(input("Ingrese un numero: "))

resultado = es_primo(num)

print(resultado)
