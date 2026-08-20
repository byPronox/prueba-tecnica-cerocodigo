ventas = [
    {"cliente": "Juan", "total": 150},
    {"cliente": "Maria", "total": 250},
    {"cliente": "Juan", "total": 300},
    {"cliente": "Pedro", "total": 100},
    {"cliente": "Maria", "total": 50},
]


def resumen_clientes(ventas):
    resumen = {}

    for venta in ventas:
        cliente = venta["cliente"]
        total = venta["total"]

        if cliente in resumen:
            resumen[cliente]["total"] += total
            resumen[cliente]["compras"] += 1
        else:
            resumen[cliente] = {"total": total, "compras": 1}

    lista_resumen = []
    for cliente in resumen:
        lista_resumen.append({
            "cliente": cliente,
            "total": resumen[cliente]["total"],
            "compras": resumen[cliente]["compras"]
        })

    lista_resumen.sort(key=lambda x: x["total"], reverse=True)

    return lista_resumen


print(resumen_clientes(ventas))