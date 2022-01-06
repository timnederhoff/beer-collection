from datetime import date

from sqlalchemy import func

from app import db


class LibraryBeer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brewery = db.Column(db.String(200))
    name = db.Column(db.String(200))
    category = db.Column(db.String(200))
    bottle_date_location = db.Column(db.String(200))
    years_to_mature = db.Column(db.Integer)
    years_to_bestbefore = db.Column(db.Integer)

    def __repr__(self):
        return '<Library Beer %r>' % self.name


class StockBeer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    librarybeer_id = db.Column(db.Integer, db.ForeignKey('library_beer.id'), nullable=False)
    librarybeer = db.relationship('LibraryBeer', backref=db.backref('stockbeers', lazy=True))
    best_before_date = db.Column(db.Date)
    bottle_date = db.Column(db.Date)
    purchase_date = db.Column(db.Date)
    purchase_price = db.Column(db.Float)
    bottle_number = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    purpose = db.Column(db.String(200))
    comments = db.Column(db.String(200))

    def __repr__(self):
        return '<Stock Beer %r>' % self.librarybeer


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()

    print("add some data")
    library_beer = LibraryBeer(brewery='Het Anker', name='Gouden Carolus Cuvee van de Keizer Imperial Dark', category='Quadrupel',
                               bottle_date_location='Wikkel', years_to_mature=10, years_to_bestbefore=5)
    stock_Beer = StockBeer(librarybeer_id=1, best_before_date=func.now(), bottle_date=func.now(), purchase_date=func.now(),
                           purchase_price=12.34, bottle_number='batch no3', quantity=3, purpose='verkoop', comments='mijn comments')
    db.session.add(library_beer)
    db.session.add(stock_Beer)
    db.session.commit()
    print("Done!")
