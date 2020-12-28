import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "192.168.1.208"),
        port=int(os.environ.get("PORT", "5000")))
