import json
from modules.utils import cargarDatos

rutaFacturas = "data/facturas.json"


def ranking_productos_menos_vendidos(fecha_inicio, fecha_fin):
    facturas = cargarDatos(rutaFacturas)

    if not facturas:
        print("No hay facturas registradas")
        return

    # 🔹 Filtrar por rango de fechas
    facturasFiltradas = [
        f for f in facturas
        if fecha_inicio <= f["fecha"][:10] <= fecha_fin
    ]

    if not facturasFiltradas:
        print("No hay ventas en ese rango de fechas")
        return

    # 🔹 Contar productos
    conteo = {}

    for factura in facturasFiltradas:
        for item in factura["productos"]:
            codigo = item["codigo"]
            nombre = item["nombre"]
            cantidad = int(item["cantidad"])

            if codigo not in conteo:
                conteo[codigo] = {
                    "nombre": nombre,
                    "cantidad": 0
                }

            conteo[codigo]["cantidad"] += cantidad

    # 🔹 Convertir a lista y ordenar (MENOR a MAYOR)
    ranking = [
        {
            "codigo": cod,
            "nombre": data["nombre"],
            "cantidad": data["cantidad"]
        }
        for cod, data in conteo.items()
    ]

    ranking.sort(key=lambda x: x["cantidad"])

    # 🔹 Mostrar TOP 5 menos vendidos
    print("\n--- PRODUCTOS MENOS VENDIDOS ---\n")

    for p in ranking[:5]:
        print(f"{p['nombre']} (Cod: {p['codigo']}) → {p['cantidad']} vendidos")

    # 🔹 Exportar JSON completo
    with open("reports/ranking_menos_vendidos.json", "w", encoding="utf-8") as archivo:
        json.dump(ranking, archivo, indent=4)

    print("\n✅ Ranking completo exportado en /reports/ranking_menos_vendidos.json")
    
crear carpeta reportes




llamar menu:
from modules.reportes import ranking_productos_menos_vendidos

fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
fecha_fin = input("Fecha fin (YYYY-MM-DD): ")

ranking_productos_menos_vendidos(fecha_inicio, fecha_fin)