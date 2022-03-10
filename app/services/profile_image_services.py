from werkzeug.exceptions import BadRequest
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from os import getenv
import boto3
import secrets


def upload_and_get_url(data: FileStorage):
    content_type = data.content_type
    verify_content(content_type)    

    return upload_to_cloud(data)

def verify_content(content: str):
    allowed_extensions =["png", "jpg", "jpeg"]
    extension_received = content.split("/")[-1]
    content_type = content.split("/")[0]

    if not extension_received in allowed_extensions:
        message = {"Error": "Extension not allowed."}
        raise BadRequest(description=message)

    if content_type != "image":
        message = {"Error": "The file must be image."}
        raise BadRequest(description=message)


def upload_to_cloud(data: FileStorage):
    s3 = boto3.resource("s3")

    bucket_location = getenv("BUCKET_REGION")
    bucket_name = getenv("BUCKET_NAME")
    bucket = s3.Bucket(bucket_name)

    key_name = secrets.token_urlsafe(64)

    bucket.put_object(
        Key=key_name, 
        Body=data,
        ACL='public-read',
        ContentType="media-type",
    )

    url = f"https://{bucket_name}.s3.{bucket_location}.amazonaws.com/{key_name}"

    return url, key_name

def verify_names(data: FileStorage) -> str:
    name = data.name
    file_name  = data.filename.split(".")[:-1]
    file_name = secure_filename(" ".join(file_name))

    if not name:
        message = {"Error": "A empty name has been send."}

        raise BadRequest(description=message)

    if not file_name:
        message = {"Error": "File name not allowed."}

        raise BadRequest(description=message)

    return file_name

def delete_object_from_cloud(id: str):
    s3_client = boto3.client("s3")
    bucket_name = getenv("BUCKET_NAME")

    response = s3_client.delete_object(
        Bucket = bucket_name,
        Key = id
    )


    
