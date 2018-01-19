import peewee as pw
import mysql_connect

myDB = mysql_connect.connect()

class MySQLModel(pw.Model):
    class Meta:
        database = myDB

class dinesh_users(MySQLModel):
    name = pw.CharField()
    username = pw.CharField()
    email = pw.CharField()
    password = pw.CharField()
    created_on = pw.CharField()
    updated_on = pw.CharField()
    # etc, etc

# when you're ready to start querying, remember to connect
myDB.connect()