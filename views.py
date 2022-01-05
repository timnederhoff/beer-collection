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
    library_beer = LibraryBeer.query.get(id)

    if request.method == 'POST':
        brewery = request.form['brewery']
        name = request.form['name']
        category = request.form['category']
        bottle_date_location = request.form['bottleyear']
        years_to_mature = request.form['yearstomature']
        years_to_bestbefore = request.form['yearstobestbefore']

        beer = LibraryBeer(id, brewery, name, category, bottle_date_location, years_to_mature, years_to_bestbefore)

        db.session.add(beer)
        db.session.commit()
        return redirect(url_for('bieren'))

    return render_template('edit-library-beer.html', beer=library_beer)


@app.route('/library-beer/<int:id>/delete', methods=('POST',))
def delete_library_beer(id):
    LibraryBeer.query().filter_by(id=id).delete()
    db.session.commit()

    flash('Beer successfully deleted!')
    return redirect(url_for('bieren'))


@app.route('/stock-beer/<int:id>/edit', methods=('GET', 'POST'))
def edit_stock_beer(id):
    stock_beer = StockBeer.query.get(id)
    library = LibraryBeer.query.all()

    def totimestamp(date):
        try:
            dt = datetime.strptime(date, '%Y-%m-%d')
            return int(pytz.utc.localize(dt).timestamp())
        except:
            print('failed to parse date: ', date)
            return ''

    if request.method == 'POST':
        librarybeer_id = request.form['beer']
        best_before_date = totimestamp(request.form['bestbeforedate'])
        bottle_date = totimestamp(request.form['bottledate'])
        purchase_date = totimestamp(request.form['purchasedate'])
        purchase_price = str(int(float(request.form['purchaseprice']) * 100))
        bottle_number = request.form['bottlenumber']
        quantity = request.form['quantity']
        purpose = request.form['purpose']
        comments = request.form['comments']

        beer = StockBeer(id, librarybeer_id, best_before_date, bottle_date, purchase_date, purchase_price, bottle_number, quantity, purpose, comments)
        db.session.add(beer)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit-stock-beer.html', beer=stock_beer, library=library)


@app.route('/stock-beer/<int:id>/delete', methods=('POST',))
def delete_stock_beer(id):
    StockBeer.filter_by(id=id).delete()
    db.session.commit()
    flash('Beer successfully deleted!')
    return redirect(url_for('index'))
