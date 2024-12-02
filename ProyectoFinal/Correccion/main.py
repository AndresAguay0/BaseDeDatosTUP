import mysql.connector
from mysql.connector import Error
from datetime import datetime


try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="usuario",
        password="contraseña",
        database="plataforma_ventas"
    )
    cursor = conexion.cursor()
except Error as e:
    print(f"Error al conectar con la base de datos: {e}")
    exit()


def agregar_producto(nombre, categoria, precio, stock):
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

def listar_productos():
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

def actualizar_producto(id_producto, nombre, categoria, precio, stock):
    try:
        sql = """
            UPDATE Productos
            SET nombre=%s, categoria=%s, precio=%s, stock=%s
            WHERE id_producto=%s
        """
        valores = (nombre, categoria, precio, stock, id_producto)
        cursor.execute(sql, valores)
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró el producto con el ID especificado.")
        else:
            print("Producto actualizado con éxito.")
    except Error as e:
        print(f"Error al actualizar el producto: {e}")

def buscar_productos(filtro=None, categoria=None, precio_min=None, precio_max=None):
    try:
        sql = "SELECT * FROM Productos WHERE 1=1"
        params = []
        
        if filtro:
            sql += " AND (nombre LIKE %s OR categoria LIKE %s)"
            params.extend([f"%{filtro}%", f"%{filtro}%"])
        
        if categoria:
            sql += " AND categoria = %s"
            params.append(categoria)
        
        if precio_min:
            sql += " AND precio >= %s"
            params.append(precio_min)
        
        if precio_max:
            sql += " AND precio <= %s"
            params.append(precio_max)
        
        cursor.execute(sql, params)
        resultados = cursor.fetchall()
        
        for producto in resultados:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: {producto[3]}, Stock: {producto[4]}")
    except Error as e:
        print(f"Error en la búsqueda: {e}")

def eliminar_producto(id_producto):
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


def menu_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Listar Productos")
        print("2. Agregar Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Búsqueda Avanzada de Productos")
        print("6. Reporte de Productos Más Vendidos")
        print("7. Volver al Menú Principal")
        
        try:
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                listar_productos()
            elif opcion == '2':
                try:
                    nombre = input("Nombre del producto: ")
                    categoria = input("Categoría: ")
                    precio = float(input("Precio: "))
                    stock = int(input("Stock: "))
                    agregar_producto(nombre, categoria, precio, stock)
                except ValueError:
                    print("Error: Por favor, ingrese datos válidos.")
            elif opcion == '3':
                try:
                    listar_productos()
                    id_producto = int(input("ID del producto a actualizar: "))
                    nombre = input("Nuevo nombre: ")
                    categoria = input("Nueva categoría: ")
                    precio = float(input("Nuevo precio: "))
                    stock = int(input("Nuevo stock: "))
                    actualizar_producto(id_producto, nombre, categoria, precio, stock)
                except ValueError:
                    print("Error: Por favor, ingrese datos válidos.")
            elif opcion == '4':
                try:
                    listar_productos()
                    id_producto = int(input("ID del producto a eliminar: "))
                    eliminar_producto(id_producto)
                except ValueError:
                    print("Error: Por favor, ingrese un ID válido.")
            elif opcion == '5':
                # Búsqueda Avanzada de Productos
                print("\n--- Búsqueda Avanzada de Productos ---")
                filtro = input("Ingrese término de búsqueda (opcional): ")
                categoria = input("Filtrar por categoría (opcional): ")
                
                try:
                    precio_min = float(input("Precio mínimo (opcional, presione Enter para omitir): ") or 0)
                    precio_max = float(input("Precio máximo (opcional, presione Enter para omitir): ") or float('inf'))
                    
                    buscar_productos(
                        filtro=filtro if filtro else None, 
                        categoria=categoria if categoria else None, 
                        precio_min=precio_min, 
                        precio_max=precio_max
                    )
                except ValueError:
                    print("Error: Por favor, ingrese valores numéricos válidos para los precios.")
            elif opcion == '6':
                # Reporte de Productos Más Vendidos
                reporte_productos_mas_vendidos()
            elif opcion == '7':
                break
            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def agregar_cliente(nombre, email, direccion):
    try:
        sql = "INSERT INTO Clientes (nombre, email, direccion) VALUES (%s, %s, %s)"
        valores = (nombre, email, direccion)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Cliente agregado con éxito.")
    except Error as e:
        print(f"Error al agregar el cliente: {e}")

def listar_clientes():
    try:
        cursor.execute("SELECT * FROM Clientes")
        resultados = cursor.fetchall()
        if not resultados:
            print("No hay clientes registrados.")
            return
        print("\n--- Lista de Clientes ---")
        for cliente in resultados:
            print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Email: {cliente[2]}, Dirección: {cliente[3]}")
    except Error as e:
        print(f"Error al listar los clientes: {e}")

