from flask import Flask, render_template, request, redirect
from data import *
from datetime import date, datetime

from controller_db import *

app = Flask(__name__)


def basicInfo(getTitle):
    #Día actual
    today = date.today()
    #Fecha actual
    now = datetime.now()
    # Seccion
    title = getTitle
    return [title, today.strftime('%Y'), now]

# home -> root
@app.route("/")
def home():
    title="Home"
    # return saludo
    return render_template("index.html",title=basicInfo(title))

@app.route('/staff')
def nosotros():
    title = "Staff"
    # return f"<div style='color:tomato'>{title}<div>"
    return render_template("staff.html", title=basicInfo(title),personas=personas)

@app.route("/staff/<int:id>")
def cargarPersona(id):
    return render_template("persona.html",persona=personas[id], title=basicInfo(None))
@app.route("/contacto")
def contacto():
    title = "Contacto"
    return render_template("contacto.html", title=basicInfo(title))



# tienda
# CRUD
@app.route("/tienda")
def cargarTienda():
    title = "Tienda CaC"
    productos = obtenerProductos()
    return render_template("tienda.html", title=basicInfo(title), productos=productos)

# @app.route('/tienda/<int:id>')
# def cargar_prod_id(id):
#     title="Tienda CaC"
#     prod = obtener_prod_por_id(id)
#     return render_template("producto.html", title=basicInfo(title), producto=prod)

# Insert -> 1) carga el form 
@app.route('/cargar_prod')
def cargaProd():
    title= "Nuevo Producto"
    return render_template("form_nuevo_prod.html",title=basicInfo(title))

# 2) enviar los datos por POST
@app.route("/insertar_producto", methods=['POST'])
def insert_prod():
    print(request.form)
    tit_prod = request.form['nombre']
    desc_prod = request.form['descripcion']
    precio_prod = request.form['precio']
    result = cargar_nuevo_prod(tit_prod,desc_prod,precio_prod)
    print(result)
    return redirect("/tienda")

# Update
@app.route("/editar_producto/<int:id>")
def editar_prod(id):
    title = "Editar Producto"
    prod_por_id = obtener_prod_por_id(id)
    # print(prod_por_id)
    return render_template("form_edit_prod.html", title=basicInfo(title), producto=prod_por_id)

@app.route("/update_producto", methods=['POST'])
def update_prod():
    id_edit = request.form['prod_id']
    nombre_edit = request.form['prod_nombre']
    desc_edit = request.form['prod_descripcion']
    precio_edit = request.form['prod_precio']
    actualizar_prod(nombre_edit,desc_edit,precio_edit,id_edit)
    return redirect("/tienda")

@app.route('/borrar_producto/<int:id>')
def delete_prod(id):
    eliminar_prod(id)
    return redirect("/tienda")