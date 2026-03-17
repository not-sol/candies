from pydantic import BaseModel


class LoginResponse(BaseModel):
    AccessToken: str
    ExpiresIn: str
    RefreshToken: str
    TokenType: str
    IdToken: int
