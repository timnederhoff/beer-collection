from sqlalchemy import func
from app import db
from models import LibraryBeer, StockBeer

print("add some data")
library_beer = LibraryBeer(brewery='Het Anker', name='Gouden Carolus Cuvee van de Keizer Imperial Dark', category='Quadrupel',
                           bottle_date_location='Wikkel', years_to_mature=10, years_to_bestbefore=5)
stock_Beer = StockBeer(librarybeer_id=1, best_before_date=func.now(), bottle_date=func.now(), purchase_date=func.now(),
                       purchase_price=12.34, bottle_number='batch no3', quantity=3, purpose='verkoop', comments='mijn comments')
db.session.add(library_beer)
db.session.add(stock_Beer)
db.session.commit()
print("done!")

