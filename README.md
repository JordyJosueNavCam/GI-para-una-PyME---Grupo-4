# Sistema de Gestión de Inventario para una PyME

**Proyecto del Primer Parcial – Programación Orientada a Objetos**  
**Carrera:** Gestión de la Información Gerencial  
**Materia:** Programación Orientada a Objetos  

---

## Integrantes del Grupo 4

- Zury Luisana Gómez Mendoza  
- Jordy Josué Navarrete Camba  
- Rebeca Sarai Pinto Mejía  
- Luis Enrique Ramírez Quinde  
- José Joel Santillán Troya  

---

## Descripción del Proyecto

El *Sistema de Gestión de Inventario para una PyME* es una aplicación desarrollada para administrar de manera eficiente el inventario de pequeñas y medianas empresas.

Este sistema permite gestionar productos clasificados en *perecibles* y *no perecibles*, administrar proveedores y controlar el stock disponible. Además, incorpora una simulación del paso del tiempo que actualiza el estado de los productos perecibles, facilitando la identificación oportuna de productos caducados.

El proyecto está basado en los principios fundamentales de la *Programación Orientada a Objetos (POO)*, tales como:

- **Encapsulamiento:** Atributos sensibles como costos y stock son protegidos mediante métodos `getters` y `setters`.
- **Herencia:** Productos especializados se derivan de una clase base común.
- **Polimorfismo:** Uso del método `verificarEstado()` redefinido para determinar el estado según el tipo de producto.

El diseño modular del sistema favorece la escalabilidad y facilita futuras mejoras como integración con bases de datos o interfaces gráficas.

---

## Funcionalidades Principales

- Registro y listado de productos.
- Clasificación de productos en perecibles y no perecibles.
- Gestión dinámica del stock: agregar y descontar unidades.
- Verificación del estado de vigencia o caducidad de los productos.
- Registro y administración de proveedores.
- Simulación del paso del tiempo para actualizar productos perecibles.

---

## Diseño del Sistema

| Clase                  | Descripción |
|------------------------|-------------|
| `Producto`             | Clase base que define atributos comunes como código, nombre, descripción, precio, stock y costo (encapsulado). |
| `ProductoPerecible`    | Subclase que incluye fecha de caducidad y redefine `verificarEstado()` para determinar si el producto está vigente o caducado. |
| `ProductoNoPerecible`  | Subclase para productos sin fecha de vencimiento. Implementa su propia versión de `verificarEstado()`. |
| `Proveedor`            | Clase que representa a los proveedores, con atributos como ID, nombre, teléfono y correo. |
| `Inventario`           | Clase contenedora que permite registrar productos/proveedores, modificar el stock y simular el paso del tiempo. |

---

## Estructura del Proyecto y Descripción de Archivos

El presente proyecto está organizado en dos niveles principales: los archivos ejecutables ubicados en la raíz del repositorio y el código fuente contenido en la carpeta `src/`. Esta estructura facilita la separación entre los componentes de ejecución y las definiciones modulares de la lógica del sistema.

### Archivos en la raíz del proyecto

| Archivo       | Descripción                                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------|
| `main.py`     | Archivo principal que funciona como punto de entrada del sistema. Gestiona la interacción con el usuario y coordina las funcionalidades implementadas. |
| `README.md`   | Documento descriptivo que presenta el proyecto, detalla su estructura, funcionalidades y orienta sobre su uso. |

### Módulos contenidos en la carpeta `src/`

| Archivo               | Descripción                                                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `src/clase_base.py`   | Define la clase base que contiene atributos y métodos comunes aplicables a todos los tipos de productos gestionados.           |
| `src/subclase1.py`    | Implementa la subclase para productos perecibles, integrando el manejo de la fecha de caducidad y lógica específica asociada.  |
| `src/subclase2.py`    | Contiene la subclase destinada a productos no perecibles, gestionando características propias de este tipo de artículos.       |
| `src/proveedor.py`    | Gestiona la representación de los proveedores, incluyendo su identificación, información de contacto y otros datos relevantes. |
| `src/inventario.py`   | Administra la gestión integral del inventario, permitiendo la incorporación, consulta y actualización de productos y proveedores. |

---

## El proyecto está organizado de la siguiente manera:

```
GI-para-una-PyME---Grupo-4/
├── src/
│   ├── clase_base.py
│   ├── inventario.py
│   ├── proveedor.py
│   ├── subclase1.py
│   └── subclase2.py
├── main.py
└── README.md
```

---

## Uso

Para utilizar el *Sistema de Gestión de Inventario para una PyME*, abra el proyecto en un entorno de desarrollo como **PyCharm** y ejecute el archivo `main.py` desde la raíz del repositorio.

Esto iniciará una interfaz de consola interactiva que permite:

- Registrar y listar productos perecibles y no perecibles.  
- Administrar proveedores.  
- Controlar el stock disponible.  
- Simular el paso del tiempo para actualizar el estado de los productos perecibles.

