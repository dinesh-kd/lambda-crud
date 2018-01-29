import os, sys
import datetime

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

    def saveUser(self, data):
        new_user = Dinesh_users(name=data['name'], username=data['username'], email=data['email'], password=data['password'],
                                created_on=datetime.datetime.now())
        return new_user.save()

    def updateUser(self, id, data):
        updated_user = Dinesh_users(name=data['name'], username=data['username'], email=data['email'], password=data['password'],
                                    updated_on=datetime.datetime.now())
        updated_user.id = id
        return updated_user.save()

    def deleteUser(self, id):
        delete_user = Dinesh_users(id=id)
        return delete_user.delete_instance()

users_db = Dinesh_users()
print(users_db.getUser(10))