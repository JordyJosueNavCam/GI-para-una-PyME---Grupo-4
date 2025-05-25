"""
GI-para-una-PyME---Grupo-4
Integrantes:
1. Gómez Mendoza Zury Luisana
2. Navarrete Camba Jordy Josué
3. Pinto Mejía Rebeca Sarai
4. Ramírez Quinde Luis Enrique
5. Santillán Troya José Joel
"""

from src.clase_base import Producto
# Clase que representa un producto no perecible, hereda de Producto
class ProductoNoPerecible(Producto):
    def verificarEstado(self):
        # Metodo que indica que el producto no tiene fecha de caducidad
        return f"Producto {self.nombre} no perecible, sin fecha de caducidad."
if __name__ == "__main__":
    # Crear un producto no perecible de ejemplo: Arroz Diana
    arroz = ProductoNoPerecible(3003, "Arroz Diana",
                                "Bolsa de arroz Diana, calidad premium, 5kg",
                                2.50, 4.00, 150)
    # Mostrar la informacion del producto
    print(arroz)
    # Verificar el estado del producto (no tiene fecha de caducidad)
    print(arroz.verificarEstado())
    # Agregar stock al producto
    arroz.actualizar_stock(25)
    # Descontar stock del producto
    arroz.actualizar_stock(-50)
    # Intentar descontar mas de lo disponible
    arroz.actualizar_stock(-200)
