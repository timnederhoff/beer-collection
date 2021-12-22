import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('bieren.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    voorraad = conn.execute('SELECT bieren.naam AS Bier, '
                            'strftime("%Y", voorraad.bottelDatum, "unixepoch") AS Botteldatum, '
                            'strftime("%Y", voorraad.aankoopDatum, "unixepoch") AS Aankoopdatum, '
                            'voorraad.aantal AS Aantal '
                            'FROM bieren, voorraad '
                            'WHERE voorraad.bier = bieren.id '
                            'ORDER BY bieren.naam, voorraad.bottelDatum').fetchall()
    conn.close()
    return render_template('index.html', voorraad=voorraad)


@app.route('/bieren')
def bieren():
    conn = get_db_connection()
    bieren = conn.execute('SELECT * FROM bieren ORDER BY brouwerij, naam').fetchall()
    conn.close()
    return render_template('bieren.html', bieren=bieren)


@app.template_filter()
def dash_if_none(value):
    return value or '-'
