from flask import Flask, render_template, jsonify

app = Flask(__name__)

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


# -------------------------
# Rotas do SSR (server-side rendering)
# -------------------------
@app.route("/ssr")
def ssr_home():
    # Aqui, o Python já monta os dados e envia prontos para o template
    noticias = [
        {"titulo": "Notícia SSR 1", "conteudo": "Conteúdo gerado pelo servidor"},
        {"titulo": "Notícia SSR 2", "conteudo": "Outro conteúdo vindo direto do servidor"}
    ]
    return render_template("SSR/index.html", noticias=noticias)


# -------------------------
# Rotas do CSR (client-side rendering)
# -------------------------
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


# -------------------------
# Rotas do CCR (client + server)
# -------------------------
@app.route("/ccr")
def ccr_home():
    # Renderiza parte no servidor
    noticias = [
        {"titulo": "Notícia CCR 1", "conteudo": "Mistura server + client"},
    ]
    return render_template("CCR/index.html", noticias=noticias)

@app.route("/api/ccr_noticias")
def api_ccr_noticias():
    # Complementa depois no cliente
    noticias = [
        {"titulo": "Notícia CCR 2", "conteudo": "Carregada via AJAX"},
        {"titulo": "Notícia CCR 3", "conteudo": "Mais dados após o load inicial"}
    ]
    return jsonify(noticias)


if __name__ == "__main__":
    app.run(debug=True)
