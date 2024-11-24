from flask import Blueprint, jsonify, request
import sqlite3

bp = Blueprint('routes', __name__)

DATABASE = 'baseball-dump.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@bp.route('/players', methods=['GET'])
def get_players():
    conn = get_db_connection()
    try:
        query = "SELECT DISTINCT player_name FROM statcast LIMIT 100;"
        players = conn.execute(query).fetchall()
        conn.close()
        return jsonify([dict(row) for row in players])
    except sqlite3.OperationalError as e:
        return jsonify({"error": str(e)}), 500
