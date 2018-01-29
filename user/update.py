import json
import models.user

user = models.user.Dinesh_users()


def update(event, context):
    if validate_data(event):
        try:
            param = json.loads(event['body'])
            user_param = event['pathParameters']
            user.updateUser(user_param['user_id'], param)
            status_code = 200
            body = {
                    "message": "User updated successfully"
            }
        except:
            status_code = 403
            body = {
                "message": "Something went wrong please try again"
            }
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
