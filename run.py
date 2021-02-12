
import os
import pymongo
from flask import (Flask, render_template, g, redirect,
                   url_for, request, flash)
from flask_oidc import OpenIDConnect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import date
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
okta_client = UsersClient("https://dev-5976059.okta.com",
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
    today = date.today()
    api_key = os.environ.get("API_KEY")
    mongo.db.reservations.delete_many({"date":
                                      {"$lt": int(today.strftime("%Y%m%d"))}})
    print({"date": {"$lt": today.strftime("%Y%m%d")}})
    return render_template("index.html", reviews=reviews, api_key=api_key)


@app.route("/reviews")
def reviews():
    reviews = list(mongo.db.reviews.find({}))
    return render_template("reviews_all.html", reviews=reviews)


@app.route("/dashboard")
@oidc.require_login
def dashboard():
    admin = os.environ.get("ADMIN")
    user = g.user.profile.email
    user_review = list(mongo.db.reviews.find(
            {"email": user}).sort("_id", pymongo.DESCENDING))
    user_reservation = list(mongo.db.reservations.find(
            {"email": user}).sort("date", pymongo.ASCENDING))
    admin_review = list(mongo.db.reviews.find({}))
    admin_reservation = list(mongo.db.reservations.find({}))
    return render_template("dashboard.html",
                           admin=admin,
                           user_review=user_review,
                           user_reservation=user_reservation,
                           admin_review=admin_review,
                           admin_reservation=admin_reservation)


@app.route("/add_reservation", methods=["GET", "POST"])
def add_reservation():
    if request.method == "POST":
        booked_date = request.form.get("date")
        date_day = booked_date[0:2]
        date_month = booked_date[3:5]
        date_year = booked_date[6:10]
        int_date = date_year + date_month + date_day
        reservation = {
            "firstName": g.user.profile.firstName,
            "lastName": g.user.profile.lastName,
            "email": g.user.profile.email,
            "date": int(int_date),
            "shown_date": request.form.get("date"),
            "slot": request.form.get("slot"),
            "covers": request.form.get("covers"),
            "requirements": request.form.get("requirements")
        }
        date_slot_query = {"shown_date": request.form.get("date"),
                           "slot": request.form.get("slot")}
        existing_reservations = mongo.db.reservations.find(date_slot_query)
        new_covers = request.form.get("covers")
        cover_count = sum(
                [int(reservation["covers"])
                 for reservation in existing_reservations])
        total_covers = int(new_covers) + int(cover_count)
        remaining_covers = 30 - int(cover_count)
        remaining_message = "Sorry, we only have " \
            + str(remaining_covers) \
            + " seats remaining for that session"
        if total_covers < 30:
            mongo.db.reservations.insert_one(reservation)
            flash("Reservation successfully booked")
            return redirect(url_for("dashboard"))
        else:
            flash(remaining_message)
            return redirect(url_for("dashboard"))
    return render_template("dashboard.html")


@app.route("/edit_reservation/<reservation_id>", methods=["GET", "POST"])
@oidc.require_login
def edit_reservation(reservation_id):
    if request.method == "POST":
        booked_date = request.form.get("date")
        date_day = booked_date[0:2]
        date_month = booked_date[3:5]
        date_year = booked_date[6:10]
        int_date = date_year + date_month + date_day
        submit = {
            "firstName": g.user.profile.firstName,
            "lastName": g.user.profile.lastName,
            "email": g.user.profile.email,
            "date": int(int_date),
            "shown_date": request.form.get("date"),
            "slot": request.form.get("slot"),
            "covers": request.form.get("covers"),
            "requirements": request.form.get("requirements")
        }
        date_slot_query = {"shown_date": request.form.get("date"),
                           "slot": request.form.get("slot")}
        existing_reservations = mongo.db.reservations.find(date_slot_query)
        new_covers = request.form.get("covers")
        cover_count = sum(
                [int(reservation["covers"])
                 for reservation in existing_reservations])
        total_covers = int(new_covers) + int(cover_count)
        remaining_covers = 30 - int(cover_count)
        remaining_message = "Sorry, we only have " \
            + str(remaining_covers) \
            + " seats remaining for that session." \
            + " Your reservation has not been updated."
        if total_covers < 30:
            mongo.db.reservations.replace_one({"_id":
                                               ObjectId(reservation_id)},
                                              submit)
            flash("Your Reservation Has Been Updated", 'update')
            return redirect(url_for("dashboard"))
        else:
            flash(remaining_message)
            return redirect(url_for("dashboard"))
    reservation = mongo.db.reservations.find_one({"_id":
                                                  ObjectId(reservation_id)})
    return render_template("edit_reservation.html", reservation=reservation)


@app.route("/delete_reservation/<reservation_id>")
def delete_reservation(reservation_id):
    mongo.db.reservations.remove({"_id": ObjectId(reservation_id)})
    flash("Your Reservation has been cancelled!", 'update')
    return redirect(url_for("dashboard"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        today = date.today()
        review = {
            "firstName": g.user.profile.firstName,
            "lastName": g.user.profile.lastName,
            "email": g.user.profile.email,
            "date": today.strftime("%d/%m/%Y"),
            "stars": request.form.get("stars"),
            "review": request.form.get("review")
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("dashboard"))
    return render_template("dashboard.html")


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
@oidc.require_login
def edit_review(review_id):
    if request.method == "POST":
        today = date.today()
        submit = {
            "firstName": g.user.profile.firstName,
            "lastName": g.user.profile.lastName,
            "email": g.user.profile.email,
            "date": today.strftime("%d/%m/%Y"),
            "stars": request.form.get("stars"),
            "review": request.form.get("review")
        }
        mongo.db.reviews.replace_one({"_id": ObjectId(review_id)}, submit)
        flash("Your Review Has Been Updated", 'update')
        return redirect(url_for("dashboard"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Your Review Was Deleted", 'update')
    return redirect(url_for("dashboard"))


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for("index"))


@app.route("/reload")
def reload():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
