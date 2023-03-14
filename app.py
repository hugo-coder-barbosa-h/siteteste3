from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, Esse é meu site (Hugo.H)"

@app.route("/sobre")
def sobre():
  return "Aqui vai o conteúdo da pag sobre"

@app.route("/contato")
def contato():
  return "Aqui vai o conteúdo da pag Contato"
