from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "root"),
        database=os.getenv("MYSQL_DATABASE", "taskdb")
    )


@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    tasks = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title, status) VALUES (%s, %s)",
        (title, "Pending")
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


@app.route("/complete/<int:id>", methods=["POST"])
def complete_task(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status = 'Completed' WHERE id = %s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s",
        (id,)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
