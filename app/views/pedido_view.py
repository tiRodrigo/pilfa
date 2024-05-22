from app import app
from flask import render_template
from app.forms import curso_form
from app import db
from app.models import curso_model

@app.route("/cadpedido")
def acompanhar_pedido():
    return render_template("pedido/cad_pedido.html")