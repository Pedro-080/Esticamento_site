from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('Esticamento/data/Dados_Cabos.csv')

@app.route('/')
def index():
    # Convertendo as linhas do dataframe em uma lista
    options = list(df['Tag'])

    # Renderizando o template HTML e passando a lista suspensa como contexto
    return render_template('index.html', options=options)

if __name__ == '__main__':
    app.run(debug=True)