import boto3
from domain.services.auth_service import AuthService


class CognitoService(AuthService):

    def __init__(self, client_id: str):
        self.client = boto3.client("cognito-idp")
        self.client_id = client_id

    def login(self, email: str, password: str):
        response = self.client.initiate_auth(
            ClientId=self.client_id,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": email,
                "PASSWORD": password
            }
        )

        return response["AuthenticationResult"]
