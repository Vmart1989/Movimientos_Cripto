from datetime import date, datetime
from flask import render_template, request, redirect, url_for, flash
from mov_criptos import app
from mov_criptos.models import *
from mov_criptos.forms import RegistrosForm


@app.route("/")
def index():
    registros = show_all()

    return render_template('index.html', pageTitle='Movimientos', data=registros)


@app.route("/purchase", methods=["GET", "POST",])
def purchase(): 
    if request.method == "GET":
        form = RegistrosForm()
        form.moneda_to.default = 'BTC'
        form.process()
        registros = show_all()
        return render_template("purchase.html", pageTitle="Transacción",
                               dataForm=form, data=registros)
    else:
        form = RegistrosForm(data=request.form)
        moneda_from = form.moneda_from.data
        moneda_to = form.moneda_to.data

        cantidad = form.cantidad_from.data
        exchange = CryptoExchange(moneda_from, moneda_to)
        rate = exchange.getRate()
        cantidad_to = cantidad*rate
        precio_unitario = cantidad/cantidad_to
        crypto_available = cryptos_to(
            cripto=moneda_from) - cryptos_from(cripto=moneda_from)

        def validateForm(form):
            errores = []
            if moneda_from == moneda_to:
                errores.append("Escoja monedas diferentes")
            elif moneda_from != 'BTC' and moneda_to == 'EUR':
                errores.append(
                    f'No puede cambiar {moneda_from } por Euros. Si la tiene, puede cambiarla por otra criptomoneda')
            elif cantidad > crypto_available and moneda_from != 'EUR':
                errores.append(
                    f'La cantidad a cambiar de {moneda_from} debe ser menor o igual a sus fondos disponibles')
                errores.append(
                    f'Actualmente dispone de {format_quantity(crypto_available)} {moneda_from} en su cartera de criptos')
            return errores

        error = validateForm(request.form)
        if error:
            return render_template("purchase.html", pageTitle="Transacción",
                                   dataForm=form, msgError=error)

        if form.calcular.data:
            return render_template("purchase.html", pageTitle="Cálculo de movimiento",
                                   dataForm=form, rate=format_quantity(rate),
                                   cantidad_to=format_quantity(cantidad_to),
                                   precio_unitario=format_quantity(
                                       precio_unitario),
                                   moneda_to=moneda_to, moneda_from=moneda_from,
                                   cantidad=format_quantity(cantidad),
                                   crypto_available=crypto_available)

        if form.validate_on_submit():
            fecha = date.today()
            now = datetime.now()
            hora = now.strftime("%H:%M:%S")
            save([fecha, hora, moneda_from, cantidad,
                 moneda_to, cantidad_to, precio_unitario])
            flash('¡Movimiento registrado con éxito!')
            return redirect(url_for('index'))
        else:
            return render_template("purchase.html", msgError={}, dataForm=form)


@app.route("/status")
def status():
    return render_template("status.html", pageTitle="Estado", invertido=euros_spent(),
                           recuperado=euros_gained(),
                           valorCompraRaw=euros_spent_raw() - euros_gained_raw(),
                           valorCompra=format_quantity(
                               euros_spent_raw() - euros_gained_raw()),
                           valorActual=format_quantity(
                               CryptoSum().get_rate_my_cryptos()),
                           valorActualRaw=CryptoSum().get_rate_my_cryptos())


@app.route("/wallet")
def wallet():
    return render_template("wallet.html", pageTitle="Cartera",
                           ada=format_quantity(
                               cryptos_to('ADA') - cryptos_from(cripto='ADA')),
                           bnb=format_quantity(
                               cryptos_to('BNB') - cryptos_from(cripto='BNB')),
                           btc=format_quantity(
                               cryptos_to('BTC') - cryptos_from(cripto='BTC')),
                           dot=format_quantity(
                               cryptos_to('DOT') - cryptos_from(cripto='DOT')),
                           eth=format_quantity(
                               cryptos_to('ETH') - cryptos_from(cripto='ETH')),
                           matic=format_quantity(
                               cryptos_to('MATIC') - cryptos_from(cripto='MATIC')),
                           sol=format_quantity(
                               cryptos_to('SOL') - cryptos_from(cripto='SOL')),
                           usdt=format_quantity(
                               cryptos_to('USDT') - cryptos_from(cripto='USDT')),
                           xrp=format_quantity(
                               cryptos_to('XRP') - cryptos_from(cripto='XRP')),
                           )
