import json
import models.user

user = models.user.Dinesh_users()

def create(event, context):
    if validate_data(event):
        try:
            param = json.loads(event['body'])
            user.saveUser(param)
            status_code = 200
            body = {
                    "message": "User created successfully"
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
        if param['name'] and param['username'] and param['email'] and param['password']:
            return True
        else:
            return False
    except:
        return False
