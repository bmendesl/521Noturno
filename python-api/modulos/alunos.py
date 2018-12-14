#!/home/developer/521Noturno/python-devops/venvaula1/bin/python3

from flask import Blueprint, make_response
import json
# Blueprint serve para separar em arquivos diferentes para nao ficar poluido em um aquivo so as rotas

alunos = Blueprint('alunos', __name__, url_prefix="/alunos")

@alunos.route("") #vaizo e equivalente a /alunos - chamei de alunos passou o decorator com @alunos 
def index():
    headers = {"content-type": "application/json", "teste": "teste"}
    conteudo = [
        {"aluno": "bruno"},
        {"aluno": "ze"}
    ]
    return make_response(json.dumps(conteudo), 200, headers)