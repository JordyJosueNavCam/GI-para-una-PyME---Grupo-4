"""
GI-para-una-PyME---Grupo-4
Integrantes:
1. Gómez Mendoza Zury Luisana
2. Navarrete Camba Jordy Josué
3. Pinto Mejía Rebeca Sarai
4. Ramírez Quinde Luis Enrique
5. Santillán Troya José Joel
"""

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
if __name__ == "__main__":
    # Crear un producto de ejemplo con los datos del producto "Aceite La Favorita"
    aceite = Producto(3001, "Aceite La Favorita",
                      "Aceite de soya refinado en botella de 1 litro",
                      1.20, 2.00, 200)
    # Mostrar la informacion inicial del producto
    print(aceite)
    # Mostrar el costo actual del producto (atributo encapsulado)
    print(f"Costo actual: ${aceite.get_costo()}")
    # Actualizar el costo a un valor valido
    aceite.set_costo(1.50)
    print(f"Costo actualizado: ${aceite.get_costo()}")
    # Intentar actualizar el costo a un valor invalido (negativo)
    aceite.set_costo(-0.50)
    # Agregar stock (sumar 50 unidades)
    aceite.actualizar_stock(50)
    # Intentar descontar mas unidades de las que hay disponibles
    aceite.actualizar_stock(-300)
    # Descontar una cantidad valida del stock (100 unidades)
    aceite.actualizar_stock(-100)
    # Verificar el estado del producto usando el metodo base
    print(aceite.verificarEstado())


