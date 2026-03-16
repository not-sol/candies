from models.auth_model import UserLogin, UserRegister, ConfirmUserRequest

# use DTOs on the parameters in the future
# functions that returns {"message"} have no response in cognito api


class AuthUsecase:

    def __init__(self, service):
        self.auth = service

    def login_user(self, credentials: UserLogin):
        response = self.auth.login(
            credentials.email,
            credentials.password
        )

        return response

    def create_user(self, credentials: UserRegister):
        self.auth.sign_up(
            credentials.email,
            credentials.password,
            credentials.full_name
        )

        return {"message": "register successful, check email for code"}

    def confirm_user(self, credentials: ConfirmUserRequest):
        self.auth.confirm_user(
            credentials.username,
            credentials.confirmationCode
        )

        return {"message": "user confirmed"}

    def delete_user(self, access_token):
        self.auth.delete_user(AcessToken=access_token)

        return {"message": "delete user successful"}

    def logout_user(self, access_token):
        self.auth.global_sign_out(AcessToken=access_token)

        return {"message": "logout successful"}
