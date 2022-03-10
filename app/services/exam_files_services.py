from werkzeug.exceptions import BadRequest
from werkzeug.datastructures import FileStorage
from os import getenv
import boto3
import secrets

def upload_file(data: FileStorage) -> str:
    content_type = data.content_type
    verify_content(content_type)

    verify_name(data)

    data_type = content_type.split("/")[-1]

    return upload_to_cloud(data, data_type)

def verify_content(content: str):
    allowed_extensions =["png", "jpg", "jpeg", "pdf"]
    extension_received = content.split("/")[-1]

    if not extension_received in allowed_extensions:
        message = {"Error": "Extension not allowed. Verify the type of content."}
        raise BadRequest(description=message)
    

def upload_to_cloud(data: FileStorage, type: str) -> str:
    s3 = boto3.resource("s3")

    bucket_location = getenv("BUCKET_REGION")
    bucket_name = getenv("BUCKET_NAME")
    bucket = s3.Bucket(bucket_name)

    key_name = secrets.token_urlsafe(64)

    content_type = "application/pdf" if type == "pdf" else "media-type"

    bucket.put_object(
        Key=key_name, 
        Body=data,
        ACL='public-read',
        ContentType=content_type,
    )

    url = f"https://{bucket_name}.s3.{bucket_location}.amazonaws.com/{key_name}"

    return url


def get_key_file(url_file: str) -> str:
    id = url_file.split(".com/")[-1]

    return id

def verify_name(data: FileStorage) -> str:
    name = data.name

    if not name:
        message = {"Error": "A empty name has been send."}

        raise BadRequest(description=message)