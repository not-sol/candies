from fastapi import APIRouter, Depends, HTTPException, Request
from usecases.file_usecase import FileUsecase
from services.aws.s3_service import S3Service
from botocore.exceptions import ClientError

router = APIRouter()


@router.get("/")
def list_files(
    request: Request,
    storage_service: S3Service = Depends(S3Service)
):
    try:
        uc = FileUsecase(storage_service)
        username = request.scope["authorizer"]["claims"]["cognito:username"]
        return uc.list_files(username)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{file_key}")
def get_presigned_download_url(file_key: str):
    # s3_service = S3Service(bucket_name=bucketName)
    # url = s3_service.generate_presigned_url(file_key)
    # return {"url": url}
    pass


@router.post("/upload")
def upload_file():
    pass


@router.put("/{file_key}/rename")
def rename_file(file_key: str):
    pass


@router.delete("/{file_key}")
def delete_file():
    pass
