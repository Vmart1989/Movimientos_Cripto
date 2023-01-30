import sqlite3
import requests #forcoinAPI
from config import *
from mov_criptos.connection import Connection
from mov_criptos.forms import RegistrosForm


def show_all():
    connect = Connection("select id,date,time,moneda_from,cantidad_from,moneda_to,cantidad_to,precio_unitario from registros order by date DESC")
    filas = connect.res.fetchall()
    columnas= connect.res.description

    resultado =[]
   
    for fila in filas:
        dato={}
        posicion=0

        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)

    connect.con.close()

    return resultado

def getEUR():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    euro = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "EUR":
            euro = item["asset_id"]
    return euro

def getBTC():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    btc = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "BTC":
            btc = item["asset_id"]
    return btc

def getETH():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    eth = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "ETH":
            eth = item["asset_id"]
    return eth

def getUSDT():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    usdt = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "USDT":
            usdt = item["asset_id"]
    return usdt

def getBNB():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    bnb = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "BNB":
            bnb = item["asset_id"]
    return bnb

def getXRP():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    xrp = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "XRP":
            xrp = item["asset_id"]
    return xrp

def getADA():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    ada = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "ADA":
            ada = item["asset_id"]
    return ada

def getSOL():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    sol = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "SOL":
            sol = item["asset_id"]
    return sol

def getDOT():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    dot = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "DOT":
            dot = item["asset_id"]
    return dot

def getMATIC():
    r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_KEY}')
    matic = ""
    lista_general = r.json()
    for item in lista_general:
        if item["asset_id"] == "MATIC":
            matic = item["asset_id"]
    return matic

def getRate(API_KEY):
    moneda_from = RegistrosForm(moneda_from)
    moneda_to = RegistrosForm(moneda_to)
    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_from}/{moneda_to}?apikey={API_KEY}')
    resultado = r.json()
    if r.status_code == 200:
        rate = resultado['rate']
        
    return rate

##COINAPI##
'''

class ModelError(Exception):
    pass

class MyCoinsApiIO:

    def getCoins(self, apiKey):
        r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apiKey}')
        if r.status_code != 200:
            raise ModelError("Error en consulta de assets:{}".format(r.status_code))

        lista_general = r.json()
        coin = ""
        for item in lista_general:
            coin = item["asset_id"]
            
            if item["asset_id"] == "EUR" or \
            item["asset_id"] == "BTC" or \
            item["asset_id"] == "ETH" or \
            item["asset_id"] == "USDT" or \
            item["asset_id"] == "BNB" or \
            item["asset_id"] == "XRP" or \
            item["asset_id"] == "ADA" or \
            item["asset_id"] == "SOL" or \
            item["asset_id"] == "DOT" or \
            item["asset_id"] == "MATIC":
            
                coin = coin.append(item["asset_id"])
                

class Exchange:
    def __init__(self,cripto):
        self.cripto = cripto
        self.rate = None
        self.time = None
        self.r = None
        self.resultado = None
    
    def updateExchange(self, apiKey):
        self.r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.cripto}/EUR?apikey={apiKey}')
        self.resultado = self.r.json()
        if self.r.status_code == 200:
            self.rate = self.resultado['rate']
            self.time = self.resultado['time']
        else:
            raise ModelError(f"status: {self.r.status_code} error: {self.resultado['error']}")
            
'''