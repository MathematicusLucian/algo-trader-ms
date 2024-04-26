# -*- coding: utf-8 -*-
import os
from src.services.api import create_app_blueprint
from src.utils.common import get_config

flask_config = get_config('FLASK_CONFIG')
config = flask_config if flask_config!=None else 'default'
# print('CFG',config)
application = create_app_blueprint(config)

# # -*- coding: utf-8 -*-
# import os
# from src.services import create_app, create_app_blueprint
# from src.utils.common import get_config

# flask_config = get_config('FLASK_CONFIG')
# config = flask_config if flask_config!=None else 'default'
# application = create_app_blueprint(config)