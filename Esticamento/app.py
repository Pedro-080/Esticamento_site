from flask import Flask, render_template,request
from flask_wtf.csrf import CSRFProtect
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import StringField

import pandas as pd

app = Flask(__name__)
app_version = 'pre-alpha 0.1'
csrf = CSRFProtect(app)

df = pd.read_csv('Esticamento/data/Dados_Cabos.csv')

class MyForm(FlaskForm):
    input_field = StringField('Campo de texto',validators=[DataRequired()])

@app.route('/')
def index():
    # Convertendo as linhas do dataframe em uma lista
    options = list(df['Tag'].unique())

    # Renderizando o template HTML e passando a lista suspensa como contexto
    return render_template('index.html', options=options,app_version=app_version)

@app.route('/result', methods=['POST'])
def result():
    selected_option = request.form.get('select')
    filtred_df = df[df['Tag'] == selected_option]
    return render_template('result.html',table=filtred_df.to_html())


# @app.route('/outra_pagina')
# def outra_pagina():   
#     return render_template('index_copy.html',app_version=app_version)




@app.route('/processar-formulario',methods=['GET','POST'])
def processar_formulario():
    if request.method == 'POST':
        select_field = request.form['select_field']
        text_field = ''
        
        if select_field == 'option_1':
            text_field = 'Você escolheu a opção 1!'
        if select_field == 'option_2':
            text_field = 'Você escolheu a opção 2!'
        if select_field == 'option_3':
            text_field = 'Você escolheu a opção 3!'
        
        return render_template('index_copy.html',text_field=text_field,app_version=app_version)
    
    return render_template('index_copy.html',app_version=app_version)


@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        print(request.form)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)