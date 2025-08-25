from flask import Flask, redirect, url_for, render_template, request, session, make_response

app = Flask(__name__)

app.secret_key = '1234'


@app.route("/login", methods=["GET", "POST"])
def carregarform():
    tema = request.cookies.get("tema", "claro")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Verifica as credenciais
        if username == "admin" and password == "1234":
            # Se as credenciais estiverem corretas, define a sessão como permanente
            # e armazena o nome de usuário na sessão.
            session.permanent = True
            session["username"] = username
            return redirect(url_for("/home"))
        else:
            # Se as credenciais estiverem incorretas, renderiza a página de login
            # novamente com uma mensagem de erro.
            return render_template("login.html", error="Usuário ou senha inválidos.", tema=tema)
        
@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("views", None)
    return redirect(url_for("carregarform"))