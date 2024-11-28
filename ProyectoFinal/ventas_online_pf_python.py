import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Conexión
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="usuario",
            password="contraseña",
            database="plataforma_ventas"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
            return conexion
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

# Manejo de cierre de la conexión
def cerrar_conexion(conexion, cursor):
    try:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
            print("Conexión cerrada correctamente.")
    except Error as e:
        print(f"Error al cerrar la conexión: {e}")

# Adicion de productos
def agregar_producto(cursor, conexion, nombre, categoria, precio, stock):
    try:
        sql = """
            INSERT INTO Productos (nombre, categoria, precio, stock)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nombre, categoria, precio, stock)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Producto agregado con éxito.")
    except Error as e:
        print(f"Error al agregar el producto: {e}")

# Listar productos
def listar_productos(cursor):
    try:
        cursor.execute("SELECT * FROM Productos")
        resultados = cursor.fetchall()
        if not resultados:
            print("No hay productos registrados.")
            return
        print("\n--- Lista de Productos ---")
        for producto in resultados:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: {producto[3]}, Stock: {producto[4]}")
    except Error as e:
        print(f"Error al listar los productos: {e}")

# Registro de orden
def registrar_orden(cursor, conexion, id_cliente, id_producto, cantidad):
    try:
        cursor.execute("SELECT stock FROM Productos WHERE id_producto = %s", (id_producto,))
        stock_actual = cursor.fetchone()[0]
        if stock_actual < cantidad:
            print("No hay suficiente stock para realizar la orden.")
            return

        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO Ordenes (id_cliente, fecha) VALUES (%s, %s)", (id_cliente, fecha))
        id_orden = cursor.lastrowid

        cursor.execute("""
            INSERT INTO DetalleOrden (id_orden, id_producto, cantidad, precio_unitario)
            VALUES (%s, %s, %s, (SELECT precio FROM Productos WHERE id_producto = %s))
        """, (id_orden, id_producto, cantidad, id_producto))

        cursor.execute("UPDATE Productos SET stock = stock - %s WHERE id_producto = %s", (cantidad, id_producto))

        conexion.commit()
        print("Orden registrada con éxito.")
    except Error as e:
        print(f"Error al registrar la orden: {e}")
        conexion.rollback()

# Actualizar cliente
def actualizar_cliente(cursor, conexion, id_cliente, nombre, email, direccion):
    try:
        sql = """
            UPDATE Clientes
            SET nombre=%s, email=%s, direccion=%s
            WHERE id_cliente=%s
        """
        valores = (nombre, email, direccion, id_cliente)
        cursor.execute(sql, valores)
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró el cliente con el ID especificado.")
        else:
            print("Cliente actualizado con éxito.")
    except Error as e:
        print(f"Error al actualizar el cliente: {e}")

# Eliminar producto
def eliminar_producto(cursor, conexion, id_producto):
    try:
        sql = "DELETE FROM Productos WHERE id_producto=%s"
        cursor.execute(sql, (id_producto,))
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró el producto con el ID especificado.")
        else:
            print("Producto eliminado con éxito.")
    except Error as e:
        print(f"Error al eliminar el producto: {e}")

def menu_principal():
    conexion = crear_conexion()
    if conexion is None:
        return

    cursor = conexion.cursor()
    
    try:
        while True:
            print("\n--- Menú Principal ---")
            print("1. Gestión de Productos")
            print("2. Gestión de Clientes")
            print("3. Procesamiento de Órdenes")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                menu_productos(cursor, conexion)
            elif opcion == '2':
                menu_clientes(cursor, conexion)
            elif opcion == '3':
                menu_ordenes(cursor, conexion)
            elif opcion == '4':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")
    finally:
        cerrar_conexion(conexion, cursor)

if __name__ == "__main__":
    menu_principal()
