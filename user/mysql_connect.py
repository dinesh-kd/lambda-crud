import peewee as pw
import boto3
client = boto3.client('ssm', region_name="us-east-1")

resp = client.get_parameters(
    Names=['dinesh_rds_db_username', 'dinesh_rds_db_password', 'dinesh_rds_db_name', 'dinesh_rds_db_endpoint' ]
)

for param in resp['Parameters']:
    if param['Name'] == 'dinesh_rds_db_username':
        name = param['Value']
    if param['Name'] == 'dinesh_rds_db_password':
        password = param['Value']
    if param['Name'] == 'dinesh_rds_db_name':
        db_name = param['Value']
    if param['Name'] == 'dinesh_rds_db_endpoint':
        rds_host = param['Value']

def connect():
    try:
        return pw.MySQLDatabase(db_name, host= rds_host, port=3306, user=name,passwd=password)
    except:
        return 0
