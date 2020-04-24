import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    headline = "Hello, World"
    names = ["Yatin", "Vishal", "Shreyans", "Kishan"]
    return render_template("index.html", headline=headline, new_year=new_year, names=names)

@app.route("/Yatin")
def Yatin():
    return "Hello, Yatin!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}! </h1>"

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

@app.route("/more")
def more():
    return render_template("more.html")
