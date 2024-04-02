# run.py

from flask import Flask
from routes import api_bp
from settings import config

def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(config[env_name])

    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True, port=5001)