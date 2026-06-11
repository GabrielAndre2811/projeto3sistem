from flask import Flask, render_template, request, Blueprint

main_bp = Blueprint('main', __name__, url_prefix='/')

@main_bp.route('/')
def home():
    return render_template('home.html')