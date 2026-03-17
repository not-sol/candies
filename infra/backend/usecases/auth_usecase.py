from models.auth_model import (
    UserLogin,
    UserCreate,
    ConfirmUserRequest
)

# use DTOs on the parameters in the future
# functions that returns {"message"} have no response in cognito api


class AuthUsecase:

    def __init__(self, cognito_service):
        self.auth = cognito_service

    def login_user(self, credentials: UserLogin):
        response = self.auth.login_user(credentials)

        return response

    def create_user(self, credentials: UserCreate):
        self.auth.create_user(credentials)

        return {"message": "register successful, check email for code"}

    def confirm_user(self, credentials: ConfirmUserRequest):
        self.auth.confirm_user(credentials)

        return {"message": "user confirmed"}

    def delete_user(self, access_token):
        self.auth.delete_user(access_token)

        return {"message": "delete user successful"}

    def logout_user(self, access_token):
        self.auth.logout_user(access_token)

        return {"message": "logout successful"}
