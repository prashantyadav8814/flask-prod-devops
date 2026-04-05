from flask import Flask, render_template
from config import Config
import mysql.connector

app = Flask(__name__)
app.config.from_object(Config)

def get_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from Production DevOps Project 🚀'")
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/health')
def health():
    return {"status": "UP"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
