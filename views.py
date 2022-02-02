from datetime import datetime

import pytz
from flask import render_template, request, redirect, url_for, flash
from models import LibraryBeer, StockBeer
from app import app, db


@app.route('/')
def index():
    stock_beers = StockBeer.query.all()
    return render_template('index.html', voorraad=stock_beers)


@app.route('/bieren')
def bieren():
    library_beers = LibraryBeer.query.all()
    return render_template('bieren.html', bieren=library_beers)


@app.route('/library-beer/<int:id>/edit', methods=('GET', 'POST'))
def edit_library_beer(id):
    library_beer = LibraryBeer.query.get(id) or LibraryBeer()

    if request.method == 'POST':
        if not library_beer.id:
            db.session.add(library_beer)

        library_beer.brewery = request.form['brewery']
        library_beer.name = request.form['name']
        library_beer.category = request.form['category']
        library_beer.bottle_date_location = request.form['bottleyear']
        library_beer.years_to_mature = request.form['yearstomature'] or None
        library_beer.years_to_bestbefore = request.form['yearstobestbefore'] or None
        db.session.commit()

        return redirect(url_for('bieren'))

    return render_template('edit-library-beer.html', beer=library_beer)


@app.route('/library-beer/<int:id>/delete', methods=('POST',))
def delete_library_beer(id):
    beer = LibraryBeer.query.get(id)
    db.session.delete(beer)
    db.session.commit()

    flash('Beer successfully deleted!')
    return redirect(url_for('bieren'))


@app.route('/stock-beer/<int:id>/edit', methods=('GET', 'POST'))
def edit_stock_beer(id):
    stock_beer = StockBeer.query.get(id) or StockBeer()
    library = LibraryBeer.query.all()

    def totimestamp(date):
        try:
            dt = datetime.strptime(date, '%Y-%m-%d')
            return pytz.utc.localize(dt)
        except:
            print('failed to parse date: ', date)
            return None

    if request.method == 'POST':
        if not stock_beer.id:
            db.session.add(stock_beer)

        stock_beer.librarybeer_id = request.form['beer']
        stock_beer.best_before_date = totimestamp(request.form['bestbeforedate'])
        stock_beer.bottle_date = totimestamp(request.form['bottledate'])
        stock_beer.purchase_date = totimestamp(request.form['purchasedate'])
        stock_beer.purchase_price = request.form['purchaseprice'] or None
        stock_beer.bottle_number = request.form['bottlenumber']
        stock_beer.quantity = request.form['quantity']
        stock_beer.purpose = request.form['purpose']
        stock_beer.comments = request.form['comments']
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit-stock-beer.html', beer=stock_beer, library=library)


@app.route('/stock-beer/<int:id>/delete', methods=('POST',))
def delete_stock_beer(id):
    beer = StockBeer.query.get(id)
    db.session.delete(beer)
    db.session.commit()
    flash('Beer successfully deleted!')
    return redirect(url_for('index'))
