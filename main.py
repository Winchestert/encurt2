from flask import Flask, request, jsonify, redirect



app = Flask(__name__)

# Dicionário para armazenar as URLs curtas e suas respectivas URLs originais
urls = {}

@app.route('/api/encurtar', methods=['POST'])
def encurtar():
    url = request.json.get('url')  # Obtém a URL original do corpo da requisição POST
    if url:
        # Gere uma chave única para a URL curta (por exemplo, utilizando hash ou algum algoritmo de encurtamento)
        chave = 'url_curta_gerada' # Substitua com o algoritmo de sua escolha

        # Armazena a URL original e a URL curta no dicionário
        urls[chave] = url

        # Retorna a URL curta gerada
        return jsonify(url_curta=f'http://localhost:5000/{chave}')

    return jsonify(erro='URL inválida'), 400  # Retorna uma mensagem de erro caso a URL não seja fornecida

@app.route('/<chave>')
def redirecionar(chave):
    if chave in urls:
        # Redireciona para a URL original correspondente
        return jsonify(url_original=urls[chave])
    else:
        return jsonify(erro='URL curta inválida'), 404  # Retorna uma mensagem de erro caso a chave não seja encontrada

if __name__ == '__main__':
    app.run(debug=True)

#retornar a url encurtada, usando http status code 302
@app.route("/redirect-external", methods=["GET"])
def redirect_external():
    return redirect("https://www.exemplo.com.br/", code=302)

@app.route("/redirect-internal", methods=["GET"])
def redirect_internal():
    return redirect("/landing", code=302)

@app.route("/landing", methods=["GET"])
def landing():
    return "Internal redirect."

@app.route("/", methods=["GET"])
def index():
    return '<a href="/redirect-internal">Internal redirect</a>' \
           '<br>' \
           '<a href="/redirect-external">External redirect</a>'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)





