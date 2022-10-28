import json
import mysql.connector
from app import app
import pymysql.cursors


class SQL_CONNECTOR:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost", user="root", password="password", database="paralleldots")
            self.conn.autocommit = True
            self.cur = self.conn.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Some Error")


    def getallemp(self):
        self.cur.execute("SELECT * FROM Employee")
        result = self.cur.fetchall()
        return json.dumps(result)

    def addnewemp(self, data):
        self.cur.execute(f"Insert into Employee(Eid, E_name, Department) VALUES ('{data['Eid']}', '{data['E_name']}', '{data['Department']}' )")
        #print(data['Department'])
        return("This function adds new Employee ")

    def updateemp(self, data):
        self.cur.execute(f"UPDATE Employee SET E_name ='{data['E_name']}', Department ='{data['Department']}' WHERE Eid = {data['Eid']} ")
        #print(data['Department'])
        if self.cur.rowcount > 0:
            return("This function updates Employee records ")
        else:
            return("Nothing to update")

    def deleteemp(self, id):
        self.cur.execute(f" DELETE from Employee WHERE Eid = {id} ")
        #print(data['Department'])
        if self.cur.rowcount > 0:
            return("This function deletes Employee records ")
        else:
            return("Nothing to delete")