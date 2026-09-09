import os
import socket
import pymysql
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "password")
DB_NAME = os.environ.get("DB_NAME", "testdb")

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

def init_db():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL
                )
            """)
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database init warning: {e}")

@app.route('/', methods=['GET'])
def get_info():
    pod_ip = socket.gethostbyname(socket.gethostname())
    return jsonify({"status": "200 OK", "pod_ip": pod_ip}), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing data"}), 400
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
        conn.commit()
        conn.close()
        return jsonify({"message": "User added"}), 201
    except pymysql.MySQLError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
        conn.close()
        return jsonify(users), 200
    except pymysql.MySQLError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)