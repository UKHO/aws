from urllib.parse import unquote_plus
import os
import boto3

s3 = boto3.client("s3")


def handle(event, context):
    destination_bucket = os.getenv("DESTINATION_BUCKET")

    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])
        print(f"Copying s3://{bucket}/{key} to s3://{destination_bucket}/{key}")
        s3.copy_object(
            CopySource={"Bucket": bucket, "Key": key},
            Bucket=destination_bucket,
            Key=key,
        )
