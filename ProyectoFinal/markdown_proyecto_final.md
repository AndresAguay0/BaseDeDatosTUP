# **Sistema de Ventas en Línea**

## **Esquema de Base de Datos**

`PRODUCTOS <id_producto, nombre, categoria, precio, stock> CLIENTES <id_cliente, nombre, email, direccion> ORDENES <id_orden, id_cliente, fecha> DETALLE_ORDEN <id_orden, id_producto, cantidad, precio_unitario>`

## **Restricciones**

*a. Cada producto tiene un código único (id_producto), pero el nombre del producto puede repetirse entre diferentes productos.*

*b. Un cliente puede realizar varias compras (órdenes). Cada cliente tiene un código único (id_cliente).*

*c. Un producto puede ser parte de varias órdenes, y en cada orden puede tener diferentes cantidades.*

*d. Cada orden tiene un identificador único (id_orden), y cada producto en la orden está asociado a un precio unitario.*

*e. El precio unitario de un producto puede cambiar entre diferentes órdenes, pero dentro de una orden se mantiene constante para cada producto.*

## **Determinación de Dependencias Funcionales**

Basándonos en las restricciones, podemos deducir las siguientes dependencias funcionales para las tablas del sistema:

1) **id_producto → nombre, categoria, precio, stock**: Cada producto tiene un código único (id_producto), y los atributos de nombre, categoría, precio y stock dependen de este código.
  
2) **id_cliente → nombre, email, direccion**: Cada cliente tiene un código único (id_cliente), y los atributos de nombre, email y dirección dependen de este código.
  
3) **id_orden → id_cliente, fecha**: Cada orden tiene un código único (id_orden), y la fecha y el cliente asociado dependen de este código.
  
4) **{id_orden, id_producto} → cantidad, precio_unitario**: Cada producto en una orden tiene una cantidad y un precio unitario asociados, dependiendo de la combinación de id_orden e id_producto.

## **Claves Candidatas**

Para identificar las claves candidatas, observamos que:

- En la tabla **PRODUCTOS**, la clave primaria es **id_producto**.
  
- En la tabla **CLIENTES**, la clave primaria es **id_cliente**.

- En la tabla **ORDENES**, la clave primaria es **id_orden**.

- En la tabla **DETALLE_ORDEN**, la clave primaria es la combinación **{id_orden, id_producto}**.

## **Elección de Clave Primaria**

Las claves primarias elegidas son las siguientes:

- En la tabla **PRODUCTOS**, elegimos **id_producto** como clave primaria.
- En la tabla **CLIENTES**, elegimos **id_cliente** como clave primaria.
- En la tabla **ORDENES**, elegimos **id_orden** como clave primaria.
- En la tabla **DETALLE_ORDEN**, elegimos la clave primaria compuesta **{id_orden, id_producto}**.

## **Normalización hasta 3FN**

**1FN**: Las tablas ya están en 1FN, ya que todos los atributos son atómicos.

**2FN**: Para cumplir 2FN, eliminamos dependencias parciales en las claves primarias compuestas. Esto implica que los atributos de cada tabla deben depender completamente de su clave primaria.

**3FN**: Para cumplir con 3FN, eliminamos dependencias transitivas para que los atributos no clave dependan únicamente de la clave primaria.

### **Nuevo Esquema en 3FN**

1) **Tabla Productos**
   - Atributos: `id_producto`, `nombre`, `categoria`, `precio`, `stock`
   - Clave primaria: `id_producto`

2) **Tabla Clientes**
   - Atributos: `id_cliente`, `nombre`, `email`, `direccion`
   - Clave primaria: `id_cliente`

3) **Tabla Ordenes**
   - Atributos: `id_orden`, `id_cliente`, `fecha`
   - Clave primaria: `id_orden`
   - Clave foránea: `id_cliente` (referencia a `Clientes`)

4) **Tabla DetalleOrden**
   - Atributos: `id_orden`, `id_producto`, `cantidad`, `precio_unitario`
   - Clave primaria compuesta: `id_orden`, `id_producto`
   - Claves foráneas:
     - `id_orden` (referencia a `Ordenes`)
     - `id_producto` (referencia a `Productos`)
