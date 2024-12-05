# programa que calcule los impuestos que debe pagar un empleado

```python
ingresos = input("¿Cuales son los ingresos? ")
ingresos = float(ingresos)
```
Pedimos al usuario que ingrese __¿Cuales son los ingresos?__ que gana y convertimos la variable a tipo `Float`

```python
if ingresos <= 1000:
    impuesto = ingresos * 0.05
elif ingresos > 1000 and ingresos <= 2500:
    impuesto = ingresos * 0.08
elif ingresos > 2500 and ingresos <= 6000:
    impuesto = ingresos * 0.12
else:
    impuesto = ingresos * 0.15
```
Se utilizan las condiciones `if elif y else` para determinar la tasa de impuesto aplicable según el rango de ingresos.
__Cálculo del impuesto__ Dentro de cada condición, se calcula el impuesto multiplicando los ingresos por la tasa correspondiente.
__Asignación del impuesto__ El resultado del cálculo se asigna a la variable impuesto.

```python
subtotal = ingresos - impuesto
```
Se calcula el salario restando el impuesto a los ingresos totales.

```python
print("Tus impuestos son " + str(impuesto) + " tu salario final es " + str(subtotal))
```
Se imprime un mensaje en pantalla mostrando el impuesto y el salario.

