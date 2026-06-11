from flask import Flask, render_template, request, Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('login_email')
        password = request.form.get('login_password')



    return render_template('login.html')

@user_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('cadastro_nome')
        email = request.form.get('cadastro_email')
        idade = request.form.get('cadastro_idade')
        telefone = request.form.get('cadastro_telefone')
        password = request.form.get('cadastro_password')
    return render_template('cadastro.html')

@user_bp.route('/dados_user', methods=['GET'])
def dados_user():
    user = {'nome': 'Gabriel', 
            'email': 'bielandre@gmail.com', 
            'idade': 20, 
            'telefone': 1199999999}

    return render_template('dados_user.html', user=user)

