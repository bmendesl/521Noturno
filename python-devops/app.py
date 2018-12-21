#!/home/developer/521Noturno/python-devops/venvdevops/bin/python3

from flask import Flask, render_template, request, session, redirect
from pdocker.bdocker import docker
from pjenkins.bjenkins import jenkins
from git_routes.git import gitlab
from ldap3 import Connection, Server
from os import urandom
import logging

logging.basicConfig(
    filename='app.log',
    level= logging.DEBUG,
    format= "%(asctime)s [ %(levelname)s ] %(name)s\n" +
    "[ %(funcName)s ] [ %(filename)s, %(lineno)s] %(message)s",
    datefmt= "[ %d/%m/%Y %H:%M:%S ]" 
)

server = Server('ldap://127.0.0.1:389')

app  = Flask(__name__)
app.register_blueprint(docker) #registro a minha rota com blueprint
app.register_blueprint(jenkins)
app.register_blueprint(gitlab)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        auth = request.form
        dn = "uid={},dc=dexter,dc=com,dc=br".format(auth['email'])
        con = Connection(
            server,
            user=dn,password=auth['password'])

        session['auth'] = con.bind()
        if session['auth']:
            return redirect('/docker')
        logging.warning("login ou senha invalida")
        return redirect('/')

@app.route('/deslogar')
def deslogar():
    session['auth'] = False
    return redirect('/')

if __name__ == "__main__":
    app.secret_key = urandom(12) #trabalhar com sessao e geraremos um token de sessao aleatorio
    app.run(debug=True, port=5050)
