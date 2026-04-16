from modules.utils import cargarDatos
import csv

rutaFacturas = "data/facturas.json"

def generarReporte():
    facturas = cargarDatos(rutaFacturas)

    if not facturas:
        print("No hay facturas registradas")
        return

    fechaBusqueda = input("Ingrese la fecha: ")
    print("-"*110)

    facturasFiltradas = [f for f in facturas if f["fecha"].startswith(fechaBusqueda)]

    if not facturasFiltradas:
        print("No hay ventas en esa fecha")
        return

    totalBrutoGeneral = 0
    totalIvaGeneral = 0
    totalGeneral = 0

    print("\nREPORTE DE VENTAS\n")
    print(f"Fecha: {fechaBusqueda}")
    print(f"{'MESA':<12}{'CANT':<8}{'BRUTO':<15}{'IVA':<15}{'TOTAL':<15}")
    print("-"*110)

    filas = []

    for factura in facturasFiltradas:
        mesa = factura["mesa"]["nombre"]

        totalCantidad = sum(item["cantidad"] for item in factura["productos"])

        subtotalBruto = sum(item["precio"] * item["cantidad"] for item in factura["productos"])

        subtotalIVA = sum((item["precio"] * item["cantidad"]) * (item["iva"] / 100) for item in factura["productos"])

        subtotal = factura["total"]

        totalBrutoGeneral += subtotalBruto
        totalIvaGeneral += subtotalIVA
        totalGeneral += subtotal

        print(f"{mesa:<12}{totalCantidad:<8}{subtotalBruto:<15.2f}{subtotalIVA:<15.2f}{subtotal:<15.2f}")

        filas.append([mesa,totalCantidad,f"{subtotalBruto:.2f}",f"{subtotalIVA:.2f}",f"{subtotal:.2f}"])

    print("-"*65)
    print(f"{'TOTAL':<12}{'':<8}{totalBrutoGeneral:<15.2f}{totalIvaGeneral:<15.2f}{totalGeneral:<15.2f}")

    opcion = input("¿Desea exportar a CSV? (s/n): ")

    if opcion.lower() == "s":
        with open("reporte.csv", "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo, delimiter=",")

            writer.writerow(["Mesa", "Cantidad", "Subtotal", "IVA", "Total"])

            for fila in filas:
                writer.writerow(fila)

            writer.writerow(["TOTAL","",f"{totalBrutoGeneral:.2f}",f"{totalIvaGeneral:.2f}",f"{totalGeneral:.2f}"])

        print("Reporte exportado con éxito")

