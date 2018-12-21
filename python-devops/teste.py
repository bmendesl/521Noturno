import paramiko

client = paramiko.client.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())#registra caso seja a primeira conexao




client.connect(
    '192.168.203.10',
    username='noturno',
    password='noturno',
)

stdin, stdout, stderr = client.exec_command("ls -la")

if stdout.channel.recv_exit_status() == 0:
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))


# from ldap3 import Connection, Server

# server = Server('ldap://127.0.0.1:389')
# # user = 'admin'
# # password = '4linux'
# dn = "uid=bruno@4linux.com.br,dc=dexter,dc=com,dc=br"

# # con = Connection(
# #     server,
# #     "cn={},dc=dexter,dc=com,dc=br".format(user), password
# # )

# con = Connection(
#     server,
#     user=dn,password='4linux'
# )

# print(con.bind())

# dn = "uid=bruno@4linux.com.br,dc=dexter,dc=com,dc=br"
# con.search(dn, "(objectclass=person)", attributes=['sn', 'userPassword'])

# # from jenkins import Jenkins # modelo que o jenkins deixa importar
# # from jenkins import Jenkins, EMPTY_CONFIG_XML # modelo que o jenkins deixa importar
# # from gitlab import Gitlab
# # from gitlab import Gitlab
# # con = Jenkins('http://localhost:8080/',
# #                 username='brunomendes',
# #                 password='4linux')
# import requests
# from gitlab import Gitlab
# from pprint import pprint
# # import gitlab
# # post = {
# #     "name":"flask-app"
# # }
# # token = 'x9wyRGV97wZa1NeG23DR'
# # usuarios = requests.get(
# #                     "http://172.17.0.3/api/v4/projects?private_token={}".format(token)
# #                         )
# # pprint(usuarios.json())

# # exit()

# # projetos = requests.post(
# #                     "http://172.17.0.3/api/v4/projects?private_token={}".format(token), post
#                         # )
# # pprint(projetos.json())
# con = Gitlab('http://172.17.0.3', private_token='x9wyRGV97wZa1NeG23DR')

# projects = con.projects.list()
# # for project in projects:
# #     print(project)

# print(con.projects.list())

# # print(con.get_job_info('teste'))
# # print(con.get_job_info_regex('teste'))
# # print(con.get_job('teste'))
# # con.create_job('job3', EMPTY_CONFIG_XML)
# # con.build_job('teste')
# # con.rename_job('teste2', 'teste')
# # print(dir(con))
# # # print(con.get_all_jobs()) # tras todos os jobs 
# # print(EMPTY_CONFIG_XML) 
# # print(con.get_whoami()) # dados do user
# # print(con.get_version())
# # import docker

# # con = docker.DockerClient("tcp://127.0.0.1:2376")


# # # for container in con.containers.list(all=True):
# # #     print(container.name, container.short_id)

# # container = con.containers.get("flask-app")

# # print(container.name, container.short_id)