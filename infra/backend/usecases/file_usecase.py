

class FileUsecase:
    def __init__(self, service):
        self.storage_service = service

    def list_file(self, username: str):
        response = self.storage_service.list_file(username)

        return response

    def list_files(self, username: str):
        response = self.storage_service.list_files(username)

        return response

    def create_file():
        pass

    def delete_files():
        pass

    def rename_file():
        pass

    def download_file():
        pass
