# Ciclos for, contador
## Se crea una lista llamada `letras` que contiene las primeras cinco letras del alfabeto.
```python
letras = ["a", "b" , "c" , "d" , "e"]
```
Se crea una variable `contador` y se inicializa en 0. Esta variable se utilizará para llevar la cuenta de las iteraciones del bucle.

```python
contador = 0
for letra in letras:
    contador = contador + 1
print("La lista letras tiene ",contador,"letras")
```
Se itera sobre cada elemento de la lista letras. En cada iteración, se incrementa el valor de contador en 1.

Impresión del resultado: Se imprime un mensaje indicando el número total de elementos en la lista `letras.`

## Se crea una lista llamada `numeros` que contiene cuatro números.
```python
numeros = [100,200,300,400]
```
Se crea una variable `sumatoria` y se inicializa en 0. Esta variable se utilizará para llevar la cuenta de las iteraciones del bucle.
```python
sumatoria = 0
for numero in numeros:
    sumatoria = sumatoria + numero
print("La sumatoria es: ",sumatoria)
```
Se itera sobre cada elemento de la lista numeros. En cada iteración, se suma el valor del elemento actual a la variable `sumatoria.`

Impresión del resultado: Se imprime el resultado de la suma.

## Se crea una lista llamada `palabras` que contiene tres palabras.
```python
palabras = ["Hoy " , "Hace " , "Frìo"]
```
Se crea una variable mensaje y se inicializa como una cadena vacía.
```python
mensaje = ""
for palabra in palabras:
    mensaje = mensaje + palabra
print(mensaje)
```
Se itera sobre cada elemento de la lista `palabras`. En cada iteración, se concatena la palabra actual al final de la variable mensaje.

Impresión del resultado: Se imprime el mensaje completo.

## Se crea una lista llamada `lista_anterior` que contiene nombres de frutas.
```python
lista_anterior = ["Manzana", "Piña" , "Uva"]
```
Se crea una lista vacía llamada `lista_nueva`
```python
lista_nueva = []
print("La lista vacia ", lista_nueva)
for fruta in lista_anterior:
    lista_nueva.append(fruta)
print("La lista copiada es: ", lista_nueva)
```
Se itera sobre cada elemento de la lista `lista_anterior`. En cada iteración, se agrega el elemento actual a la lista `lista_nueva` utilizando el método `append()`.

Impresión del resultado: Se imprime la lista copiada.

