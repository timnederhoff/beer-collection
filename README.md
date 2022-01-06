## Setup

install requirements:
```shell
VENV_DIR="venv"
rm -rf $VENV_DIR
python3 -m venv $VENV_DIR
pip3 install -r requirements.txt
. venv/bin/activate
```

## Run
From the root of this project:
```shell
export FLASK_ENV=development
python3 app.py
```

## TODO
queries:
* gemiddelde prijs per bier
* aantal bieren per (bier+jaar)
* hoeveel bieren op voorraad per jaartal
* aantal jaar tot verkoopdatum per (bier+jaar)
* welke bieren moeten dit jaar verkocht worden?
