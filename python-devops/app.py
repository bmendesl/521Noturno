#!/home/developer/521Noturno/python-devops/venvaula1/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

# route parametro de um metodo, o que muda e o que renderiza na rota
# veio com minha url e tenho essa info no meu backend usando como string
@app.route('/<string:nome>', methods=["GET"])
def index(nome):

    return jsonify({'nome':nome})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
    # esta escutando de todos os ips
    # debug nunca por em PROD, pq fica vulneravel




# ------------------------------------------
# route parametro de um metodo, o que muda e o que renderiza na rota
# @app.route('/', methods=["GET"])
# def index():
#     return jsonify({'nome':'bruno'})

# ------------------------------------------
# @app.route('/', methods=["GET"])
# def index():
#     return jsonify({'mensagem':'hello world'})

