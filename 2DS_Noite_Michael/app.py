from flask import Flask, render_template, request

# intencia do servidor do flask
app = Flask(__name__)

# Reota 1: Pagina inicial
@app.route('/')
def home():
    return render_template("index.html")

#Rota 2: Exibição da tela de cadastro MEteodo (GET)
@app.route('/cadastro')
def pagina_cadastro():
    return render_template("cadastro.html")

# Rota 3: Processamento dos dados Metodo (POST)
@app.route('/salvar', methods=["POST"])
def salvar_cadastro():
    nome_digitado = request.form.get("campo_nome")
    info_digitado = request.form.get("campo_info")

    return render_template("resultado.html", nome=nome_digitado, info=info_digitado)

if __name__ == '__main__':
    app.run(debug=True)
