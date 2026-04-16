from modules.utils import cargarDatos, guardarDatos, inputNoVacio

ruta = "data/clientes.json"

def existeCedula(clientes, cedula):
    return any(c["cedula"] == cedula for c in clientes)

def emailValido(email):
    return "@" in email and "." in email

def crearCliente():
    clientes = cargarDatos(ruta)

    while True:
        cedula = inputNoVacio("Ingresa la cedula del cliente: ")
        if existeCedula(clientes, cedula):
            print("Ya existe un cliente con esa cedula")
        else:
            break

    nombre = inputNoVacio("Ingresa el nombre del cliente: ")
    telefono = inputNoVacio("Ingresa el telefono del cliente: ")
    
    while True:
        email = inputNoVacio("Ingresa el email del cliente: ")
        if not emailValido(email):
            print("Email inválido (debe contener @ y .)")
        else:
            break

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

    clientes.append(cliente)
    guardarDatos(ruta, clientes)

    print("Se ha creado el cliente correctamente")


def verClientes():
    clientes = cargarDatos(ruta)

    if not clientes:
        print("No hay clientes registrados")
        return

    print("LISTA DE CLIENTES: \n")
    print(f"{'CEDULA':<15}{'NOMBRE':<20}{'TELEFONO':<15}{'EMAIL':<25}")
    print("-"*110)

    for c in clientes:
        print(f"{c['cedula']:<15}{c['nombre']:<20}{c['telefono']:<15}{c['email']:<25}")

    print("-"*110)