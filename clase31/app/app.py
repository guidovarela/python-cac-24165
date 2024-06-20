from flask import Flask, render_template
from data import *

app = Flask(__name__)

# home -> root
@app.route("/")
def hello_world():
    saludo = "Hola Mundo!"
    title="Home"
    # return saludo
    return render_template("index.html",saludo=saludo,title=title)

@app.route('/contacto')
def cargarContacto():
    title = "Contacto"

    users = ["Marcelo","Emanuel","Stephanie","Miguel","Marisa","Julian"]

    # return f"<div style='color:tomato'>{title}<div>"
    return render_template("contacto.html", title=title,users=users,personas=personas)