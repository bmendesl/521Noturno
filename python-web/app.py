#!/home/developer/521Noturno/python-web/venv_web/bin/python3

from flask import Flask, render_template
from pymongo import MongoClient
import requests

app = Flask(__name__)

@app.route('/')
def index():
    var = list(range(10))
    return render_template('index.html', numeros=var)

@app.route('/cep/<string:cep>')
def teste(cep):
    data = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    print(data)
    return render_template('index2.html', data=data.json())

if __name__ == "__main__":
    app.run(debug=True)
