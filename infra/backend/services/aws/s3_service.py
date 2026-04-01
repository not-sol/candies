import boto3
import os
from typing import List, Dict


class S3Service:
    def __init__(self):
        self.bucket_name = os.getenv("S3_BUCKET")
        self.s3 = boto3.client("s3")

    def generate_presigned_url(self, key: str, expires_in: int = 3600):
        url = self.s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": self.bucket_name, "Key": key},
            ExpiresIn=expires_in,
        )
        return url


def list_files(self, username: str) -> List[Dict]:
    response = self.s3.list_objects_v2(
        Bucket=self.bucket_name,
        Prefix=f"{username}/"
    )

    objects = response.get("Contents", [])

    user_files = []
    for obj in objects:
        user_files.append({
            "key": obj["Key"],
            "size": obj["Size"]
        })

    return user_files
