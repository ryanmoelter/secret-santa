from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)


@app.route("/")
def createGroupPage():
    return render_template("index.html")

@app.route("/add-person",methods=["POST"])
def addPerson():
    return redirect("/")