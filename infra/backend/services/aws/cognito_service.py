import boto3
from models.auth_model import (
    UserLogin,
    UserCreate,
    ConfirmUserRequest,
)


class CognitoService:

    def __init__(self):
        self.client = boto3.client("cognito-idp")
        self.client_id = "2kmf4vu3q7v1dolm7fo0jivi5t"

    def login_user(self, credentials: UserLogin):
        response = self.client.initiate_auth(
            ClientId=self.client_id,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": credentials.username,
                "PASSWORD": credentials.password
            }
        )

        return response["AuthenticationResult"]

    def create_user(self, credentials: UserCreate):
        response = self.client.sign_up(
            ClientId=self.client_id,
            Username=credentials.username,
            Password=credentials.password,
            UserAttributes=[
                {"Name": "email", "Value": credentials.email},
                {"Name": "preferred_username", "Value": credentials.username},
            ],
        )
        return response

    def confirm_user(self, request: ConfirmUserRequest):
        response = self.client.confirm_sign_up(
            ClientId=self.client_id,
            Username=request.username,
            ConfirmationCode=request.confirmation_code
        )

        return response

    def logout_user(self, access_tokens: str):
        self.client.global_sign_out(AccessToken=access_tokens)

    def delete_user(self, access_tokens: str):
        self.client.delete_user(AccessToken=access_tokens)
