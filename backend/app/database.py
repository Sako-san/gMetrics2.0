import sqlite3
from flask import current_app, g

DATABASE = 'baseball-dump.db'

def get_db_connection():
    """
    Opens a new database connection if not already connected.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row  # Allows accessing rows as dictionaries
    return g.db

def close_db_connection(e=None):
    """
    Closes the database connection if it exists.
    """
    db = g.pop('db', None)
    if db is not None:
        db.close()
