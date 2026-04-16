from modules.utils import cargarDatos, guardarDatos
import datetime

rutaProductos = "data/productos.json"
rutaClientes= "data/clientes.json"
rutaMesas= "data/mesas.json"
rutaFacturas= "data/facturas.json"

def buscarProducto(codigo, productos):
    return next((p for p in productos if p["codigo"] == codigo), None)

def buscarCliente(cedula, clientes):
    return next((c for c in clientes if c["cedula"] == cedula), None)

def buscarMesa(codigo, mesas):
    return next((m for m in mesas if m["codigo"] == codigo), None)

def verCarrito(carrito):
    if not carrito:
        print("Carrito vacío")
        return
    
    print("Carrito actual:")
    for item in carrito:
        print(f"Codigo: {item['codigo']}, Producto: {item['nombre']}, Unidades: {item['cantidad']}, IVA:{item['iva']}, Precio: {item['precio']}, Subtotal: {item['subtotal']}")

def agregarProducto(carrito, productos):
    codigo = input("Código del producto: ")
    producto = buscarProducto(codigo, productos)

    if not producto:
        print("Producto no encontrado")
        return

    cantidad = int(input("Cantidad: "))

    subtotal = (producto["precio"] + (((producto["precio"])/100)*producto["iva"])) * cantidad

    item = {
        "codigo": producto["codigo"],
        "nombre": producto["nombre"],
        "cantidad": cantidad,
        "precio": producto["precio"],
        "iva": producto["iva"],
        "subtotal": subtotal
    }

    carrito.append(item)
    print("Producto agregado exitosamente")
    
def facturar():
    print("""Bienvenido al modulo de facturación.
Por favor ingresa los datos solicitados:""")
    productos = cargarDatos(rutaProductos)
    clientes = cargarDatos(rutaClientes)
    mesas = cargarDatos(rutaMesas)
    facturas = cargarDatos(rutaFacturas)

    codMesa = input("Código de mesa: ")
    mesa = buscarMesa(codMesa, mesas)
    if not mesa:
        print("Mesa no encontrada")
        return

    cedulaCliente = input("Cedula del cliente: ")
    cliente = buscarCliente(cedulaCliente, clientes)

    if not cliente:
        print("Cliente no encontrado")
        return

    carrito = []
    
    print("Su factura ha iniciado correctamente")
    
    while True:
        print("""Seleccione la opcion que desee:
    1. Agregar producto
    2. Ver carrito
    3. Finalizar factura
    0. Cancelar
    """)
        opcion = input("Opcion: ")

        match opcion:
            case "1":
                print("-"*110)
                agregarProducto(carrito, productos)
                print("-"*110)

            case "2":
                print("-"*110)
                verCarrito(carrito)
                print("-"*110)

            case "3":
                print("-"*110)
                if not carrito:
                    print("No hay productos")
                    continue

                total = sum(item["subtotal"] for item in carrito)

                factura = {
                    "fecha": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "mesa": mesa,
                    "cliente": cliente,
                    "productos": carrito,
                    "total": total
                }

                facturas.append(factura)
                guardarDatos(rutaFacturas, facturas)

                print("FACTURA")
                print(f"Fecha: {factura['fecha']}")
                print(f"Mesa: {mesa['nombre']}")
                print(f"Cliente: {cliente['nombre']}")
                print("-"*110)
                print("PRODUCTOS")
                print("-"*110)
                print(f"{'COD':<5}{'NOMBRE':<15}{'CANT':<6}{'PRECIO':<10}{'IVA':<8}{'SUBTOTAL':<10}")

                for item in carrito:
                    print(f"{item['codigo']:<5}"
                        f"{item['nombre']:<15}"
                        f"{item['cantidad']:<6}"
                        f"{item['precio']:<10.2f}"
                        f"{item['iva']:<8.2f}"
                        f"{item['subtotal']:<10.2f}")
                print("-"*110)
                print(f"{'TOTAL:':<46}{total:.2f}")
                print("-"*110)
                break

            case "0":
                print("-"*110)
                print("Factura cancelada")
                break

            case _:
                print("-"*110)
                print("Opción inválida")
                print("-"*110)
        