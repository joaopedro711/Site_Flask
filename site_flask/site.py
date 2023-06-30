from flask import Flask, request

app = Flask(__name__)

@app.route("/comando", methods=["GET", "POST"])
def comando():
    if request.method == "GET":
        if 'mensagem_comando' in app.config:                        #caso exista alguma mensagem_comando na variável de configuração
            mensagem_comando = app.config['mensagem_comando']
            return mensagem_comando
        else:
            return 'Nenhuma mensagem_comando foi postada ainda.'
    
    elif request.method == "POST":
        mensagem_comando = request.data.decode('utf-8')             # Obtém a mensagem do corpo (se for html) da requisição
        app.config['mensagem_comando'] = mensagem_comando           # Armazena a mensagem_comando na variável de configuração
        return 'Mensagem_comando postada'

@app.route("/resposta", methods=["GET", "POST"])
def resposta():
    if request.method == "GET":
        if 'mensagem_resposta' in app.config:                        #caso exista alguma mensagem_resposta na variável de configuração
            mensagem_resposta = app.config['mensagem_resposta']
            return mensagem_resposta
        else:
            return 'Nenhuma mensagem_resposta foi postada ainda.'
    
    elif request.method == "POST":
        mensagem_resposta = request.data.decode('utf-8')             # Obtém a mensagem_resposta do corpo (se for html) da requisição
        app.config['mensagem_resposta'] = mensagem_resposta          # Armazena a mensagem na variável de configuração
        return 'Mensagem_resposta postada'

if __name__ == "__main__":
    app.run(debug=True)