from fastapi import APIRouter, Depends, HTTPException
from usecases.auth_usecase import AuthUsecase
from services.aws.cognito_service import CognitoService
from botocore.exceptions import ClientError
from models.auth_model import (
    UserLogin,
    UserCreate,
    ConfirmUserRequest,
    ForgotPasswordConfirm
)

router = APIRouter()


@router.post("/me")
async def get_user(
    access_token: str,
    cognito: CognitoService = Depends(CognitoService)

):
    try:
        uc = AuthUsecase(cognito)
        return uc.get_user(access_token)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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


@router.post("/refresh-token")
async def refresh_access_token(
    refresh_token: str,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.refresh_access_token(refresh_token)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/create-user")
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


@router.post("/resend-code")
async def resend_confirmation_code(
    username: str,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.resend_confirmation_code(username)

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


@router.post("/request-forgot-password")
async def request_forgot_password(
    username: str,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.request_forgot_password(username)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/confirm-forgot-password")
async def confirm_forgot_password(
    request: ForgotPasswordConfirm,
    cognito: CognitoService = Depends(CognitoService)
):
    try:
        uc = AuthUsecase(cognito)
        return uc.confirm_forgot_password(request)

    except ClientError as e:
        error_message = e.response["Error"]["Message"]
        raise HTTPException(status_code=400, detail=error_message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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
