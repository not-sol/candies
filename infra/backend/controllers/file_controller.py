from fastapi import APIRouter
from typing import List
from services.aws.s3_service import S3Service
from models.file_model import FileResponse

router = APIRouter()

bucketName = "candies-try-bucket"


@router.get("", response_model=List[FileResponse])
def list_files():
    s3_service = S3Service(bucket_name=bucketName)
    files = s3_service.list_files()
    return files


@router.get("/{file_key}/download")
def get_presigned_download_url(file_key: str):
    s3_service = S3Service(bucket_name=bucketName)
    url = s3_service.generate_presigned_url(file_key)
    return {"url": url}
