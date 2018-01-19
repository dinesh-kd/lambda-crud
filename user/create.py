import json
import mysql_connect
import datetime

def create(event, context):
    if validate_data(event):
        try:
            conn = mysql_connect.connect()
            with conn.cursor() as cursor:
                param = json.loads(event['body'])
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


def validate_data(event):
    try:
        param = json.loads(event['body'])
        if param['name'] and param['username'] and param['email'] and param['password']:
            return True
        else:
            return False
    except:
        return False
