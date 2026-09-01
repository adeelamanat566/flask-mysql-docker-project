import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection settings
# Change these values according to your MySQL container.
MYSQL_HOST = os.environ.get("MYSQL_HOST", "sql")
MYSQL_PORT = int(os.environ.get("MYSQL_PORT", "3306"))
MYSQL_USER = os.environ.get("MYSQL_USER", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "adeel")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", "deveops")


def get_db_connection():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )


@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM users ORDER BY id DESC")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", users=users)


@app.route("/add", methods=["POST"])
def add_user():
    name = request.form["name"]
    email = request.form["email"]

   phone = request.form["phone"]
address = request.form["address"]

conn = get_db_connection()
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO users (name, email, phone, address)
    VALUES (%s, %s, %s, %s)
    """,
    (name, email, phone, address)
)
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
