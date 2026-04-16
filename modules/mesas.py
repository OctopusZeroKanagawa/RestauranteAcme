from modules.utils import cargarDatos, guardarDatos
ruta = "data/mesas.json"

def crearMesa():
    mesas = cargarDatos(ruta)
    codigo = input("Ingresa el codigo de la mesa: ")
    nombre = input("Ingresa el nombre de la mesa: ")
    puestos = input("Ingresa la cantidad de sillas de la mesa: ")
    
    mesa = {
        "codigo": codigo,
        "nombre": nombre,
        "puestos": puestos,
    }
    
    mesas.append(mesa)
    guardarDatos(ruta, mesas)
    print("Se ha creado la mesa correctamente")

def verMesas():
    mesas = cargarDatos(ruta)
    if not mesas:
        print("No hay mesas registradas")
        return
    for p in mesas:
        print(f"Codigo: {p['codigo']}, Nombre: {p['nombre']}, Sillas disponibles: {p['puestos']}")
