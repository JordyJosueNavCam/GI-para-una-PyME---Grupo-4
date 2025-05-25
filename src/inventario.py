"""
GI-para-una-PyME---Grupo-4
Integrantes:
1. Gómez Mendoza Zury Luisana
2. Navarrete Camba Jordy Josué
3. Pinto Mejía Rebeca Sarai
4. Ramírez Quinde Luis Enrique
5. Santillán Troya José Joel
"""

from src.subclase1 import ProductoPerecible
from src.subclase2 import ProductoNoPerecible
from src.proveedor import Proveedor
class Inventario:
    # Metodo constructor que inicializa los diccionarios de productos y proveedores
    def __init__(self):
        self.productos = {}    # Diccionario para almacenar productos por su codigo
        self.proveedores = {} # Diccionario para almacenar proveedores por su ID
    # Metodo para agregar un producto al inventario si no existe ya
    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            print(f"Producto con codigo {producto.codigo} ya existe.")
            return False
        self.productos[producto.codigo] = producto
        print(f"Producto {producto.nombre} agregado al inventario.")
        return True
    # Metodo para eliminar un producto del inventario por su codigo
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            eliminado = self.productos.pop(codigo)
            print(f"Producto {eliminado.nombre} eliminado del inventario.")
            return True
        print(f"No existe producto con codigo {codigo} en el inventario.")
        return False
    # Metodo para buscar un producto por su codigo
    def buscar_producto(self, codigo):
        return self.productos.get(codigo, None)
    # Metodo para actualizar el stock de un producto existente
    def actualizar_stock(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto:
            return producto.actualizar_stock(cantidad)
        print(f"Producto con codigo {codigo} no encontrado.")
        return False
    # Metodo para agregar un proveedor si no existe ya en el sistema
    def agregar_proveedor(self, proveedor):
        if proveedor.id_proveedor in self.proveedores:
            print(f"Proveedor con ID {proveedor.id_proveedor} ya existe.")
            return False
        self.proveedores[proveedor.id_proveedor] = proveedor
        print(f"Proveedor {proveedor.nombre} agregado.")
        return True
    # Metodo para mostrar todos los productos en el inventario
    def listar_productos(self):
        print("\nListado de productos en inventario:")
        for prod in self.productos.values():
            print(prod)
    # Metodo para mostrar todos los proveedores registrados
    def listar_proveedores(self):
        print("\nListado de proveedores:")
        for prov in self.proveedores.values():
            print(prov)
    # Metodo para verificar el estado de cada producto del inventario
    def verificar_estado_productos(self):
        print("\nEstado de productos:")
        for prod in self.productos.values():
            print(prod.verificarEstado())
    # Metodo para simular el paso de un dia en productos perecibles
    def pasar_dia(self):
        for prod in self.productos.values():
            if isinstance(prod, ProductoPerecible):
                prod.pasar_dia()
if __name__ == "__main__":
    # Crear una instancia del inventario
    inventario = Inventario()
    # Crear proveedores de ejemplo
    proveedor1 = Proveedor(1, "Corporacion Favorita", "0998765432", "contacto@favorita.com.ec")
    proveedor2 = Proveedor(2, "Nacional Galletas", "0981234567", "ventas@nacionalgalletas.com.ec")
    # Agregar proveedores al inventario
    inventario.agregar_proveedor(proveedor1)
    inventario.agregar_proveedor(proveedor2)
    # Crear productos de ejemplo (perecible y no perecibles)
    producto1 = ProductoNoPerecible(3001, "Aceite La Favorita",
                                    "Aceite de soya refinado en botella de 1 litro",
                                    1.20, 2.00, 200)
    producto2 = ProductoPerecible(3004, "Leche Toni Pasteurizada",
                                  "Leche fresca pasteurizada en envase de 1 litro",
                                  0.90, 1.50, 100, 7)
    # Agregar productos al inventario
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)
    # Listar productos y proveedores
    inventario.listar_productos()
    inventario.listar_proveedores()
    # Actualizar stock de un producto (agregar y luego descontar)
    inventario.actualizar_stock(3001, 50)
    inventario.actualizar_stock(3001, -30)
    # Verificar el estado de los productos (caducidad)
    inventario.verificar_estado_productos()
    # Simular el paso de un dia
    inventario.pasar_dia()
    print("\nSimulacion de un dia completada.")
    # Verificar estado nuevamente para ver si disminuyeron los dias
    inventario.verificar_estado_productos()
