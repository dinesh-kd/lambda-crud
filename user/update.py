import json
import mysql_connect
import datetime

def update(event, context):
    if validate_data(event):
        try:
            conn = mysql_connect.connect()
            param = json.loads(event['body'])
            user_param = event['pathParameters']
            with conn.cursor() as cursor:
                sql = "UPDATE `dinesh_users` set `name` = %s,`username` = %s,`email` = %s,`password` = %s,`updated_on` = %s where id = %s "
                cursor.execute(sql, (
                param['name'], param['username'], param['email'], param['password'],
                datetime.datetime.now(), user_param['user_id']))
                conn.commit()
                status_code = 200
                body = {
                    "message": "User updated successfully"
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
        user_param = event['pathParameters']
        if param['name'] and param['username'] and param['email'] and param['password'] and user_param['user_id']:
            return True
        else:
            return False
    except:
        return False
