import boto3


class CognitoService:

    def __init__(self):
        self.client = boto3.client("cognito-idp")
        self.client_id = "6afddfftiaavt6tkvvd4nh19dc"

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
