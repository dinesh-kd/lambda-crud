# Lamabda Crud

## endpoints:
  * POST - https://tvq543j6s0.execute-api.us-east-1.amazonaws.com/dev/users
    #### Body
    ```javascript
        {
            "name":"Dinesh",
            "username": "dinesh-kd",
            "email":"dinesh.kd@diversey.com",
            "password": "Dinesh@123"
        }
    ```
  * GET - https://tvq543j6s0.execute-api.us-east-1.amazonaws.com/dev/users/{user_id}
  * DELETE - https://tvq543j6s0.execute-api.us-east-1.amazonaws.com/dev/users/{user_id}
  * PUT - https://tvq543j6s0.execute-api.us-east-1.amazonaws.com/dev/users/{user_id}
    #### Body
    ```javascript
        {
            "name":"Dinesh",
            "username": "dinesh-kd",
            "email":"dinesh.kd@diversey.com",
            "password": "Dinesh@123"
        }
    ```

