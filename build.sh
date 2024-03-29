#! /bin/bash

sudo apt-get install python3.7 python3.7-venv

python3.7 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
