import sqlite3
from config import *
from mov_criptos.connection import Connection

def show_all():
    connect = Connection("select id,date,time,moneda_from,cantidad_from,moneda_to,cantidad_to from registros order by date DESC")
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