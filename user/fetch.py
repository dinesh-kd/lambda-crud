import json
import models.user

user = models.user.Dinesh_users()

def fetch(event, context):
    if validate_data(event):
        try:
            param = event['pathParameters']
            user_data = user.getUser(param['user_id'])
            status_code = 200
            body = {
                   "data": user_data
            }
        except:
            status_code = 403
            body = {
                "message": "Something went wrong please try again"
            }
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
