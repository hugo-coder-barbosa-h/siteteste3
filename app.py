from flask import Flask
app=Flask(_name_)

menu="""
<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> ! <a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def index():
  return "Olá, Esse é meu site (Hugo.H)"
def hello_world():
  return menu+"Olá, mundo! Esse é o meu site. (Graziela França)"

@app.route("/sobre")
def sobre():
  return "Aqui vai o conteúdo da pag sobre"
  return menu+"Aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
  return "Aqui vai o conteúdo da pag Contato"
  return menu+"Aqui vai o conteúdo da página Contato"
