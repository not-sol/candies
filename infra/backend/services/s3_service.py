import boto3
from typing import List
import os


class S3Service:
    def __init__(self):
        self.s3_client = boto3.client("s3")
        self.bucket_name = os.environ.get("BUCKET_NAME")

    def list_files(self, user_id: str) -> List[dict]:
        """
        Returns a list of file metadata for a specific user.
        Each file is a dict: {'file_name': ..., 'size': ..., 'key': ...}
        """
        prefix = f"{user_id}/"
        response = self.s3_client.list_objects_v2(
            Bucket=self.bucket_name,
            Prefix=prefix
        )

        files = []
        if "Contents" in response:
            for obj in response["Contents"]:
                # Skip folder itself
                if obj["Key"].endswith("/"):
                    continue
                files.append({
                    "file_name": obj["Key"].replace(prefix, ""),
                    "size": obj["Size"],
                    "key": obj["Key"]
                })
        return files
