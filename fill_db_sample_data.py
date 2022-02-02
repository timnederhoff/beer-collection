import sqlite3
from app import db
from models import LibraryBeer

print("add some data")
db.session.add(LibraryBeer(brewery='Het Anker', name='Gouden Carolus Cuvee van de Keizer Imperial Dark', category='Quadrupel', bottle_date_location='Wikkel', years_to_mature=10, years_to_bestbefore=5))
db.session.add(LibraryBeer(brewery='Hertog Jan', name='Grand Prestige', category='Quadrupel', bottle_date_location='Etiket, dop', years_to_mature=8))
db.session.add(LibraryBeer(brewery='Het Anker', name='Gouden Carolus Whisky Infused', category='Quadrupel'))
db.session.add(LibraryBeer(brewery='St.Bernardus', name='St.Bernardus Abt 12', category='Quadrupel', years_to_bestbefore=4))
db.session.add(LibraryBeer(brewery='Kompaan', name='The Black Gold Bloedbroeder', category='Stout + ruby port'))
db.session.add(LibraryBeer(brewery='Rochefort', name='Rochefort 8', category='Gerstewijn', years_to_bestbefore=5))
db.session.add(LibraryBeer(brewery='The Musketeers', name='Troubadour Imperial stout', category='Stout'))
db.session.add(LibraryBeer(brewery='The Musketeers', name='Troubadour Obscura', category='Milde Stout'))
db.session.add(LibraryBeer(brewery='De Koningshoeven', name='La Trappe Quadrupel', category='Quadrupel', years_to_bestbefore=3))
db.session.add(LibraryBeer(brewery='De Halve Maan', name='Straffe Hendrik Quadrupel', category='Quadrupel'))
db.session.add(LibraryBeer(brewery='De Halve Maan', name='Straffe Hendrik Heritage', category='Quadrupel', bottle_date_location='Etiket'))
db.session.add(LibraryBeer(brewery='Maallust', name='Maallust 1818', category='Quadrupel', bottle_date_location='Etiket', years_to_mature=25, years_to_bestbefore=25))
db.session.add(LibraryBeer(brewery='Frontaal', name='Rhodesian', category='Gerstewijn', bottle_date_location='Etiket', years_to_mature=10, years_to_bestbefore=5))
db.session.add(LibraryBeer(brewery='Abdij van Orval', name='Orval', category='Trappist', bottle_date_location='Etiket'))
db.session.add(LibraryBeer(brewery='3 Fonteinen', name='Oude Geuze', category='Geuze', bottle_date_location='Etiket, kurk', years_to_mature=15, years_to_bestbefore=40))
db.session.add(LibraryBeer(brewery='Boon', name='Oude Geuze Boon', category='Geuze', bottle_date_location='Wikkel', years_to_bestbefore=20))
db.session.add(LibraryBeer(brewery='Van Steenberge', name='Gulden Draak 9000 Quadrupel', category='Quadrupel', bottle_date_location='Etiket'))
db.session.add(LibraryBeer(brewery='Van Steenberge', name='Gulden Draak Brewmaster Edition', category='Bruin, dubbel', bottle_date_location='Etiket'))
db.session.add(LibraryBeer(brewery='Vanhonsebrouck', name='Kasteel Donker', category='Bruin, dubbel', years_to_mature=15))
db.session.add(LibraryBeer(brewery='Abdij van Val Dieu', name='Val-Dieu Grand Cru', category='Strong Ale', years_to_mature=10, years_to_bestbefore=5))
db.session.add(LibraryBeer(brewery='Bosteels', name='Pauwel Kwak', category='Strong Ale'))
db.session.add(LibraryBeer(brewery='Abdij van Chimay', name='Chimay Grande Reserve', category='Quadrupel', bottle_date_location='Etiket', years_to_mature=15, years_to_bestbefore=5))

db.session.commit()

connection = sqlite3.connect('db.db')
with open('fill_db_sample_data.sql') as f:
    connection.executescript(f.read())
connection.commit()
connection.close()

print("done!")

