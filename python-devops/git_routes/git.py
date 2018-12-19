from flask import Flask, Blueprint, render_template


gitlab = Blueprint('gittlab', __name__, url_prefix='/gitlab')

@gitlab.route('')
def index():
    return render_template('gitlab.html')
