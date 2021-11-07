import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def helloWorld():
	return "Teste da primeira rota no vídeo do Samuel."

@app.route("/youtube", methods=["GET"])
def teste():
    return "Rota do youtube funcionando!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)