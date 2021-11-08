import os
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def helloWorld():
    return "Teste da primeira rota hersio"


@app.route("/youtube", methods=["GET"])
def teste():
    return "Rota do youtube funcionando!"


@app.route("/arquivos", methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    # para rodar local, abaixo
    #app.run(host='0.0.0.0', port=port)
    # rodar no server
    server(app, host='0.0.0.0', port=port)
