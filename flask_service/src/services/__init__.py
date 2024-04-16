from flask import Blueprint, Flask, flash, redirect, url_for
# from flask_login import current_user
from flask_service.src.services.flask_setup_service import FlaskSetupService
from flask_sock import Sock
from settings import config
from src.utils.common import get_config, register_blueprints
# from .sentiment_service import *
# from .x_service import x_archive
# from .scraping_service import *
# from .crypto_analysis import *
from .metals_data_service import *

def create_app(config_type, package_name, package_path):
    flask_setup = Flask(__name__, instance_relative_config=True)
    app = FlaskSetupService(flask_setup, test_config=None)
    # register_blueprints(app, package_name, package_path)
    return app

def create_app_blueprint(config): #Flask app as RMIS instance
    return create_app(config, __name__, __path__)