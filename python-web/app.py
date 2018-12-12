#!/home/developer/521Noturno/python-web/venv_web/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index()
