from flask import Flask
import pymysql
import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv()

app = Flask(__name__)

def get_db_connection():
    instance_conn = os.environ.get("INSTANCE_CONNECTION_NAME")

    return pymysql.connect(
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASS"],
        database=os.environ["DB_NAME"],
        unix_socket=f"/cloudsql/{instance_conn}"
    )

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users")
        users = cursor.fetchall()
        conn.close()
        return f"<pre>{users}</pre>"
    except Exception as e:
        return f"<pre>{e}</pre>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
