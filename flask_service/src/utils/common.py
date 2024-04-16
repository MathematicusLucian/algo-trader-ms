# -*- coding: utf-8 -*-
import os
import pkgutil
import importlib
from flask import Blueprint
from pathlib import Path
from src.utils.utils import get_envar
from src.endpoints import get_root

def get_config(envar_key):
    get_envar(envar_key)

# returns rv (list): list of blueprints
def register_blueprints(app, package_name, package_path):
    # blue_prints = []
    # for _, name, _ in pkgutil.iter_modules(package_path):
    #     files = importlib.import_module('%s.%s' % (package_name, name))
    #     for item in dir(files):
    #         item = getattr(files, item)
    #         if isinstance(item, Blueprint):
    #             app.register_blueprint(item)
    #         blue_prints.append(item)
    # return blue_prints
    app.add_endpoint('/', 'root', get_root, methods=['GET'])
    return app