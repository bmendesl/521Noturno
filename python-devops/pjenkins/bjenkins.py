from flask import Blueprint, render_template, redirect, request
from jenkins import Jenkins, EMPTY_CONFIG_XML
from time import sleep

con = Jenkins('http://localhost:8080/',
                username='brunomendes',
                password='4linux')

jenkins = Blueprint('jenkins', __name__, url_prefix='/jenkins')

@jenkins.route('')
def index():
    # print(con.get_all_jobs()[0])
    return render_template('jenkins.html', jobs=con.get_all_jobs())

@jenkins.route('/build/<string:name>')
def build_job(name):
    con.build_job(name)
    sleep(10)
    return redirect('/jenkins')

@jenkins.route('/update/<string:name>', methods=['GET', 'POST'])
def update_job(name):
    if request.method == 'GET':
        return render_template('jenkins_update.html', 
                                job_name=name, xml=con.get_job_config(name))
    elif request.method == 'POST':
        # print(request.form)
        print('action')
        xml = request.form['xml']
        con.reconfig_job(name, xml)
        return redirect('/jenkins')