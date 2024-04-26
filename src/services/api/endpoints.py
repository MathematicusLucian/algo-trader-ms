# -*- coding: utf-8 -*-
from flask import Blueprint, Flask, g, request, jsonify
import json
import os
from flask_cors import CORS
from datetime import datetime, timedelta, time
import pandas as pd
from dotenv import load_dotenv  
from pathlib import Path
from markupsafe import escape
# from src.services.spider.jobs import apply_to_jobs
# from src.read_db import fetch_jobs_from_table
# from src.services.db.db import create_connection, is_table, create_table, read_table, query_table, update_table
from src.utils.utils import get_env_var, get_json_file, save_dataframe
from src.utils.common import get_config

env_path = Path('./src') / '.env'
load_dotenv(dotenv_path=env_path)
app = Flask(__name__)
CORS(app)

api_key = get_config('LIVECOINWATCH_API_KEY')
base_currency = get_config('BASE_CURRENCY')
coins = get_config('COINS')
route = Blueprint('default', __name__)

def get_config():
    config_file_name = get_env_var('CONFIG_FILE')
    CWD_DIR = os.getcwd()
    CONFIG_FILE_PATH = os.path.join(f"{CWD_DIR}/config/{config_file_name}")
    return get_json_file(CONFIG_FILE_PATH)

def save_jobs_to_database(db_config, list_of_jobs_scraped_by_spider):
    print(db_config)
    # freshly_scraped_jobs_df_cols_undefined = pd.DataFrame(list_of_jobs_scraped_by_spider)
    # columnsTitles = ['site_name','search__role_title','job_title','job_link','company','location','salary','date_fetch', 'date_application']
    # freshly_scraped_jobs_df = freshly_scraped_jobs_df_cols_undefined.reindex(columns=columnsTitles)            
    
    # save_dataframe(freshly_scraped_jobs_df)

    # CWD_DIR = os.getcwd()
    # PAR_DIR = os.path.abspath(os.path.join(CWD_DIR, os.pardir))
    # db_path = os.path.join(PAR_DIR, db_config[0]["db_path"])
    # conn = create_connection(db_path)
    
    # if conn is not None:    
    #     original_jobs = []
    #     table_name = db_config[0]["table_name"]

    #     if is_table(conn, table_name):
    #         existing_jobs = read_table(conn, table_name)
    #         existing_jobs_df = pd.DataFrame(existing_jobs)
    #         original_jobs = [job for job in freshly_scraped_jobs_df if job not in existing_jobs_df]
    #     else:
    #         original_jobs = freshly_scraped_jobs_df
    #     original_jobs_df = pd.DataFrame(original_jobs)
    #     original_jobs_df['date_loaded'] = datetime.now()
    #     original_jobs_df['date_loaded'] = original_jobs_df['date_loaded'].astype(str)

    #     if not is_table(conn, table_name):
    #         create_table(conn, original_jobs_df, table_name)
    #     else:
    #         update_table(conn, original_jobs_df, table_name)
    # else:
    #     print("Database connection failed")

@route.route("/api")
def index():
    return jsonify({"status": 200, "msg":"JobHunter Flask API"})

@route.route("/api/ping")
def ping():
    return jsonify({"status": 200, "msg":"I am the JobHunter Flask API"})

@route.route("/api/save_jobs/<jobs>")
def save_jobs(jobs):
    if request.method == 'POST':
        print (f"X: {escape(jobs)}")
        return jsonify({"status": 200, "msg":"I am the JobHunter Flask API"})
    else:
        return jsonify({"I only accept POST requests.":""})

@route.route('/api/jobs', methods=['GET'])
def run_model():
    scraper_config = get_config()
    db_config = scraper_config["db_config"]
    db_path = db_config[0]["db_path"]
    # conn = create_connection(db_path)
    # if conn is not None:
    #     table_name = db_config[0]["table_name"]
    #     if is_table(conn, table_name):
    #         existing_jobs = read_table(conn, table_name)
    #         return json.loads(existing_jobs.to_json(orient="records"))
    #     else:
    #         return {"Table does not exist":""}
    # else:
    #     return {"Database connection failed":""}