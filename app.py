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


# -------------------------
# Rotas do CCR (client + server)
# -------------------------
@app.route("/ccr")
def ccr_home():
    # Renderiza parte no servidor
    noticias = [
        {"titulo": "Filme 'A Grande Aventura' bate recorde de bilheteira em seu primeiro fim de semana", "conteudo": "O novo filme de ação 'A Grande Aventura' arrecadou mais de R$ 10 milhões em seu primeiro fim de semana nos cinemas."},
        {"titulo": "Análise: Exibição militar da China mostra risco da política de tarifas de Trump", "conteudo": "O poderio militar da República Popular da China foi plenamente exibido em um desfile que marcou o 80º aniversário do fim da Segunda Guerra Mundial na quarta-feira (3/9)."},
    ]
    return render_template("CCR/index.html", noticias=noticias)

@app.route("/api/ccr_categoria/<string:categoria>")
def api_ccr_categoria(categoria):
    noticias_por_categoria = {
        "entretenimento": [
            {"titulo": "Novo filme brasileiro é aclamado em Cannes", "conteudo": "A produção nacional conquistou elogios internacionais."},
            {"titulo": "Cantor famoso anuncia álbum surpresa", "conteudo": "O álbum chega às plataformas digitais na próxima sexta-feira."},
            {"titulo": "Reality show bate recorde de audiência", "conteudo": "O programa alcançou 40 milhões de telespectadores em sua estreia."}
        ],
        "política": [
            {"titulo": "Congresso aprova nova lei tributária", "conteudo": "O texto altera regras de impostos sobre consumo."},
            {"titulo": "Presidente se reúne com líderes mundiais", "conteudo": "O encontro discutiu medidas contra mudanças climáticas."},
            {"titulo": "Eleições municipais têm recorde de candidatos jovens", "conteudo": "Maioria deles disputa pela primeira vez um cargo público."}
        ],
        "esporte": [
            {"titulo": "Brasil conquista ouro no vôlei", "conteudo": "Seleção vence final emocionante contra a Itália."},
            {"titulo": "Time X vence clássico nacional", "conteudo": "Com gol nos acréscimos, garantiu liderança do campeonato."},
            {"titulo": "Atleta quebra recorde mundial", "conteudo": "Marca foi superada em competição internacional."}
        ],
        "receitas": [
            {"titulo": "Bolo de cenoura fofinho", "conteudo": "Aprenda a fazer o clássico bolo com cobertura de chocolate."},
            {"titulo": "Macarrão ao molho pesto", "conteudo": "Receita simples e saborosa em apenas 20 minutos."},
            {"titulo": "Feijoada completa", "conteudo": "O prato típico brasileiro em versão fácil e deliciosa."}
        ]
    }

    return jsonify(noticias_por_categoria.get(categoria.lower(), []))


if __name__ == "__main__":
    app.run(debug=True)
