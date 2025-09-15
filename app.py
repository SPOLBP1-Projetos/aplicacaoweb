from flask import Flask, render_template, jsonify

app = Flask(__name__)

noticias_por_categoria = {
    "home": [
        {"titulo": "Notícia SSR Home 1", "conteudo": "Conteúdo inicial do servidor"},
        {"titulo": "Notícia SSR Home 2", "conteudo": "Outra notícia inicial"}
    ],
    "entretenimento": [
        {"titulo": "Novo filme é sucesso de bilheteria", "conteudo": "O longa arrecadou milhões em sua estreia."},
        {"titulo": "Cantora lança single surpresa", "conteudo": "A faixa já está no topo das paradas."},
    ],
    "política": [
        {"titulo": "Congresso aprova reforma", "conteudo": "Texto altera regras fiscais."},
        {"titulo": "Presidente participa de cúpula", "conteudo": "Debateu sobre clima e economia."},
    ],
    "esporte": [
        {"titulo": "Brasil vence clássico", "conteudo": "Jogo emocionante decidido no fim."},
        {"titulo": "Atleta quebra recorde", "conteudo": "Novo recorde mundial estabelecido."},
    ],
    "receitas": [
        {"titulo": "Receita de bolo de chocolate", "conteudo": "Fácil e delicioso."},
        {"titulo": "Macarrão caseiro", "conteudo": "Simples e rápido de preparar."},
    ]
}

# -------------------------
# Página inicial (escolha)
# -------------------------
@app.route("/")
def escolha():
    return render_template("escolha.html")


# -------------------------
# Rotas do MPA
# -------------------------
@app.route("/mpa")
def mpa_home():
    return render_template("MPA/home.html")

@app.route("/mpa/entretenimento")
def mpa_entretenimento():
    return render_template("MPA/entretenimento.html")

@app.route("/mpa/politica")
def mpa_politica():
    return render_template("MPA/politica.html")

@app.route("/mpa/esportes")
def mpa_esportes():
    return render_template("MPA/esportes.html")

@app.route("/mpa/receitas")
def mpa_receitas():
    return render_template("MPA/receitas.html")


# -------
# Rotas do SSR (server-side rendering)
# -------
@app.route("/ssr/<string:categoria>")
def ssr_categoria(categoria):
    categoria = categoria.lower()
    noticias = noticias_por_categoria.get(categoria, noticias_por_categoria["home"])
    return render_template("SSR/index.html", noticias=noticias, categoria=categoria)

# Página inicial redireciona para "home"
@app.route("/ssr")
def ssr_home():
    return ssr_categoria("home")


# -----
# Rotas do CSR (client-side rendering)
# ----
@app.route("/csr")
def csr_home():
    # Apenas entrega o HTML vazio + JS
    return render_template("CSR/index.html")

@app.route("/api/csr_noticias")
def api_csr_noticias():
    # API que o JavaScript vai consumir
    noticias = [
        {"titulo": "Notícia CSR 1", "conteudo": "Carregada via fetch()"},
        {"titulo": "Notícia CSR 2", "conteudo": "Outra notícia via AJAX"}
    ]
    return jsonify(noticias)

if __name__ == "__main__":
    app.run(debug=True)