def registrar_orden(id_cliente, id_producto, cantidad):
    try:
        
        cursor.execute("SELECT stock FROM Productos WHERE id_producto = %s", (id_producto,))
        stock = cursor.fetchone()[0]
        
        if cantidad > stock:
            print(f"Error: Cantidad solicitada ({cantidad}) supera el stock disponible ({stock})")
            return
        
        
        sql_orden = "INSERT INTO Ordenes (id_cliente, fecha) VALUES (%s, %s)"
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(sql_orden, (id_cliente, fecha))
        id_orden = cursor.lastrowid
        
        
        cursor.execute("SELECT precio FROM Productos WHERE id_producto = %s", (id_producto,))
        precio = cursor.fetchone()[0]
        
        
        sql_detalle = """
            INSERT INTO DetalleOrden (id_orden, id_producto, cantidad, precio_unitario)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql_detalle, (id_orden, id_producto, cantidad, precio))
        
       
        sql_stock = "UPDATE Productos SET stock = stock - %s WHERE id_producto = %s"
        cursor.execute(sql_stock, (cantidad, id_producto))
        
        conexion.commit()
        print("Orden registrada con éxito.")
    except Error as e:
        conexion.rollback()
        print(f"Error al registrar la orden: {e}")

def actualizar_cliente(id_cliente, nombre, email, direccion):
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

def eliminar_cliente(id_cliente):
    try:
        sql = "DELETE FROM Clientes WHERE id_cliente=%s"
        cursor.execute(sql, (id_cliente,))
        conexion.commit()
        if cursor.rowcount == 0:
            print("No se encontró el cliente con el ID especificado.")
        else:
            print("Cliente eliminado con éxito.")
    except Error as e:
        print(f"Error al eliminar el cliente: {e}")

def listar_ordenes_por_cliente(id_cliente):
    try:
        sql = """
            SELECT o.id_orden, o.fecha, d.id_producto, d.cantidad, d.precio_unitario
            FROM Ordenes o
            JOIN DetalleOrden d ON o.id_orden = d.id_orden
            WHERE o.id_cliente = %s
        """
        cursor.execute(sql, (id_cliente,))
        resultados = cursor.fetchall()
        if not resultados:
            print("No se encontraron órdenes para este cliente.")
            return
        print("\n--- Órdenes del Cliente ---")
        for orden in resultados:
            print(f"ID Orden: {orden[0]}, Fecha: {orden[1]}, Producto: {orden[2]}, "
                  f"Cantidad: {orden[3]}, Precio Unitario: {orden[4]}")
    except Error as e:
        print(f"Error al listar las órdenes del cliente: {e}")
        
def reporte_productos_mas_vendidos():
    try:
        sql = """
        SELECT p.id_producto, p.nombre, SUM(do.cantidad) as total_vendido
        FROM Productos p
        JOIN DetalleOrden do ON p.id_producto = do.id_producto
        GROUP BY p.id_producto, p.nombre
        ORDER BY total_vendido DESC
        LIMIT 5
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        print("\n--- Top 5 Productos Más Vendidos ---")
        for producto in resultados:
            print(f"Producto: {producto[1]}, Total Vendido: {producto[2]}")
    except Error as e:
        print(f"Error generando reporte: {e}")


def menu_clientes():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Listar Clientes")
        print("2. Agregar Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        
        try:
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                listar_clientes()
            elif opcion == '2':
                nombre = input("Nombre: ")
                email = input("Email: ")
                direccion = input("Dirección: ")
                agregar_cliente(nombre, email, direccion)
            elif opcion == '3':
                listar_clientes()
                id_cliente = int(input("ID del cliente a actualizar: "))
                nombre = input("Nuevo nombre: ")
                email = input("Nuevo email: ")
                direccion = input("Nueva dirección: ")
                actualizar_cliente(id_cliente, nombre, email, direccion)
            elif opcion == '4':
                listar_clientes()
                id_cliente = int(input("ID del cliente a eliminar: "))
                eliminar_cliente(id_cliente)
            elif opcion == '5':
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Error: Por favor, ingrese un valor válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def menu_ordenes():
    while True:
        print("\n--- Gestión de Órdenes ---")
        print("1. Registrar Orden")
        print("2. Listar Órdenes por Cliente")
        print("3. Volver al Menú Principal")
        
        try:
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                listar_clientes()
                id_cliente = int(input("ID del cliente: "))
                listar_productos() 
                id_producto = int(input("ID del producto: "))
                cantidad = int(input("Cantidad: "))
                registrar_orden(id_cliente, id_producto, cantidad)
            elif opcion == '2':
                listar_clientes()
                id_cliente = int(input("ID del cliente: "))
                listar_ordenes_por_cliente(id_cliente)
            elif opcion == '3':
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Error: Por favor, ingrese un valor válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Productos")
        print("2. Gestión de Clientes")
        print("3. Procesamiento de Órdenes")
        print("4. Salir")
        
        try:
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                menu_productos()
            elif opcion == '2':
                menu_clientes()
            elif opcion == '3':
                menu_ordenes()
            elif opcion == '4':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")
        except Exception as e:
            print(f"Error inesperado: {e}")


def cerrar_conexion():
    try:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
    except Error as e:
        print(f"Error al cerrar la conexión: {e}")


if __name__ == "__main__":
    try:
        menu_principal()
        menu_productos()
        menu_clientes()
        menu_ordenes()
    finally:
        cerrar_conexion()
