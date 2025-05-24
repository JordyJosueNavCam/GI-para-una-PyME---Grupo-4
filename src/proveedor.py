class Proveedor:
    def __init__(self, id_proveedor, nombre, telefono, correo):
        # Constructor de la clase Proveedor
        # Inicializa los atributos con los datos proporcionados
        self.id_proveedor = id_proveedor  # Identificador unico del proveedor
        self.nombre = nombre              # Nombre del proveedor
        self.telefono = telefono          # Numero de telefono del proveedor
        self.correo = correo              # Correo electronico del proveedor

    def __str__(self):
        # Metodo especial que devuelve una representacion en cadena del objeto
        return f"Proveedor({self.id_proveedor}): {self.nombre} | Tel: {self.telefono} | Email: {self.correo}"
