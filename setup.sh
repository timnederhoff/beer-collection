#!/usr/bin/env sh
VENV_DIR="venv"

rm -rf $VENV_DIR
python3 -m venv $VENV_DIR
pip3 install -r requirements.txt
