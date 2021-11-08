import os
from flask import Flask, request, jsonify, send_from_directory, render_template

#DIRETORIO = "E:\\DOCS\\Python\\vscode\\flask\\api_flask\\Teste_CD\\teste_cd-1\\upload"
#DIRETORIO = ".\\upload"

api = Flask(__name__)
pasta = os.path.abspath('index.html')

print('pasta1:'+pasta)
pasta = pasta.replace(chr(92), chr(47)+chr(47))
pasta = pasta.replace('index.html', 'upload')
print('pasta2:'+pasta)
DIRETORIO = pasta
# parametros = pasta+/upload


@api.route("/arquivos", methods=["GET"])
def index():
    return render_template('index.html')


@api.route("/arquivos", methods=["GET"])
def lista_arquivos():
    arquivos = []

    for nome_do_arquivo in os.listdir(DIRETORIO):
        endereco_do_arquivo = os.path.join(DIRETORIO, nome_do_arquivo)

        if(os.path.isfile(endereco_do_arquivo)):
            arquivos.append(nome_do_arquivo)

    # return "Entrou get1"
    return jsonify(arquivos)


@api.route("/arquivos/<nome_do_arquivo>",  methods=["GET"])
def get_arquivo(nome_do_arquivo):
    # return "Entrou get2"
    return send_from_directory(DIRETORIO, nome_do_arquivo, as_attachment=True)


@api.route("/arquivos", methods=["POST"])
def post_arquivo():
    arquivo = request.files.get("meuArquivo")

    print(arquivo)
    nome_do_arquivo = arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nome_do_arquivo))

    # return "Post"
    return '', 201


if __name__ == "__main__":
    api.run(debug=True, port=8000)
