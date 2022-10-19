#import mysql.connector
#conn = mysql.connector.connect(host="localhost", user="root", password="password", database="paralleldots")

from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'paralleldots'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)