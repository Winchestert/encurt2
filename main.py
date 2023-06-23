from flask import Flask, request, jsonify, redirect
import string, random



app = Flask(__name__)

# Dicionário para armazenar as URLs curtas e suas respectivas URLs originais
urls = {}

@app.route('/api/encurtar', methods=['POST'])
def encurtar():
    url = request.json.get('url')  # Obtém a URL original do corpo da requisição POST
    def generate_short_code():
        if url:
            chave = generate_short_code()  # Gera uma chave única para a URL curta
            urls[chave] = url  # Armazena a URL original e a URL curta no dicionário

        # Retorna a URL curta gerada
            return jsonify(url_curta=f'http://localhost:5000/{chave}', code=302)

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
@app.route('/<chave>')
def redirecionar(chave):
    if chave in urls:
        # Redireciona para a URL original correspondente com o status code 302
        return redirect(urls[chave], code=302)
    else:
        return jsonify(erro='URL curta inválida'), 404  # Retorna uma mensagem de erro caso a chave não seja encontrada

if __name__ == '__main__':
    app.run(debug=True)




