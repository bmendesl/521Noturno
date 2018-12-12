#!/home/developer/521Noturno/python-devops/venvaula1/bin/python3

from flask import Flask, jsonify, request
from pymongo import MongoClient


try:
    con = MongoClient()
    db = con['python'] #chamando de 'db' so para a sintaxe ficar igual ao mongo
except Exception as e:
    print(e)

app = Flask(__name__)

def validar_json(json):
    if json:
        try:
            if json['nome'] and json['_id']:
                db.usuarios.insert(json)
                return True
            else:
                return False
        except KeyError:
            return False
    else:
        return False

# route parametro de um metodo, o que muda e o que renderiza na rota
# veio com minha url e tenho essa info no meu backend usando como string
@app.route('/<string:nome>', methods=['GET'])
def index(nome):
    return jsonify({'nome':nome})

# pegando todos da tabela usuarios no banco
# @app.route('/usuarios', methods=['GET'])
# def usuarios():
#     return jsonify(list(db.usuarios.find())) #find cursor que transformamos em lista

# pegando todos da tabela usuarios no banco - outro modo
@app.route('/usuarios', methods=['GET', 'POST', 'PUT'])
def usuarios():
    if request.method == 'GET':
        return jsonify(list(db.usuarios.find())) #find cursor que transformamos em lista
    else:
        data = request.get_json() #recebe o post do POSTMAN com formato json e trata se e vazio
        if isinstance(data, dict):   #isinstance funciona como teste, nesse caso se o objeto for dicionario true 
            status = validar_json(data)
            return jsonify({'status': status})
        elif isinstance(data, list):
            for registro in data:
                if not validar_json(registro):
                    return jsonify({'status': False})
                else:
                    return jsonify({'status': True})
            
# # Passando o id do usuario no banco na tabela usuarios e ele retorna com os dados do usuario
@app.route('/usuario/<int:id>', methods=['GET', 'PUT'])
def get_user_id(id):
    return jsonify(db.usuarios.find_one({'_id':id})) #find_one ja tras com formato de dicionario sem precisar de trazer em formato lista

# Melhorando o codigo acima, trantando se for int ou string para buscar pelo nome tambem
@app.route('/usuarios/<string:busca>', methods=['GET'])
def get_user(busca):
    if busca.isnumeric():
        return jsonify(db.usuarios.find_one({'_id': int(busca)}))
    else:
        return jsonify(list(db.usuarios.find({'nome':busca.lower().strip()})))

# trabalhando o metodo POST         
@app.route('/usuarios', methods=['POST'])
def register_user():
    print(request.get_json()) #request usamos para pegar dados que o usuario envia
    return 'success'

# esta escutando de todos os ips
# debug nunca por em PROD, pq fica vulneravel
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)




# 11/12
# ------------------------------------------
# jeito que eu fiz
# @app.route('/usuarios')
# def usuarios():
#     usuarios = []
#     for x in db.usuarios.find():
#         usuarios.append(x)
#     return jsonify(usuarios)

# -----------------------------------------------------
# @app.route('/usuarios/<int:id>', methods=["GET"])
# def get_user(id):
#     return jsonify(list(db.usuarios.find({'_id':id}))) #find cursor que transformamos em lista



# -----------------------------------------------------------------------------------------------------
# 10/12
# ------------------------------------------
# route parametro de um metodo, o que muda e o que renderiza na rota
# @app.route('/', methods=["GET"])
# def index():
#     return jsonify({'nome':'bruno'})

# ------------------------------------------
# @app.route('/', methods=["GET"])
# def index():
#     return jsonify({'mensagem':'hello world'})



