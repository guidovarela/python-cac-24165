import pymysql
from db import conectarMySQL


# Read -> SELECT
def obtenerProductos():
    # conexion mysql
    conexion = conectarMySQL()
    productos = []
    with conexion.cursor() as cursor:
        # Create a new record
        sql = """SELECT * FROM productos"""
        cursor.execute(sql)
        productos = cursor.fetchall()
        conexion.commit()
        conexion.close()
        return productos
    
# CRUD -> Create, Read, Update, Delete 

# Create -> Insert
def cargar_nuevo_prod(nombre, descripcion, precio):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        query = "INSERT INTO productos (nombre, descripcion, precio) VALUES (%s, %s, %s)"
        cursor.execute(query,(nombre, descripcion, precio))
        result = cursor
        conexion.commit()
        conexion.close()
        return result
    

# Update 1) ubicar por id el producto a modificar
def obtener_prod_por_id(id):
    conexion = conectarMySQL()
    prod = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM productos WHERE id = %s", (id,))
        prod = cursor.fetchone()
    conexion.close()
    return prod

# 2) realizar el Update en MySQL
def actualizar_prod(nombre, descripcion, precio, id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE productos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",(nombre, descripcion, precio, id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result

# Delete
def eliminar_prod(id):
    conexion = conectarMySQL()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM productos WHERE id = %s", (id))
        result = cursor
    conexion.commit()
    conexion.close()
    return result