from datetime import date, datetime
from mov_criptos import app
from flask import render_template, request, redirect, url_for, flash
from mov_criptos.models import *
from mov_criptos.forms import RegistrosForm


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
        cryptoAvailable = CryptosTo(cripto=moneda_from) - CryptosFrom(cripto=moneda_from)
        
        def validateForm(form):
            errores = []
            if moneda_from == moneda_to:
                errores.append("Escoja monedas diferentes")
            elif cantidad > cryptoAvailable and moneda_from != 'EUR':
                errores.append(f'La cantidad a cambiar de {moneda_from} debe ser menor o igual a sus fondos disponibles')
                errores.append(f'Actualmente dispone de {formatQuantity(cryptoAvailable)} {moneda_from} en su cartera de criptos')
            return errores
        
        error = validateForm(request.form)
        if error:
            return render_template("purchase.html", pageTitle = "Transacción", dataForm = form, msgError=error)

        if form.calcular.data:
                return render_template("purchase.html",pageTitle = "Cálculo de movimiento", 
                                       dataForm = form, rate=formatQuantity(rate), 
                                       cantidad_to=formatQuantity(cantidad_to), 
                                       precio_unitario = formatQuantity(precio_unitario), 
                                       moneda_to=moneda_to, moneda_from=moneda_from, 
                                       cantidad=formatQuantity(cantidad), 
                                       cryptoAvailable = cryptoAvailable)

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

@app.route("/wallet")
def wallet():
    return render_template("wallet.html", pageTitle = "Cartera", 
                           ada = formatQuantity(CryptosTo('ADA') - CryptosFrom(cripto='ADA')),
                           bnb = formatQuantity(CryptosTo('BNB') - CryptosFrom(cripto='BNB')),
                           btc = formatQuantity(CryptosTo('BTC') - CryptosFrom(cripto='BTC')),
                           dot = formatQuantity(CryptosTo('DOT') - CryptosFrom(cripto='DOT')),
                           eth = formatQuantity(CryptosTo('ETH') - CryptosFrom(cripto='ETH')),
                           matic = formatQuantity(CryptosTo('MATIC') - CryptosFrom(cripto='MATIC')),
                           sol = formatQuantity(CryptosTo('SOL') - CryptosFrom(cripto='SOL')),
                           usdt = formatQuantity(CryptosTo('USDT') - CryptosFrom(cripto='USDT')),
                           xrp = formatQuantity(CryptosTo('XRP') - CryptosFrom(cripto='XRP')),
                           )
                        
