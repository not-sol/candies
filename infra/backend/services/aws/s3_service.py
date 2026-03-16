import boto3
from typing import List, Dict


class S3Service:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.s3 = boto3.client("s3")

    def generate_presigned_url(self, key: str, expires_in: int = 3600):
        url = self.s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": self.bucket_name, "Key": key},
            ExpiresIn=expires_in,
        )
        return url

    def list_files(self) -> List[Dict]:
        response = self.s3.list_objects_v2(Bucket=self.bucket_name)
        files = []
        for obj in response.get("Contents", []):
            files.append({
                "key": obj["Key"],
                "size": obj["Size"]
            })
        return files
