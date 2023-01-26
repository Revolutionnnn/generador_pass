from flask import Flask, render_template, request
from main import generator_password

app = Flask(__name__)


@app.route("/rango", methods=["POST", 'GET'])
def rango():
    rango = request.form['rango']
    contra_generada = generator_password(int(rango))

    return render_template('index.html', contra_generada=contra_generada)


if __name__ == '__main__':
    app.run(debug=True)
