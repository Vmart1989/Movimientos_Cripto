from datetime import date, datetime
from mov_criptos import app
from flask import render_template, request, redirect, url_for, flash
from mov_criptos.models import *
from mov_criptos.forms import RegistrosForm

@app.route("/")
def index():
    registros = show_all()

    return render_template('index.html', pageTitle = 'Movimientos', data=registros)

@app.route("/purchase",methods=["GET","POST"])
def purchase():
    form = RegistrosForm()
    if request.method == "GET":
        return render_template("purchase.html", pageTitle = "Transacción", dataForm = form)

@app.route("/status")
def status():
    return render_template("status.html", pageTitle = "Estado")