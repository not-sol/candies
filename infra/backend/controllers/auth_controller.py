from fastapi import APIRouter, Depends, HTTPException
from models.auth_model import UserLogin, TokenResponse
from usecases.auth_usecase import AuthUsecase
from services.aws.cognito_service import CognitoService

router = APIRouter()


@router.get("/me")
async def me_user():
    pass


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


@router.post("/register")
async def register_user():
    pass


@router.post("/confirm")
async def confirm_user():
    pass


@router.post("/logout")
async def logout_user():
    pass


@router.post("/reset-password")
async def reset_password_user():
    pass


@router.post("/forgot-password")
async def forgor_password_user():
    pass
