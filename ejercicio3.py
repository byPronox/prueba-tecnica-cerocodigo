def calcular_total(productos):
    
    total = 0

    for producto in productos:

        if "cantidad" not in producto or "precio" not in producto:
            continue

        cantidad = producto["cantidad"]
        precio = producto["precio"]

        if cantidad > 0:
            total += cantidad * precio

    return total


productos = [

    {"nombre": "Producto A", "cantidad": 2, "precio": 10},
    {"nombre": "Producto B", "cantidad": 3, "precio": 5}

]

print(calcular_total(productos))