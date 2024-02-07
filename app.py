from cs50 import SQL
from flask import Flask, url_for, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "xj73nvn2896hb"


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


#very useful function [  SQL( )  ] provided by cs50 to help shorten the execution of further function like .execute etc
crdb = SQL("sqlite:///data/credentials.db")
bkdb = SQL("sqlite:///data/bookings1.db")
bk2db = SQL("sqlite:///data/bookings2.db")
bk3db = SQL("sqlite:///data/bookings3.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        result = crdb.execute("SELECT * FROM credentials WHERE EMAIL = ?", email)
        if len(result) == 0:
            return render_template("relogin.html")
        else:
            submitted_password = request.form.get("password")
            if check_password_hash(result[0]["PASSWORDS"],submitted_password) == True:
                session["name"] = request.form.get("email")
                return redirect("/area")
            else:
                return render_template("relogin.html")
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        crdb.execute("INSERT INTO credentials (FULLNAME,EMAIL,PASSWORDS) VALUES(?,?,?)",name,email,generate_password_hash(password))
        return redirect(url_for("login"))
    else:
        return render_template("register.html")


@app.route("/forget", methods=["GET"])
def forget():
        return render_template("forget.html")

@app.route("/area", methods=["GET", "POST"])
def area():
    return render_template("area.html")

@app.route("/particulars", methods=["GET", "POST"])
def particulars():
    if request.method == "POST":
        name = request.form.get("name")
        purpose = request.form.get("purpose")
        date = request.form.get("date")
        timestart = request.form.get("timestart")
        timeend = request.form.get("timeend")
        if session["space"] == "space1":
            condition1 = bkdb.execute("SELECT COUNT(*) AS count FROM bookings1 WHERE DATE = ? AND ((TIMESTART >= ? AND TIMEEND <= ?) OR (TIMESTART <= ? AND TIMEEND <= ?) OR (TIMESTART >= ? AND TIMESTART <= ?) OR (TIMEEND >= ? AND TIMEEND <= ?))", date,timestart,timeend,timestart,timeend,timestart,timeend,timestart,timeend)
            condition1_count = condition1[0]['count']
            if (condition1_count == 0):
                bkdb.execute("INSERT INTO bookings1 (NAME,PURPOSE,DATE,TIMESTART,TIMEEND) VALUES(?,?,?,?,?)",name,purpose,date,timestart,timeend)
                return redirect("/table")
            else:
                return render_template("particulars.html", error_message="Your booking overlaps an existing booking!")

        elif session["space"] == "space2":
            condition2 = bk2db.execute("SELECT COUNT(*) AS count FROM bookings2 WHERE DATE = ? AND ((TIMESTART >= ? AND TIMEEND <= ?) OR (TIMESTART <= ? AND TIMEEND <= ?) OR (TIMESTART >= ? AND TIMESTART <= ?) OR (TIMEEND >= ? AND TIMEEND <= ?))", date,timestart,timeend,timestart,timeend,timestart,timeend,timestart,timeend)
            condition2_count = condition2[0]['count']
            if (condition2_count == 0):
                bk2db.execute("INSERT INTO bookings2 (NAME,PURPOSE,DATE,TIMESTART,TIMEEND) VALUES(?,?,?,?,?)",name,purpose,date,timestart,timeend)
                return redirect("/table")
            else:
                return render_template("particulars.html", error_message="Your booking overlaps an existing booking!")

        else:
            condition3 = bk3db.execute("SELECT COUNT(*) AS count FROM bookings3 WHERE DATE = ? AND ((TIMESTART >= ? AND TIMEEND <= ?) OR (TIMESTART <= ? AND TIMEEND <= ?) OR (TIMESTART >= ? AND TIMESTART <= ?) OR (TIMEEND >= ? AND TIMEEND <= ?))", date,timestart,timeend,timestart,timeend,timestart,timeend,timestart,timeend)
            condition3_count = condition3[0]['count']
            if (condition3_count == 0):
                bk3db.execute("INSERT INTO bookings3 (NAME,PURPOSE,DATE,TIMESTART,TIMEEND) VALUES(?,?,?,?,?)",name,purpose,date,timestart,timeend)
                return redirect("/table")
            else:
                return render_template("particulars.html", error_message="Your booking overlaps an existing booking!")

    else:
        session["space"] = request.args.get("space")
        return render_template("particulars.html")


@app.route("/table", methods=["GET", "POST"])
def table():
    if request.method == "POST":
        session.clear()
        return render_template("login.html")
    else:
        if "space" in session and session["space"] == "space1":
            results1 = bkdb.execute("SELECT * FROM bookings1 ORDER BY DATE ASC;")
            return render_template("table.html", results = results1)
        elif "space" in session and session["space"] == "space2":
            results2 = bk2db.execute("SELECT * FROM bookings2 ORDER BY DATE ASC;")
            return render_template("table.html", results = results2)
        elif "space" in session and session["space"] == "space3":
            results3 = bk3db.execute("SELECT * FROM bookings3 ORDER BY DATE ASC;")
            return render_template("table.html", results = results3)
