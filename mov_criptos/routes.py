from mov_criptos import app
from flask import render_template, request, redirect, url_for, flash

@app.route("/")
def index():
    return render_template('index.html', pageTitle = 'Movimientos')

@app.route("/purchase")
def purchase():
    return render_template("purchase.html", pageTitle = "Compra")

@app.route("/status")
def status():
    return render_template("status.html", pageTitle = "Estado")