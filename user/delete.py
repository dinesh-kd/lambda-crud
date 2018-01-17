import json
import mysql_connect
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def delete(event, context):
    conn = mysql_connect.connect()
    param = event['pathParameters']
    if validate_data(param):
        try:
            with conn.cursor() as cursor:
                sql = "delete from `dinesh_users` where id = %s;"
                cursor.execute(sql, param['user_id'])
                result = cursor.fetchone()
                conn.commit()
                status_code = 200
                body = {
                    "message": "User removed successfully"
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


def validate_data(param):
    try:
        if param['user_id']:
            return True
        else:
            return False
    except:
        return False
