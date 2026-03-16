import boto3
from models.auth_model import (
    ConfirmUserRequest,
    UserCreate
)


class CognitoService:

    def __init__(self):
        self.client = boto3.client("cognito-idp")
        self.client_id = "6afddfftiaavt6tkvvd4nh19dc"

    def login_user(self, credentials: UserCreate):
        response = self.client.initiate_auth(
            ClientId=self.client_id,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": credentials.email,
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
                {"Name": "email", "Value": credentials.email}
            ]
        )

        return response

    def confirm_user(self, request: ConfirmUserRequest):
        response = self.client.confirm_sign_up(
            ClientId=self.client_id,
            Username=request.username,
            ConfirmationCode=request.confirmationCode
        )

        return response

    def logout_user(self, access_tokens: str):
        self.client.global_sign_out(access_tokens)

    def delete_user(self, access_tokens: str):
        self.client.delete_user(access_tokens)
