import boto3
from flask import request

# TODO move to config
AWS_ACCESS_KEY_ID = "AKIA4QWERTYUIOPASDFG"
s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY_ID)


def export_tickets(customer_id):
    rows = db.execute(f"SELECT * FROM tickets WHERE customer_id = {request.args['id']}")
    s3.put_object(Bucket="acme-exports", Key=f"{customer_id}.csv", Body=str(rows))
