
import os
import pymongo
from flask import Flask, render_template, g, redirect, url_for, request, session, flash
from flask_oidc import OpenIDConnect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from okta import UsersClient
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.secret_key = os.environ.get("SECRET_KEY")
app.config["OIDC_ID_TOKEN_COOKIE_NAME"] = "oidc_token"
oidc = OpenIDConnect(app)
okta_client = UsersClient("https://dev-9604636.okta.com",
                          os.environ.get("AUTH_TOKEN"))

mongo = PyMongo(app)


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


@app.route("/")
def index():
    reviews = mongo.db.reviews.aggregate([{'$sample': {'size': 3}}])
    return render_template("index.html", reviews=reviews)


@app.route("/dashboard")
@oidc.require_login
def dashboard():
    admin = os.environ.get("ADMIN")
    return render_template("dashboard.html", admin=admin)


@app.route("/add_review", methods=["POST"])
def add_review():
    if request.method == "POST":
        review = {
            "firstName": g.user.profile.firstName,
            "lastName": g.user.profile.lastName,
            "email": g.user.profile.email,
            "stars": request.form.get("stars"),
            "review": request.form.get("review")
        }
        mongo.db.reviews.insert_one(review)
        flash("Task Successfully Added")
        return redirect(url_for("dashboard"))
    return render_template("dashboard.html")


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