Asegúrese de que la estructura del proyecto se mantenga intacta para evitar errores de importación entre los módulos contenidos en la carpeta `src/`.

---

### Ejemplo de Ejecución

Al ejecutar el archivo principal `main.py`, el sistema inicia cargando automáticamente los datos iniciales de proveedores y productos, mostrando en la consola una confirmación detallada por cada elemento agregado:

![Captura de pantalla 2025-05-25 131157](https://github.com/user-attachments/assets/a4566e60-5b69-40ec-bb65-27681ee98dac)

Posteriormente, se despliega el menú principal del sistema, que ofrece al usuario las siguientes opciones para la gestión integral del inventario:

![Captura de pantalla 2025-05-25 131124](https://github.com/user-attachments/assets/dc7d6ee9-6c59-454e-b9ef-f9a945bbe00d)

---

### Ejemplo de Ejecución (continuación)

A continuación se describen las principales funcionalidades que el usuario puede ejecutar a través del menú, ejemplificando su uso:

#### 1. Listar productos

Al seleccionar esta opción, el sistema muestra un listado detallado de todos los productos registrados en el inventario, incluyendo información relevante como código, nombre, descripción, precio, stock disponible y estado (vigente o caducado para productos perecibles).

Ejemplo de salida:

![Captura de pantalla 2025-05-25 134250](https://github.com/user-attachments/assets/43fc3b72-8b85-4b80-aee8-0407652b0205)



#### 2. Listar proveedores

Esta opción presenta un listado de todos los proveedores registrados, mostrando sus datos de identificación, nombre, teléfono y correo electrónico.

Ejemplo de salida:

![Captura de pantalla 2025-05-25 134434](https://github.com/user-attachments/assets/510f7b35-ee84-477c-97a1-1e798c998707)



#### 3. Agregar stock a un producto

Permite aumentar la cantidad de unidades disponibles de un producto específico. El usuario debe ingresar el código del producto y la cantidad a agregar.

Ejemplo:

![Captura de pantalla 2025-05-25 134652](https://github.com/user-attachments/assets/06e8ddd2-1f15-4224-bdf6-4aae67eb31f5)



#### 4. Descontar stock de un producto

Permite reducir la cantidad de unidades disponibles de un producto, simulando ventas o consumo. Se solicita el código y la cantidad a descontar, validando que el stock no quede negativo.

Ejemplo:

![Captura de pantalla 2025-05-25 134833](https://github.com/user-attachments/assets/33dcb002-3782-4a3c-990c-4040b6a6220d)



#### 5. Verificar estado de productos

Ejecuta la evaluación del estado de todos los productos, especialmente los perecibles, para identificar si están vigentes o caducados según la fecha actual y la fecha de caducidad.

Ejemplo de salida:

![Captura de pantalla 2025-05-25 134953](https://github.com/user-attachments/assets/3826db25-10a9-4f4a-bd4e-cf6c328c42c7)



#### 6. Simular paso de un día

Esta función simula el avance de un día en el sistema, actualizando las fechas y estados de los productos perecibles, permitiendo así la gestión temporal del inventario.

Al ejecutarla, el sistema confirma la simulación:

![Captura de pantalla 2025-05-25 135146](https://github.com/user-attachments/assets/2c775440-8cdf-4732-b9a4-604649500267)

![Captura de pantalla 2025-05-25 135218](https://github.com/user-attachments/assets/14c41c4a-2fa6-426a-81cb-9f08f38ab178)



#### 7. Salir

Finaliza la ejecución del programa de manera ordenada.

![Captura de pantalla 2025-05-25 135325](https://github.com/user-attachments/assets/edf9c61d-60d3-4ea3-8444-9687f4a9c2e5)




Con esta estructura interactiva, el sistema facilita la gestión eficiente y controlada del inventario, adecuándose a las necesidades de una pequeña o mediana empresa.

---

## Requisitos

Para ejecutar el sistema, asegúrate de tener instaladas las siguientes dependencias y configuraciones:

- **Python 3.8** o superior.
- No requiere librerías externas adicionales.
- Sistema operativo compatible: Windows, Linux o macOS.
- Acceso a consola o terminal para ejecutar el archivo `main.py`.

---

## Herramientas Utilizadas

- **IDE:** PyCharm Community Edition 2024 (o la versión utilizada).
- **Lenguaje de programación:** Python 3.8 o superior.
- **Control de versiones:** Git (opcional).
- **Sistema operativo de desarrollo:** Windows / Linux / macOS.

---

## Agradecimientos

Agradecemos a nuestro docente de Programación Orientada a Objetos por guiarnos en el desarrollo de este proyecto, el cual nos permitió aplicar conceptos clave de la programación modular, la orientación a objetos y la gestión estructurada de sistemas.

También agradecemos a cada integrante del Grupo 4 por su compromiso y colaboración activa en cada etapa del trabajo.

---

**Gracias por visitar nuestro repositorio.**










