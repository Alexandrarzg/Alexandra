# p-11 agregar un cilco while para que se repita hasta que ingrese la palabra salir
# 15/11/24
# Alexandra Rodriguez Gomez

def primo(num):
    if num < 10 or num > 99:
        return "El número ingresado no está en el rango de 10 a 99."
    
    for i in range(2, num):
        if num % i == 0:
            return f"El número {num} no es primo."
    
    return f"El número {num} es primo."

while True:
    entrada = input("Ingrese un numero o 'salir' para terminar: ")
    
    if entrada.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    try:
        num = int(entrada)
        
        resultado = primo(num)
        
        print(resultado)
    
    except ValueError:
        print("Por favor, ingresa un número válido.")
