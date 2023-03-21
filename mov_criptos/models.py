"""import requests module for making request to API"""
import requests
from config import API_KEY
from mov_criptos.connection import Connection


def show_all():
    """receives data from database 
        returns table filled with data"""
    connect = Connection(
        "SELECT id,date,time,moneda_from,cantidad_from,moneda_to,cantidad_to,precio_unitario from registros order by date DESC, time DESC")
    filas = connect.res.fetchall()
    columnas = connect.res.description

    resultado = []

    for fila in filas:
        dato = {}
        posicion = 0

        for campo in columnas:
            dato[campo[0]] = fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()

    return resultado


def save(registro):
    '''
    receives form data
    saves it to database
    '''
    connect = Connection(
        f"INSERT INTO registros (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, precio_unitario) VALUES(?,?,?,?,?,?,?)", registro)
    connect.con.commit()
    connect.con.close()


def euros_spent():
    '''
    returns amount of euros spent formated to european style and less decimals
    '''
    connect = Connection(
        f"SELECT sum(cantidad_from) FROM Registros WHERE moneda_from = 'EUR'")
    resultado = connect.res.fetchall()
    connect.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = f'{resultado[0][0]:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    return resultado


def euros_spent_raw():
    '''
    returns amount of euros spent with all decimals
    '''
    connect = Connection(
        f"SELECT sum(cantidad_from) FROM Registros WHERE moneda_from = 'EUR'")
    resultado = connect.res.fetchall()
    connect.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado


def euros_gained():
    '''
    returns amount of euros gained formated to european style and less decimals
    '''
    connect = Connection(
        f"SELECT sum(cantidad_to) FROM Registros WHERE moneda_to = 'EUR'")
    resultado = connect.res.fetchall()
    connect.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = f'{resultado[0][0]:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    return resultado


def euros_gained_raw():
    '''
    returns amount of euros gained with all decimals
    '''
    connect = Connection(
        f"SELECT sum(cantidad_to) FROM Registros WHERE moneda_to = 'EUR'")
    resultado = connect.res.fetchall()
    connect.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado


def cryptos_to(cripto):
    '''
    receives crypto as parameter
    returns amount of that crypto in database
    '''
    connect = Connection(
        f"SELECT sum(cantidad_to) FROM Registros WHERE moneda_to = '{cripto}'")
    resultado = connect.res.fetchall()
    connect.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado


def cryptos_from(cripto):
    '''
    receives crypto as parameter
    returns amount of that crypto in database
    '''
    connect = Connection(
        f"SELECT sum(cantidad_from) FROM Registros WHERE moneda_from = '{cripto}'")
    resultado = connect.res.fetchall()
    connect.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado


class CryptoExchange:
    def __init__(self, moneda_from, moneda_to):
        self.moneda_from = moneda_from
        self.moneda_to = moneda_to
        self.rate = 0

    def getRate(self):
        r = requests.get(
            f'https://rest.coinapi.io/v1/exchangerate/{self.moneda_from}/{self.moneda_to}?apikey={API_KEY}')
        resultado = r.json()
        if r.status_code == 200:
            self.rate = resultado['rate']

            return self.rate
        else:
            raise ModelError(
                f"status: {self.r.status_code} error: {self.resultado['error']}")


class CryptoSum:
    def __init__(self):
        pass

    def sum_crypto_to(self):
        """
        receives sum of all criptos purchased in database
        adds to cryptos totals
        """
        connect = Connection(
            f"SELECT sum(cantidad_to), moneda_to FROM Registros GROUP by moneda_to")
        sumact = connect.res.fetchall()
        if sumact != "":
            totales_criptos_to = []
            for suma in sumact:
                if suma[1] != 'EUR':
                    totales_criptos_to.append(suma)
            connect.con.close()
            return totales_criptos_to
        else:
            return 0

    def sum_crypto_from(self):
        """
        receives sum of all criptos spent in database
        adds to cryptos spent totals
        """
        connect = Connection(
            f"SELECT sum(cantidad_from), moneda_from FROM Registros GROUP by moneda_from")
        sumacf = connect.res.fetchall()
        if sumacf != "":
            totales_criptos_from = []
            for suma in sumacf:
                if suma[1] != 'EUR':
                    totales_criptos_from.append(suma)
            connect.con.close()
            return totales_criptos_from
        else:
            return 0

    def substract_crypto_sums(self):
        """
        total of cryptos purchased minus total of cryptos spent
        """
        crypto_to = self.sum_crypto_to()
        crypto_from = self.sum_crypto_from()
        resultado = []
        if crypto_to != 0 and crypto_from != 0:
            for suma_to in crypto_to:
                for suma_from in crypto_from:
                    if suma_to[1] == suma_from[1]:
                        resta = suma_to[0] - suma_from[0]
                        resultado.append(suma_from[1])
                        resultado.append(resta)
                        nuevo_resultado = [(resultado[i], resultado[i+1])
                                           for i in range(0, len(resultado), 2)]
                        resultado = nuevo_resultado
                        return resultado
        else:
            return 0

    def get_rate_my_cryptos(self):
        """
        checks for current value of all cryptos in wallet
        """
        restas_cripto = self.substract_crypto_sums()
        lista_valores_cripto = []
        if restas_cripto != None:
            for c in restas_cripto:
                crypto = c[0]
                r = requests.get(
                    f'https://rest.coinapi.io/v1/exchangerate/{crypto}/EUR?apikey={API_KEY}')
                resultado = r.json()
                if r.status_code == 200:
                    rate = resultado['rate']
                    valor_cripto = rate * c[1]
                    lista_valores_cripto.append(valor_cripto)
                else:
                    raise ModelError(
                        f"status: {r.status_code} error: {resultado['error']}")
            return sum(lista_valores_cripto)
        else:
            return 0


def format_quantity(quantity):
    """
    receives amount
    returns amount formated with specific decimals depending on amount and with European style
    """
    if quantity >= 1:
        resultado = f'{quantity:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    elif quantity == 0:
        resultado = 0
    elif quantity < 0:
        resultado = f'{quantity:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    else:
        resultado = f'{quantity:,.6f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')

    return resultado

