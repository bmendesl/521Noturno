from flask import Blueprint, render_template

docker = Blueprint('docker', __name__, url_prefix='/docker')



@docker.route("")
def index():
    return render_template('docker.html')
    