from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
if __name__ == "__main__":
    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    from views import *

    app.run(debug=True)

# Set up the SQLAlchemy Database to be a local file 'desserts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)


@app.template_filter()
def to_euro_comma_delimited(value):
    if value:
        return "€ {:.2f}".format(value).replace('.', ',')
    else:
        return '-'


@app.template_filter()
def value_or_empty(value):
    if value:
        return "{:.2f}".format(value)
    else:
        return ''


@app.template_filter()
def dash_if_none(value):
    return value or '-'
