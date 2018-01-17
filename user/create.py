import json
import mysql_connect
import logging
import datetime

def create(event, context):
    conn = mysql_connect.connect()
    print(conn)
    param = json.loads(event['body'])
    print(param)
    if validate_data(param):
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO `dinesh_users` (`name`,`username`,`email`,`password`,`created_on`) VALUES (%s,%s,%s,%s,%s);"
                cursor.execute(sql, (
                param['name'], param['username'], param['email'], param['password'],
                datetime.datetime.now()))
                conn.commit()
                status_code = 200
                body = {
                    "message": "User created successfully"
                }
        except:
            status_code = 403
            body = {
                "message": "Something went wrong please try again"
            }
        finally:
            conn.close()
    else:
        status_code = 400
        body = {
            "message": "Please enter all the values"
        }
    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }
    return response


def validate_data(param):
    try:
        if param['name'] and param['username'] and param['email'] and param['password']:
            return True
        else:
            return False
    except:
        return False
