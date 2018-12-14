#!/home/developer/521Noturno/python-devops/venvdevops/bin/python3

from flask import Flask, render_template
from docker.bdocker import docker

app  = Flask(__name__)
app.register_blueprint(docker)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
