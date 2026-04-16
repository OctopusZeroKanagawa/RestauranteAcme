import json, os
    
def cargarDatos(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r") as archivo:
        contenido = archivo.read().strip()

        if not contenido:
            return []

        return json.loads(contenido)    

def guardarDatos(ruta,datos):
    with open(ruta,"w") as archivo:
        json.dump(datos,archivo, indent=4)

def inputNoVacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Este campo no puede estar vacío")
        else:
            return valor
        
def inputEntero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero válido")

def inputFloat(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Debe ingresar un número decimal válido")

def inputOpcion(mensaje, opcionesValidas):
    while True:
        valor = input(mensaje).strip()
        if valor in opcionesValidas:
            return valor
        else:
            print(f"Opción inválida. Opciones: {', '.join(opcionesValidas)}")
            

