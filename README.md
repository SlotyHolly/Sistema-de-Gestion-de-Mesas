# Sistema de Gestion de Mesas

Este proyecto es un **Sistema de Gestión de Mesas** desarrollado en **Python 3.11** con **Tkinter** para la interfaz gráfica de usuario (GUI) y **JSON** como base de datos para almacenar la información de usuarios y eventos. El sistema permite la gestión de eventos para **usuarios** y **administradores**, con funciones de autenticación, compra de tickets y manejo de eventos.

## Características principales
  
- **Dashboard del Mesero**:
  - Los Meseros pueden actualizar los pedidos de las mesas que tienen asignadas.
  - Visualización de las mesas administradas.
  
- **Dashboard del Gerente**:
  - Los Gerentes pueden cargar nuevos eventos.
  - Los Gerentes pueden modificar los eventos existentes.
  
- **Recuperación de Contraseña**:
  - Los usuarios pueden recuperar su contraseña mediante un código predefinido ("1234").
  - Validación del código y cambio de contraseña.

## Tecnologías usadas
- ``Python 3.11``: Lenguaje de programación principal.
- ``Flask``: Biblioteca utilizada para levantar el servicio web
- ``Jinja2``: Jinja2 para generar plantillas HTML dinámicas.
- ``Vercel``: Para el deploy en CLOUD.
- ``PosgresSQL``: Para el manejo de las tablas.

## Estructura del proyecto

El proyecto sigue la siguiente estructura de carpetas:

```
Sistema-de-Gestion-de-Mesas/
│
├── app.py                # Punto de entrada de la aplicación Flask
├── config.py             # Configuración de la app y base de datos
├── requirements.txt      # Dependencias del proyecto (Flask, psycopg2, etc.)
├── /models               # Definición de los modelos ORM (SQLAlchemy)
│   ├── __init__.py
│   ├── employee.py
│   ├── product.py
│   └── order.py
└── /routes               # Rutas o controladores (endpoints Flask)
    ├── __init__.py
    ├── employee_routes.py
    ├── order_routes.py
    └── product_routes.py
```

## Diseño de la Base de Datos (PostgreSQL)

```
+-------------------+          +---------------------+           +-------------------+
|   Employees       |          |     Products        |           |      Orders       |
|-------------------|          |---------------------|           |-------------------|
| id (PK)           |<------.  | id (PK)             |       .-->| id (PK)           |
| name              |       |  | name                |       |   | table_number      |
| role              |       |  | category            |       |   | status            |
+-------------------+       |  | price               |       |   | employee_id (FK)  |
                            |  +---------------------+       |   +-------------------+
                            |                                |
                            |                                |
                            |                                |
                            |     +-----------------------+  |
                            |     |     OrderItems        |  |
                            |     |-----------------------|  |
                            |     | id (PK)               |  |
                            |     | order_id (FK)         |--+
                            +-----| product_id (FK)       |
                                  | quantity              |
                                  +-----------------------+
```

## **Diseño de la Base de Datos (PostgreSQL)**
### **Tablas principales:**

1. **Employees (Empleados)**

- ``id``: Primary Key
- ``name``: Nombre del empleado
- ``role``: Cargo (mesero, cocinero, etc.)

2. **Products (Productos)**

- ``id``: Primary Key
- ``name``: Nombre del producto
- ``category``: Comida o Bebida
- ``price``: Precio

3. **Orders (Pedidos)**

- ``id``: Primary Key
- ``table_number``: Número de la mesa
- ``status``: Estado del pedido (pendiente, en preparación, servido)
- ``employee_id``: Foreign Key -> Employees

4. **OrderItems (Detalle del pedido)**

- ``id``: Primary Key
- ``order_id``: Foreign Key -> Orders
- ``product_id``: Foreign Key -> Products
- ``quantity``: Cantidad


### Descripción de las Relaciones
1. **Employees → Orders:**

- Un empleado puede tener varios pedidos asignados (relación uno a muchos).
- En la tabla Orders, la columna employee_id es una clave foránea (FK) que referencia a la tabla Employees.

2. **Orders → OrderItems:**

- Un pedido puede tener varios productos asociados (relación uno a muchos).
- La columna order_id en OrderItems es una clave foránea (FK) que referencia a la tabla Orders.

3. **Products → OrderItems:**

- Un producto puede aparecer en varios pedidos (relación muchos a muchos).
- Esta relación se descompone en una tabla intermedia OrderItems con las columnas order_id y product_id como claves foráneas.
