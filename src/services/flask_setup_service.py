from datetime import datetime
from functools import wraps
from src.endpoints.rest import algo_blueprint
from flask import Blueprint, Flask, flash, redirect, url_for
# from flask_login import current_user
from flask_sock import Sock

class FlaskSetupService(object):

    def __init__(self, app, test_config=None, **configs):
        self.app = app
        self.configs(**configs)
#     def __init__(self, *args, **kwargs):
#         Flask.__init__(self, *args, **kwargs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value
        # if self.app.config["DEBUG"] == True:
        #     self.app.config.from_object('config.DevConfig')
        # else:
        #     self.app.config.from_object('config.ProdConfig')
        # # self.app.config.from_mapping(
        # #     SECRET_KEY='dev',
        # #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        # # )
        # # if test_config is None:
        # #     # load the instance config, if it exists, when not testing
        # #     app.config.from_pyfile('config.py', silent=True)
        # # else:
        # #     # load the test config if passed in
        # #     app.config.from_mapping(test_config)
        # # ensure the instance folder exists
        # try:
        #     os.makedirs(app.instance_path)
        # except OSError:
        #     pass
        # # db = SQLAlchemy(app)
        # # migrate = Migrate(app, db)
        # # with app.app_context():
        # #     db.create_all()
        self.add_blueprint_routes()

    def sock_setup(self):
        self.sock = Sock()
        self.sock.init_app(self.app)

    def add_blueprint_routes(self):
        self.app.register_blueprint(algo_blueprint)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)

    # def add_endpoint__sock(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
    #     while True:
    #         data = ws.receive()
    #         ws.send(data)

    # def check_expired(self, func):
    #     @wraps(func)
    #     def decorated_function(*args, **kwargs):
    #         if datetime.utcnow() > current_user.account_expires:
    #             flash("Your account has expired. Update your billing info.")
    #             return redirect(url_for('account_billing'))
    #         return func(*args, **kwargs)
    #     return decorated_function

    def run(self, **kwargs):
        self.app.run(**kwargs)