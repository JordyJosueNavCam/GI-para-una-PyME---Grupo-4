class Producto:
    # Metodo constructor que inicializa los atributos del producto
    def __init__(self, codigo, nombre, descripcion, costo, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.__costo = costo  # Atributo encapsulado
        self.precio = precio
        self.stock = stock

    # Metodo getter para obtener el costo del producto
    def get_costo(self):
        return self.__costo

    # Metodo setter para modificar el costo del producto si es un valor positivo
    def set_costo(self, nuevo_costo):
        if nuevo_costo > 0:
            self.__costo = nuevo_costo
        else:
            print("El costo debe ser un valor positivo.")

    # Metodo que devuelve un mensaje generico sobre el estado del producto
    def verificarEstado(self):
        return "Estado no definido para producto generico."

    # Metodo para actualizar el stock del producto segun la cantidad indicada
    def actualizar_stock(self, cantidad):
        if cantidad < 0 and abs(cantidad) > self.stock:
            print(f"No hay suficiente stock para descontar {abs(cantidad)} unidades.")
            return False
        self.stock += cantidad
        print(f"Stock actualizado. Nuevo stock de {self.nombre}: {self.stock}")
        return True

    # Metodo que devuelve una representacion en texto del producto
    def __str__(self):
        return (f"Producto({self.codigo}): {self.nombre} - {self.descripcion} | "
                f"Precio: ${self.precio:.2f} | Stock: {self.stock}")



