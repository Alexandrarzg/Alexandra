# P-5 Ciclos for, contador
# 05/11/24
# Alexandra Rodriguez Gomez
letras = ["a", "b" , "c" , "d" , "e"]
contador = 0
for letra in letras:
    contador = contador + 1
print("La lista letras tiene ",contador,"letras")

print("\n sumatoria")
numeros = [100,200,300,400]
sumatoria = 0
for numero in numeros:
    sumatoria = sumatoria + numero
print("La sumatoria es: ",sumatoria)

print("\n suma con string")
palabras = ["Hoy " , "Hace " , "Frìo"]
mensaje = ""
for palabra in palabras:
    mensaje = mensaje + palabra
print(mensaje)


print("\n map pattern")
lista_anterior = ["Manzana", "Piña" , "Uva"]
lista_nueva = []
print("La lista vacia ", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
print("La lista copiada es: ", lista_nueva)
