import os
import json
from flask import Flask, jsonify, request, session
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_mail import Mail, Message
from src.endpoints import algo_blueprint

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if app.config["DEBUG"] == True:
        app.config.from_object('config.DevConfig')
    else:
        app.config.from_object('config.ProdConfig')
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )
    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # db = SQLAlchemy(app)
    # migrate = Migrate(app, db)
    # with app.app_context():
    #     db.create_all()
    app.register_blueprint(algo_blueprint)
    return app

if __name__ == '__main__':
   app = create_app()
#    set FLASK_APP=main
   app.run(debug=True, port=5001)