from flask import Flask, render_template, request
from routes.main_routes import main_bp
from routes.user_routes import user_bp

app = Flask(__name__)


app.register_blueprint(user_bp)
app.register_blueprint(main_bp)


if __name__ == '__main__':
    app.run(debug=True)
