from models.auth_model import UserLogin


class AuthUsecase:

    def __init__(self, cognito_service):
        self.auth = cognito_service

    def login_user(self, credentials: UserLogin):
        tokens = self.auth.login(
            credentials.email,
            credentials.password
        )

        return {
            "access_token": tokens["AccessToken"],
            "id_token": tokens["IdToken"],
            "refresh_token": tokens["RefreshToken"],
            "token_type": "Bearer"
        }
