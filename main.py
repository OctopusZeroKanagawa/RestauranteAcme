import modules.productos as p, modules.clientes as c, modules.mesas as m, modules.facturacion as f, modules.reportes as r

def menu():
    while True:
        print("-"*110)
        print("Bienvenido al resturante ACME")
        print("-"*110)
        print("""Los modulos disponibles son:
    1.Productos
    2.Mesas
    3.Clientes
    4.Facturación
    5.Registro de ventas
    6.Producto más vendido
    0.Salir""")
        modulo = input("Digite el modulo a usar: ")
        print("-"*110)
        
        match modulo:
            case "1":
                while True:
                    print("""Bienvenido al modulo de productos.
Las opciones disponibles son:
    1.Crear Producto
    2.Ver productos disponibles
    0.Regresar al menu principal""")
                    opcion = input("Digite la opción a usar: ")
                    print("-"*110)
                    
                    match opcion:
                        case "1":
                            p.crearProducto()
                            print("-"*110)
                        case "2":
                            p.verProductos()
                            print("-"*110)
                        case "0":
                            break
                        case _:
                            print("Opcion invalida")
                            print("-"*110)
                        
            case "2":
                while True:
                    print("""Bienvenido al modulo de mesas.
Las opciones disponibles son:
    1.Crear Mesa
    2.Ver mesas disponibles
    0.Regresar al menu principal""")
                    opcion = input("Digite la opción a usar: ")
                    print("-"*110)

                    match opcion:
                        case "1":
                            m.crearMesa()
                            print("-"*110)
                        case "2":
                            m.verMesas()
                            print("-"*110)
                        case "0":
                            break
                        case _:
                            print("Opcion invalida")
                            print("-"*110)
                        
            case "3":
                while True:
                    print("""Bienvenido al modulo de clientes.
Las opciones disponibles son:
    1.Crear Cliente
    2.Ver clientes registrados
    0.Regresar al menu principal""")
                    opcion = input("Digite la opción a usar: ")
                    print("-"*110)

                    match opcion:
                        case "1":
                            c.crearCliente()
                            print("-"*110)
                        case "2":
                            c.verClientes()
                            print("-"*110)
                        case "0":
                            break
                        case _:
                            print("Opcion invalida")
                            print("-"*110)
            case "4":
                f.facturar()
            case "5":
                r.generarReporte()
            case "6":
                r.rankingMayorVentas()
            case "0":
                print("Hasta pronto, tenga un buen dia.")
                print("-"*110)
                break
            case _:
                    print("Opcion invalida")
menu ()
