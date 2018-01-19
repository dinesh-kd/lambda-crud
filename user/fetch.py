import json
import mysql_connect
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def fetch(event, context):
    if validate_data(event):
        try:
            conn = mysql_connect.connect()
            param = event['pathParameters']
            with conn.cursor() as cursor:
                sql = "select `id`,`name`,`username`,`email` from `dinesh_users` where id = %s;"
                cursor.execute(sql, param['user_id'])
                result = cursor.fetchone()
                conn.commit()
                headers = ['id', 'name', 'username', 'email']
                user_data = dict(zip(headers, result))
                status_code = 200
                body = {
                    "data": user_data
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
            "message": "User id is required"
        }
    response = {
        "statusCode": status_code,
        "body": json.dumps(body)
    }
    return response


def validate_data(event):
    try:
        param = event['pathParameters']
        if param['user_id']:
            return True
        else:
            return False
    except:
        return False
