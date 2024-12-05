# P4  programa que calcule los impuestos que debe pagar un empleado
# 29/10/2024
# Alexandra Rodriguez Gomez
ingresos = input("¿Cuales son los ingresos? ")
ingresos = float(ingresos)

if ingresos <= 1000:
    impuesto = ingresos * 0.05
elif ingresos > 1000 and ingresos <= 2500:
    impuesto = ingresos * 0.08
elif ingresos > 2500 and ingresos <= 6000:
    impuesto = ingresos * 0.12
else:
    impuesto = ingresos * 0.15
subtotal = ingresos - impuesto
print("Tus impuestos son " + str(impuesto) + " tu salario final es " + str(subtotal))
