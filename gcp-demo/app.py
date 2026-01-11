from flask import Flask
import pymysql
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()



def get_db_connection():
    return pymysql.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        database=os.getenv("DB_NAME"),
        unix_socket=os.getenv('INSTANCE_CONNECTION_NAME')
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


