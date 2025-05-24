from src.clase_base import Producto


# Clase que representa un producto perecible, hereda de Producto
class ProductoPerecible(Producto):
    def __init__(self, codigo, nombre, descripcion, costo, precio, stock, dias_para_caducar):
        # Llama al constructor de la clase base para inicializar los atributos comunes
        super().__init__(codigo, nombre, descripcion, costo, precio, stock)

        # Verifica que dias_para_caducar sea un entero positivo
        if isinstance(dias_para_caducar, int) and dias_para_caducar >= 0:
            self.dias_para_caducar = dias_para_caducar
        else:
            raise ValueError("dias_para_caducar debe ser un entero positivo")

    def verificarEstado(self):
        # Verifica si el producto esta caducado o todavia vigente
        if self.dias_para_caducar == 0:
            return f"Producto {self.nombre} esta CADUCADO."
        else:
            return f"Producto {self.nombre} esta vigente. Quedan {self.dias_para_caducar} dias para caducar."

    def pasar_dia(self):
        # Simula el paso de un dia reduciendo en uno los dias restantes para caducar
        if self.dias_para_caducar > 0:
            self.dias_para_caducar -= 1

    def __str__(self):
        # Devuelve una representacion en cadena del producto, incluyendo los dias para caducar
        return super().__str__() + f" | Dias para caducar: {self.dias_para_caducar}"
