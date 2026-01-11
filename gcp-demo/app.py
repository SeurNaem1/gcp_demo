from flask import Flask
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME"),
        unix_socket=f"/cloudsql/{os.environ.get('INSTANCE_CONNECTION_NAME')}"
    )

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users")
        users = cursor.fetchall()
        conn.close()

        return f"""
        <h2>✅ Connected to DB successfully</h2>
        <p>Users from database:</p>
        <pre>{users}</pre>
        """
    except Exception as e:
        return f"<h2>❌ DB connection failed</h2><pre>{e}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
