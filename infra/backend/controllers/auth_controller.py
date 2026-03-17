from fastapi import APIRouter, Depends, HTTPException
from usecases.auth_usecase import AuthUsecase
from services.aws.cognito_service import CognitoService
from botocore.exceptions import ClientError
from models.auth_model import (
    UserLogin,
    UserCreate,
    ConfirmUserRequest,
)

router = APIRouter()


@router.get("/me")
async def me_user():
    pass


@router.post("/login")
async def login_user(
    credentials: UserLogin,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.login_user(credentials)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/register")
async def create_user(
    credentials: UserCreate,
    cognito: CognitoService = Depends(CognitoService),
):
    try:
        uc = AuthUsecase(cognito)
        return uc.create_user(credentials)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/confirm")
async def confirm_user(
    request: ConfirmUserRequest,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.confirm_user(request)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/logout")
async def logout_user(
    access_tokens: str,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.logout_user(access_tokens)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reset-password")
async def reset_password_user():
    pass


@router.post("/forgot-password")
async def forgot_password_user():
    pass


@router.delete("/delete")
async def delete_user(
    access_tokens: str,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.delete_user(access_tokens)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
