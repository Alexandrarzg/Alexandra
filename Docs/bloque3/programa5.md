# Programa que calcule el nivel de desampeño de un estudiante respecto con su calificacion.

el programa solicita al usuario que ingrese su calificación utilizando `input()`,
Como el valor ingresado es una cadena de texto, la función `int()` convierte esta entrada a un número entero.

1. primer condicional `if` si la calificacion ingresada es menor a 60 el programa imprime `Su nivel de desempeño es insuficiente`
2. Senundo condicional `elif` si la calificacion ingresada esta entre 70 y 79 el programa imprime `Su nivel de desempeño es suficiente`
3. Tercer condicional `elif` si la caificacion ingresada esta entre 80 y 89 el programa imprime `Su nivel de desempeño esta muy bien`
4. Cuarta condicional `elif` si la calificacion ingresada esta entre 90 y 95 el programa imprime `Su nivel de desempeño es notable`
5. Condicional `elif` si la calificacion es mayor a 95 el programa imprime `Su nivel de desempeño es excelente`

Después de que se haya mostrado el mensaje correspondiente al nivel de desempeño, 
el programa imprime un mensaje de despedida: __"¡Gracias por usar nuestro sistema!"__
