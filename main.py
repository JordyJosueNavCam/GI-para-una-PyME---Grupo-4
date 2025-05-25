"""
GI-para-una-PyME---Grupo-4
Integrantes:
1. Gómez Mendoza Zury Luisana
2. Navarrete Camba Jordy Josué
3. Pinto Mejía Rebeca Sarai
4. Ramírez Quinde Luis Enrique
5. Santillán Troya José Joel
"""

from src.inventario import Inventario
from src.proveedor import Proveedor
from src.subclase1 import ProductoPerecible
from src.subclase2 import ProductoNoPerecible
# Funcion que muestra el menu principal al usuario
def mostrar_menu():
    print("""
========= SISTEMA DE GESTION DE INVENTARIO =========
1. Listar productos
2. Listar proveedores
3. Agregar stock a un producto
4. Descontar stock de un producto
5. Verificar estado de productos
6. Simular paso de un dia
7. Salir
=====================================================
""")
# Punto de entrada principal del programa
if __name__ == "__main__":
    # Crear una instancia del inventario
    inventario = Inventario()
    # Crear instancias de proveedores y agregarlos al inventario
    proveedor1 = Proveedor(1, "Corporacion Favorita", "0998765432", "contacto@favorita.com.ec")
    proveedor2 = Proveedor(2, "Nacional Galletas", "0981234567", "ventas@nacionalgalletas.com.ec")
    inventario.agregar_proveedor(proveedor1)
    inventario.agregar_proveedor(proveedor2)
    # Crear productos de ejemplo (perecibles y no perecibles)
    aceite = ProductoNoPerecible(3001, "Aceite La Favorita", "Aceite de soya refinado - 1L", 1.20, 2.00, 200)
    galletas = ProductoNoPerecible(3002, "Galletas Festival", "Galletas tradicionales 150g", 0.50, 0.85, 300)
    arroz = ProductoNoPerecible(3003, "Arroz Diana", "Bolsa de arroz premium 5kg", 2.50, 4.00, 150)
    leche = ProductoPerecible(3004, "Leche Toni Pasteurizada", "Leche fresca 1L", 0.90, 1.50, 100, 7)
    queso = ProductoNoPerecible(3005, "Queso Manaba", "Queso fresco 500g", 1.80, 2.80, 75)
    # Agregar productos al inventario
    for producto in [aceite, galletas, arroz, leche, queso]:
        inventario.agregar_producto(producto)
    # Bucle principal que muestra el menu hasta que el usuario decida salir
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")
        # Listar todos los productos registrados
        if opcion == "1":
            inventario.listar_productos()
        # Listar todos los proveedores registrados
        elif opcion == "2":
            inventario.listar_proveedores()
        # Agregar unidades al stock de un producto
        elif opcion == "3":
            try:
                codigo = int(input("Ingrese codigo del producto: "))
                cantidad = int(input("Cantidad a agregar: "))
                inventario.actualizar_stock(codigo, cantidad)
            except ValueError:
                print("Entrada invalida. Ingrese valores numericos.")
        # Descontar unidades del stock de un producto
        elif opcion == "4":
            try:
                codigo = int(input("Ingrese codigo del producto: "))
                cantidad = int(input("Cantidad a descontar: "))
                inventario.actualizar_stock(codigo, -cantidad)
            except ValueError:
                print("Entrada invalida. Ingrese valores numericos.")
        # Mostrar el estado actual de cada producto
        elif opcion == "5":
            inventario.verificar_estado_productos()
        # Simular que ha pasado un dia para los productos perecibles
        elif opcion == "6":
            inventario.pasar_dia()
            print("Se ha simulado el paso de un dia en los productos perecibles.")
        # Salir del sistema
        elif opcion == "7":
            print("Saliendo del sistema. Hasta luego.")
            break
        # Opcion no valida
        else:
            print("Opcion no valida. Intente nuevamente.")
