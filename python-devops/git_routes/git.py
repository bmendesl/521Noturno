from flask import Flask, Blueprint, render_template
from gitlab import Gitlab

gitlab = Blueprint('gittlab', __name__, url_prefix='/gitlab')

con = Gitlab('http://172.17.0.3', private_token='x9wyRGV97wZa1NeG23DR')

@gitlab.route('')
def index():
    users = con.users.list()
    projects = con.projects.list()
    return render_template('gitlab.html', users=users, projects=projects)


