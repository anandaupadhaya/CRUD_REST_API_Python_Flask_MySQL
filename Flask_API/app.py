from flask import Flask
app = Flask(__name__)


app.config["DEBUG"] = True
@app.route("/")
def Dashboard():
    return("Welcome to Flask API Learning")

@app.route("/home")
def home():
    return(" This is the Homepage")

import user_signup
import Sql_Conn
from Sql_Conn import SQL_CONNECTOR
from flask import request

obj = SQL_CONNECTOR()

@app.route("/getallemp")
def getallemp():
    return obj.getallemp()

@app.route("/addemp", methods = ["POST"])
def addemp():
    return obj.addnewemp(request.form)

@app.route("/update", methods = ["PUT"])
def updateemp():
    return obj.updateemp(request.form)

@app.route("/delete/<id>", methods = ["DELETE"])
def deleteemp(id):
    return obj.deleteemp(id)


