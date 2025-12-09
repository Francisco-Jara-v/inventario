from utils import limpiar
from inventario import agregar_producto, listar_producto, buscar_producto, eliminar_producto

def menu():
    while True:
        print("----------------")
        print("       Menu")
        print("----------------")
        print("1.- Agregar producto")
        print("2.- Listar producto")
        print("3.- Buscar producto")
        print("4.- Eliminar producto")
        print("5.- Salir")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            limpiar()
            print("------------------------------")
            print("       AGREGAR PRODUCTO")
            print("------------------------------")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la Cantidad del producto: "))
            precio_unitario = float(input("Ingrese el valor unitario del producto: $"))
            agregar_producto(nombre, cantidad, precio_unitario)
            print("¡PRODUCTO AGREGADO EXITOSAMENTE!")
            
            
            
            
        elif opcion == "2":
            limpiar()
            producto = listar_producto()
            print("-----------------------------------")
            print("         LISTA DE PRODUCTOS")
            print("-----------------------------------")
            for p in producto:
                print(f"ID: {p['id']} | {p['nombre']} | {p['cantidad']} | {p['precio_unitario']}")
                print("")

        
        elif opcion == "3":
            limpiar()
            busqueda = input("Inserte el nombre del producto que desea buscar: ")
            resultados = buscar_producto(busqueda)
            print("-----------------------------------")
            print("             RESULTADOS")
            print("-----------------------------------")
            for p in resultados:
                print(f"ID: {p['id']} | {p['nombre']} | {p['cantidad']} | {p['precio_unitario']}")
                print("")
                    
        elif opcion == "4":
            limpiar()
            product_id = int(input("Ingrese el ID que desea eliminar: "))
            if eliminar_producto(product_id):
                print("¡PRODUCTO ELIMINADO!.")
                print("")
            else:
                print("No se encontro el Producto")

        elif opcion == "5":
            limpiar()
            print ("Saliendo...")
            break

        else:
            limpiar()
            print("Opcion invalida!")
            

menu()

