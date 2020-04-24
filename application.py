import datetime

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
        
    return render_template("index.html",  notes=session["notes"])

@app.route("/more")
def more():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    headline = "Hello, World"
    names = ["Yatin", "Vishal", "Shreyans", "Kishan"]
    return render_template("more.html", headline=headline, new_year=new_year, names=names)

@app.route("/Yatin")
def Yatin():
    return "Hello, Yatin!"

@app.route("/hello1", methods=["GET", "POST"])
def hello1():
    if request.method == "GET":
        return "Please submit the form insted."
    else:
        name = request.form.get("name")
        return render_template("hello1.html", name=name)

@app.route("/NAME")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}! </h1>"

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

