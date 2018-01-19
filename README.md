# Lambda Crud

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
    #### Invoke local
    ```javascript
        serverless invoke local --function create --path mock/create.json
    ```
  * GET - https://tvq543j6s0.execute-api.us-east-1.amazonaws.com/dev/users/{user_id}
    #### Invoke local
    ```javascript
        serverless invoke local --function fetch --path mock/fetch.json
    ```
  * DELETE - https://tvq543j6s0.execute-api.us-east-1.amazonaws.com/dev/users/{user_id}
    #### Invoke local
    ```javascript
        serverless invoke local --function delete --path mock/delete.json
    ```
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
    #### Invoke local
    ```javascript
        serverless invoke local --function update --path mock/update.json
    ```

