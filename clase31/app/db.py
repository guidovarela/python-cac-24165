
# instalar pymysql -> pip install pymysql
# importar pymysql / SQLachemy / dbmysql

import pymysql

# conectar con el servidro MySQL
def conectarMySQL():
    # datos sencibles -> variables de entorno
    host="localhost"
    user="root"
    clave=""
    db="tienda_py"
    return pymysql.connect(host=host,user=user,password=clave,database=db)

def obtenerProductos():
    # conexion mysql
    conexion = conectarMySQL()
    productos = []
    with conexion.cursor() as cursor:
        # Create a new record
        sql = "SELECT * FROM productos"
    # consulta
        cursor.execute(sql)
        productos = cursor.fetchall()
    # return resultados
        return productos





# CRUD -> Create, Read, Update, Delete 