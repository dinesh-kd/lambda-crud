import os, sys

here = os.path.dirname(os.path.realpath(__file__))
root = os.path.dirname(here)
sys.path.append(os.path.join(root))

import mysql_connect as mysql_connect
import peewee as pw

db = mysql_connect.connect()

class Dinesh_users(pw.Model):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=25)
    username = pw.CharField(max_length=25)
    email = pw.CharField(max_length=25)
    password = pw.TextField()
    created_on = pw.DateTimeField()
    updated_on = pw.DateTimeField()

    class Meta:
        database = db

    def getUser(self, id):
        user = Dinesh_users.get(Dinesh_users.id == id)
        return {'id': user.id, 'name': user.name, 'username': user.username, 'email': user.email}

