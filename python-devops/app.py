#!/home/developer/521Noturno/python-devops/venvdevops/bin/python3

from flask import Flask, render_template
from pdocker.bdocker import docker
from pjenkins.bjenkins import jenkins
from git_routes.git import gitlab

app  = Flask(__name__)
app.register_blueprint(docker) #registro a minha rota com blueprint
app.register_blueprint(jenkins)
app.register_blueprint(gitlab)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5050)
