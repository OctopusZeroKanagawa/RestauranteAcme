from modules.utils import cargarDatos, guardarDatos, inputNoVacio, inputFloat, inputOpcion
ruta = "data/productos.json"

def existeCodigo(productos, codigo):
    return any(p["codigo"] == codigo for p in productos)

def crearProducto():
    productos = cargarDatos(ruta)

    while True:
        codigo = inputNoVacio("Ingresa el codigo del producto: ")

        if existeCodigo(productos, codigo):
            print("Ya existe un producto con ese código")
        else:
            break

    nombre = inputNoVacio("Ingresa el nombre del producto: ")
    tipo = inputOpcion("Ingresa el tipo del producto (1=comida, 2=bebida, 3=postre): ", ["1", "2", "3"])
    precio = inputFloat("Ingresa el precio del producto: ")
    iva = inputFloat("Ingresa el IVA del producto (%): ")

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "precio": precio,
        "iva": iva
    }

    productos.append(producto)
    guardarDatos(ruta, productos)

    print("Se ha creado el producto correctamente")


def verProductos():
    productos = cargarDatos(ruta)

    if not productos:
        print("No hay productos registrados")
        return

    print("LISTA DE PRODUCTOS: \n")
    print(f"{'COD':<6}{'NOMBRE':<15}{'TIPO':<10}{'PRECIO':<10}{'IVA':<8}")
    print("-"*110)

    for p in productos:
        print(f"{p['codigo']:<6}{p['nombre']:<15}{p['tipo']:<10}{p['precio']:<10.2f}{p['iva']:<8.2f}")
