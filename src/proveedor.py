"""
GI-para-una-PyME---Grupo-4
Integrantes:
1. Gómez Mendoza Zury Luisana
2. Navarrete Camba Jordy Josué
3. Pinto Mejía Rebeca Sarai
4. Ramírez Quinde Luis Enrique
5. Santillán Troya José Joel
"""

class Proveedor:
    # Constructor de la clase Proveedor
    def __init__(self, id_proveedor, nombre, telefono, correo):
        # Inicializa los atributos con los datos proporcionados
        self.id_proveedor = id_proveedor  # Identificador unico del proveedor
        self.nombre = nombre              # Nombre del proveedor
        self.telefono = telefono          # Numero de telefono del proveedor
        self.correo = correo              # Correo electronico del proveedor
    def __str__(self):
        # Metodo especial que devuelve una representacion en cadena del objeto
        return f"Proveedor({self.id_proveedor}): {self.nombre} | Tel: {self.telefono} | Email: {self.correo}"
if __name__ == "__main__":
    # Crear instancias de la clase Proveedor
    proveedor1 = Proveedor(1, "Distribuidora La Favorita", "0999999999", "ventas@lafavorita.com")
    proveedor2 = Proveedor(2, "Productos Nacional", "0988888888", "contacto@nacional.com")
    # Mostrar los proveedores creados
    print(proveedor1)
    print(proveedor2)
