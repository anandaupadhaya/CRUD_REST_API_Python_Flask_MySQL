from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


'''''

#import pandas as pd
import pymysql
import flask
from flask import request, json, jsonify, flash
from flask_mysqldb import MySQL
import mysql.connector
conn = mysql.connector.connect(host="localhost", user="root", password="password", database="paralleldots")


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods = ["GET"])
def home():
    return("Welcome")

@app.route('/emp')
def emp():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM Employee")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/emp/')
def emp_details(emp_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, email, phone, address FROM emp WHERE id =%s", emp_id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#emp_data = pd.read_sql_query("SELECT * FROM Employee", conn)
#print(emp_data)

if __name__ == '__main__':
    app.run()

'''''