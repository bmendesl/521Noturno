from flask import Blueprint, render_template, redirect
from docker import DockerClient

docker = Blueprint('docker', __name__, url_prefix='/docker')

con = DockerClient("tcp://127.0.0.1:2376") # API do docker

@docker.route("")
def index():
    containers = con.containers.list(all=True)
    return render_template('newdocker.html', containers=containers)

@docker.route("/start/<string:id>")
def start_container(id):
    container = con.containers.get(id)
    container.start()
    return redirect('/docker')

@docker.route("/stop/<string:id>")
def stop_container(id):
    container = con.containers.get(id)
    container.stop()
    return redirect('/docker')
