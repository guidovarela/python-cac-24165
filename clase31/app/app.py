from flask import Flask, render_template
from data import *
from db import obtenerProductos
from datetime import date, datetime

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

@app.route("/tienda")
def cargarTienda():
    title = "Tienda CaC"
    productos = obtenerProductos()
    return render_template("tienda.html", title=basicInfo(title), productos=productos)

@app.route("/contacto")
def contacto():
    title = "Contacto"
    return render_template("contacto.html", title=basicInfo(title))