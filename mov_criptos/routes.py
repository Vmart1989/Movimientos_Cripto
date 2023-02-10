from datetime import date, datetime
from mov_criptos import app
from flask import render_template, request, redirect, url_for, flash
from mov_criptos.models import *
from mov_criptos.forms import RegistrosForm, COINS, ValidationError


@app.route("/")
def index():
    registros = show_all()

    return render_template('index.html', pageTitle = 'Movimientos', data=registros)

@app.route("/purchase",methods=["GET","POST",])
def purchase(): 
    if request.method == "GET":
        form = RegistrosForm()
        form.moneda_to.default = 'BTC'
        form.process()
        registros = show_all()
        return render_template("purchase.html", pageTitle = "Transacción", dataForm = form, data=registros)
    else:
        form = RegistrosForm(data=request.form)
        moneda_from = form.moneda_from.data
        moneda_to = form.moneda_to.data
        
        cantidad = form.cantidad_from.data
        exchange = CryptoExchange(moneda_from, moneda_to)
        rate = exchange.getRate()
        cantidad_to = cantidad*rate
        precio_unitario = cantidad/cantidad_to
        monedas_disponibles = showMonedaTo()
        
        def validateForm(form):
            errores = []
            if moneda_from == moneda_to:
                errores.append("Escoja monedas diferentes")
            if moneda_from not in monedas_disponibles:
                errores.append(f'No tiene fondos disponibles de {moneda_from}')
            return errores
        
        error = validateForm(request.form)
        if error:
            return render_template("purchase.html", pageTitle = "Transacción", dataForm = form, msgError=error)

        if form.calcular.data:
                return render_template("purchase.html",pageTitle = "Cálculo de movimiento", dataForm = form, rate=formatQuantity(rate), cantidad_to=formatQuantity(cantidad_to), precio_unitario = formatQuantity(precio_unitario), moneda_to=moneda_to, moneda_from=moneda_from, cantidad=formatQuantity(cantidad))

        if form.validate_on_submit():
            fecha = date.today()
            now = datetime.now()
            hora = now.strftime("%H:%M:%S")
            save([fecha,hora, moneda_from, cantidad, moneda_to, cantidad_to, precio_unitario])
            flash('¡Movimiento registrado con éxito!')
            return redirect(url_for('index'))
        else:
            return render_template("purchase.html", msgError={}, dataForm=form)

@app.route("/status")
def status():
    return render_template("status.html", pageTitle = "Estado", invertido = eurosSpent(), recuperado = eurosGained(), valorCompraRaw = eurosSpentRaw() - eurosGainedRaw(), valorCompra = formatQuantity(eurosSpentRaw() - eurosGainedRaw()), valorActual = formatQuantity(CryptoSum().getRateMyCryptos()), valorActualRaw = CryptoSum().getRateMyCryptos())