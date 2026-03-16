from fastapi import APIRouter, Depends, HTTPException
from models.auth_model import UserLogin, TokenResponse
from usecases.auth_usecase import AuthUsecase
from services.aws.cognito_service import CognitoService

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
async def login_user(
    credentials: UserLogin,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.login_user(credentials)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
