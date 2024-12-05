# Agregando elementos en una lista

```python
colores = ["rojo", "azul"]
```
Creamos una lista de tipo `string` con nombres de colores y la guardamos en la variable `colores`

- `print(colores)` imprimimos la lista en la consola

```python
colores.append("verde")
```
el `append` se utiliza para agregar elementos nuevos a una lista, en este caso el color `verde`

- `print(colores)` imprimimos la lista nuevamente, pero esta vez aparecera el nuevo elemento que agregamos
- `print(colores + "amarillo")` Marca error ya que no podemos sumar una lista con una cadena de texto

