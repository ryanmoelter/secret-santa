#internal
from dbOperations import dbConn

#external
import json
import psycopg2 as pg
from psycopg2 import sql

 
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

class Person:

    def __init__(self,name):
        self.name = name
    
    def name(self):
        return str(self.name)

@app.route("/")
def createGroupPage():
    return render_template("index.html")

@app.route("/add-person",methods=["POST"])
def addPerson():
    person = request.form.get("name")
    name = Person(person).name
    query = """insert into group_members(Name) values (%s)"""
    dbConn.execute_insert(query,name)
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)
    
