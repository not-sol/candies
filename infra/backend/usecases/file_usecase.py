from services.aws.s3_service import S3Service


class FileUsecase:
    def __init__(self, s3_service: S3Service):
        self.s3_service = s3_service

    def list_files():
        pass

    def create_file():
        pass

    def delete_files():
        pass

    def rename_file():
        pass

    def download_file():
        pass
