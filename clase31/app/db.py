# instalar pymysql -> pip install pymysql
# importar pymysql / SQLachemy / dbmysql
import pymysql

# conectar con el servidro MySQL
def conectarMySQL():
    # datos sencibles -> variables de entorno
    # local
    # host="localhost"
    # user="root"
    # clave=""
    # db="tienda-py"
    
    # deploy -> Pythonanywhere
    host="guidovarela.mysql.pythonanywhere-services.com"
    user="guidovarela"
    clave="codo2024"
    db="guidovarela$tienda-py"


    return pymysql.connect(host=host,user=user,password=clave,database=db)