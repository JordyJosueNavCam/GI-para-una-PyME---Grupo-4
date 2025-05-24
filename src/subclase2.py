from src.clase_base import Producto

# Clase que representa un producto no perecible, hereda de Producto
class ProductoNoPerecible(Producto):
    def verificarEstado(self):
        # Metodo que indica que el producto no tiene fecha de caducidad
        return f"Producto {self.nombre} no perecible, sin fecha de caducidad."
