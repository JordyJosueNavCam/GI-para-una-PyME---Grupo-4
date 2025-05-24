from src.inventario import Inventario
from src.proveedor import Proveedor
from src.subclase1 import ProductoPerecible
from src.subclase2 import ProductoNoPerecible

# Funcion que muestra el menu de opciones al usuario
def menu():
    print("""
=== Sistema de Gestion de Inventario ===
1. Listar productos
2. Listar proveedores
3. Agregar stock a un producto
4. Descontar stock de un producto
5. Verificar estado de productos
6. Simular paso de un dia
7. Salir
""")

# Punto de entrada del programa
if __name__ == "__main__":
    # Crear una instancia de Inventario
    inventario = Inventario()

    # Crear y agregar proveedores al inventario
    p1 = Proveedor(1, "Corporacion Favorita", "0998765432", "contacto@favorita.com.ec")
    p2 = Proveedor(2, "Nacional Galletas", "0981234567", "ventas@nacionalgalletas.com.ec")
    inventario.agregar_proveedor(p1)
    inventario.agregar_proveedor(p2)

    # Crear y agregar productos al inventario
    aceite = ProductoNoPerecible(3001, "Aceite La Favorita",
                                 "Aceite de soya refinado en botella de 1 litro",
                                 1.20, 2.00, 200)
    galletas = ProductoNoPerecible(3002, "Galletas Festival",
                                   "Paquete de galletas tradicionales Festival 150g",
                                   0.50, 0.85, 300)
    arroz = ProductoNoPerecible(3003, "Arroz Diana",
                                "Bolsa de arroz Diana, calidad premium, 5kg",
                                2.50, 4.00, 150)
    leche = ProductoPerecible(3004, "Leche Toni Pasteurizada",
                              "Leche fresca pasteurizada en envase de 1 litro",
                              0.90, 1.50, 100, 7)
    queso = ProductoNoPerecible(3005, "Queso Manaba",
                                "Queso fresco tradicional Manaba, 500g",
                                1.80, 2.80, 75)

    inventario.agregar_producto(aceite)
    inventario.agregar_producto(galletas)
    inventario.agregar_producto(arroz)
    inventario.agregar_producto(leche)
    inventario.agregar_producto(queso)

    # Bucle principal del menu
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            # Listar todos los productos registrados
            inventario.listar_productos()
        elif opcion == "2":
            # Listar todos los proveedores registrados
            inventario.listar_proveedores()
        elif opcion == "3":
            # Agregar stock a un producto existente
            try:
                codigo = int(input("Ingrese codigo del producto: "))
                cantidad = int(input("Ingrese cantidad a agregar: "))
                inventario.actualizar_stock(codigo, cantidad)
            except ValueError:
                print("Entrada invalida, ingrese numeros enteros.")
        elif opcion == "4":
            # Descontar stock de un producto existente
            try:
                codigo = int(input("Ingrese codigo del producto: "))
                cantidad = int(input("Ingrese cantidad a descontar: "))
                inventario.actualizar_stock(codigo, -cantidad)
            except ValueError:
                print("Entrada invalida, ingrese numeros enteros.")
        elif opcion == "5":
            # Verificar estado actual de los productos
            inventario.verificar_estado_productos()
        elif opcion == "6":
            # Simular paso de un dia para productos perecibles
            inventario.pasar_dia()
            print("Se ha simulado el paso de un dia para todos los productos perecibles.")
        elif opcion == "7":
            # Salir del programa
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            # Opcion no reconocida
            print("Opcion no valida. Intente nuevamente.")
