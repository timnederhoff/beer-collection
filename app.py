import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from datetime import datetime
from werkzeug.exceptions import abort

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('bieren.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_library_beer(library_id):
    conn = get_db_connection()
    beer = conn.execute('SELECT * FROM bieren WHERE id = ?', (library_id,)).fetchone()
    conn.close()
    if beer is None:
        abort(404)
    return beer


def get_stock_beer(stock_id):
    conn = get_db_connection()
    stock_beer = conn.execute('SELECT * FROM voorraad WHERE id = ?', stock_id).fetchone()
    conn.close()
    if stock_beer is None:
        abort(404)
    return stock_beer


@app.route('/')
def index():
    conn = get_db_connection()
    voorraad = conn.execute('SELECT voorraad.id AS ID, '
                            'bieren.naam AS Bier, '
                            'voorraad.bottelDatum AS Botteldatum, '
                            'voorraad.aankoopDatum AS Aankoopdatum, '
                            'voorraad.tenMinsteHoudbaarTot AS THT, '
                            'voorraad.aantal AS Aantal, '
                            'voorraad.prijsinkoop*0.01 AS Prijs '
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


@app.route('/library-beer/<int:id>/edit', methods=('GET', 'POST'))
def edit_library_beer(id):
    library_beer = get_library_beer(id)

    if request.method == 'POST':
        brewery = request.form['brewery']
        name = request.form['name']

        if not (brewery or name):
            flash('Brewery and Name are required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE bieren SET brouwerij = ?, naam = ?'
                         ' WHERE id = ?',
                         (brewery, name, id))
            conn.commit()
            conn.close()
            return redirect(url_for('bieren'))

    return render_template('edit-library-beer.html', beer=library_beer)


@app.template_filter()
def epoch_to_date(value, formatstr="%Y"):
    if isinstance(value, int):
        return datetime.utcfromtimestamp(value).strftime(formatstr)
    return '-'


@app.template_filter()
def cents_to_euros(value):
    if value:
        return "€ {:.2f}".format(value).replace('.', ',')
    else:
        return '-'


@app.template_filter()
def dash_if_none(value):
    return value or '-'
