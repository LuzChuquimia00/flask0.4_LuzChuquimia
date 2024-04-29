import os 
import sqlite3

import click
from flask import current_app, g 

#Constante con nombre y locación del database
db_folder = current_app.instance_path
db_name = 'Musicas.sqlite'
db_file = os.path.join(db_folder,db_name)
db_sql_file = 'datos.sql'

def get_db():
    if 'db' not in g: 