from flask import Flask, render_template, request, redirect

# Inicialização do servidor Flask
app = Flask(__name__)

# Base de dados em memória
lista_de_caastro = []

# Rota 1: Página inicial
@app.route('/')
def home():
    busca = request.args.get("busca", "").strip().lower()

    if busca:
        registros_filtrados = [item for item in lista_de_caastro if busca in item["nome"].lower()]
    else:
        registros_filtrados = lista_de_caastro
    
    # Cálculo de métricas / indicadores 
    total_registro = len(lista_de_caastro)
    total_faturamento = sum(item["valor"] for item in lista_de_caastro)
    total_concluidos = sum(1 for item in lista_de_caastro if item["status"] == "concluidos")

    # Enviar os indicadores para a página 
    return render_template("index.html",
        cadastro=registros_filtrados,
        total=total_registro,
        faturamento=total_faturamento,
        concluidos=total_concluidos,
        busca=busca
    )

# Rota 2: Exibição da tela de cadastro (GET)
@app.route('/cadastro')
def pagina_cadastro():
    return render_template("cadastro.html")

# Rota 3: Processamento dos dados (POST)
@app.route('/salvar', methods=["POST"])
def salvar_cadastro():
    nome_digitado = request.form.get("campo_nome", "").strip()
    info_digitado = request.form.get("campo_info", "").strip()
    valor_str = request.form.get("campo_valor", "0").strip()

    try:
        valor = float(valor_str)
        if valor <= 0:
            raise ValueError()
    except ValueError:
        return "<h3>Erro 400: o valor deve ser um valor maior que zero!</h3><br><a href='/cadastro'>voltar ao formulário</a>", 400

    # Validação: verificar se os campos obrigatórios vieram vazios
    if not nome_digitado or not info_digitado:
        return "<h3>Erro 400: preencha todos os campos obrigatórios do formulário</h3><br><a href='/cadastro'>voltar ao formulário</a>", 400

    # Criação do novo registro
    novo_registro = {
        "nome": nome_digitado,
        "info": info_digitado,
        "valor": valor,
        "status": "pendente"
    }

    lista_de_caastro.append(novo_registro)

    # Redirecionar para a home 
    return redirect("/")

# Rota 4: Alterar status
@app.route("/mudar-status/<int:indice>")
def mudar_status(indice):
    if 0 <= indice < len(lista_de_caastro):
        if lista_de_caastro[indice]["status"] == "pendente":
            lista_de_caastro[indice]["status"] = "concluidos"
        else:
            lista_de_caastro[indice]["status"] = "pendente"

    return redirect("/")

# Rota 5: Excluir registro
@app.route("/excluir/<int:indice>")
def excluir_cadastro(indice):
    if 0 <= indice < len(lista_de_caastro):
        lista_de_caastro.pop(indice)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)