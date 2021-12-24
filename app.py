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
    stock_beer = conn.execute('SELECT * FROM voorraad WHERE id = ?', (stock_id,)).fetchone()
    conn.close()
    if stock_beer is None:
        abort(404)
    return stock_beer


def get_library():
    conn = get_db_connection()
    library = conn.execute('SELECT * FROM bieren ORDER BY brouwerij, naam').fetchall()
    conn.close()
    return library


@app.route('/')
def index():
    conn = get_db_connection()
    voorraad = conn.execute('SELECT voorraad.id, '
                            'bieren.naam, '
                            'voorraad.bottelDatum, '
                            'voorraad.aankoopDatum, '
                            'voorraad.tenMinsteHoudbaarTot, '
                            'voorraad.aantal, '
                            'voorraad.prijsinkoop*0.01 '
                            'FROM bieren, voorraad '
                            'WHERE voorraad.bier = bieren.id '
                            'ORDER BY bieren.naam, voorraad.bottelDatum').fetchall()
    conn.close()
    return render_template('index.html', voorraad=voorraad)


@app.route('/bieren')
def bieren():
    return render_template('bieren.html', bieren=get_library())


@app.route('/library-beer/<int:id>/edit', methods=('GET', 'POST'))
def edit_library_beer(id):
    library_beer = get_library_beer(id)

    if request.method == 'POST':
        brewery = request.form['brewery']
        name = request.form['name']
        category = request.form['category']
        bottleyear = request.form['bottleyear']
        yearstomature = request.form['yearstomature']
        yearstobestbefore = request.form['yearstobestbefore']

        if not (brewery or name):
            flash('Brewery and Name are required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE bieren '
                         'SET (brouwerij, naam, soort, plekOpflesBotteljaar, aantalJarenRijpen, aantalJarenTotTHT) '
                         '= (?, ?, ?, ?, ?, ?) '
                         'WHERE id = ?',
                         (brewery, name, category, bottleyear, yearstomature, yearstobestbefore, id))
            conn.commit()
            conn.close()
            return redirect(url_for('bieren'))

    return render_template('edit-library-beer.html', beer=library_beer)


@app.route('/library-beer/<int:id>/delete', methods=('POST',))
def delete_library_beer(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM bieren WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Beer successfully deleted!')
    return redirect(url_for('bieren'))


@app.route('/stock-beer/<int:id>/edit', methods=('GET', 'POST'))
def edit_stock_beer(id):
    stock_beer = get_stock_beer(id)
    library = get_library()

    if request.method == 'POST':
        beer_id = request.form['beer']
        quantity = request.form['quantity']
        bottledate = request.form['bottledate']
        purchasedate = request.form['purchasedate']
        bestbeforedate = request.form['bestbeforedate']
        purchaseprice = request.form['purchaseprice']

        if not (beer_id or quantity):
            flash('Beer and quantity are required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE voorraad '
                         'SET (bier, aantal, bottelDatum, aankoopDatum, tenMinsteHoudbaarTot, prijsinkoop) '
                         '= (?, ?, ?, ?, ?, ?) '
                         'WHERE id = ?',
                         (beer_id, quantity, bottledate, purchasedate, bestbeforedate, purchaseprice, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit-stock-beer.html', beer=stock_beer, library=library)


@app.route('/stock-beer/add', methods=('GET', 'POST'))
def add_stock_beer():
    library = get_library()

    if request.method == 'POST':
        library_beer_id = request.form['beer']
        quantity = request.form['quantity']

        if not (library_beer_id or quantity):
            flash('Beer and quantity are required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO voorraad (bier, aantal) VALUES (?, ?)', (library_beer_id, quantity))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('add-stock-beer.html', library=library)


@app.route('/stock-beer/<int:id>/delete', methods=('POST',))
def delete_stock_beer(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM voorraad WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


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


@app.template_filter()
def get_name_of(library, beer):
    return [item for item in library if item['id'] == beer][0]['naam']
