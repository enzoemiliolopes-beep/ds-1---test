from flask import Flask

# intencia do servidor do flask
app = Flask(__name__)

# Reota 1: Pagina inicial
@app.route('/')
def home():
    return "<h1>Servidor Flask rodando!</h1>" "<h1>Bem-Vindo ao meu servidor Flask !<h1/>"

#Rota 2: Sobre aplicação 
@app.route('/sobre')
def sobre():
    return "<h1>Sobre a aplicação<h1/>" "<p>Esta é uma simples aplicação Flask.<p/>"

# Rota 3: Status da aplicação 
@app.route('/status')
def status():
    return "<h1>Status da aplicação <h1/>" "<p>O servidor Flask esta rodando corretamente.<p/>"

if __name__ == '__main__':
    app.run(debug=True)
