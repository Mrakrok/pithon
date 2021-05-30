from flask import Flask, request, render_template, redirect
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/", methods = ["POST"])
def checklogin():
    UN = request.form["username"]
    PW = request.form["password"]

    sqlconnection = sqlite3.Connection(currentlocation + "\login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password From Usert WHERE Username = {un} AND Password = {pw}".format(un = UN, pw = PW )

    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows) ==1:
        return render_template("LoggedIn.html")
    else:
        return redirect("/register")

@app.route("/register", methods= ["GET", "POST"])
def registerpage():
    if request.method == "POST":
        dUN = request.form["DUsername"]
        dPW = request.form["DPassword"]
        Uemail = request.form["Emaluser"]
        sqlconnection = sqlite3.Connection(currentlocation + "\login.db")
        cursor = sqlconnection.cursor()
        query1 = "INSERT INTO Users VALUES("{u}","{p}","{e}")".format(u = dUN, p = dPW, e = Uemail)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect ("/")
    return render_template("Register.html")


if __name__ == "__main__":
    app.run()