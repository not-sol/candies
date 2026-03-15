# from fastapi import APIRouter, Depends, HTTPException, Header
# from typing import List
# from services.s3_service import S3Service
# from schemas.file_schema import FileResponse
# import jwt
#
# router = APIRouter(prefix="/files")
#
#
# def get_current_user(authorization: str = Header(...)):
#     try:
#         token = authorization.split(" ")[1]
#         decoded = jwt.decode(token, options={"verify_signature": False})
#         user_id = decoded.get("sub")
#         if not user_id:
#             raise HTTPException(status_code=401, detail="Invalid token")
#         return user_id
#     except Exception:
#         raise HTTPException(status_code=401, detail="Invalid authorization")
#
#
# @router.get("", response_model=List[FileResponse])
# def list_files(user_id: str = Depends(get_current_user)):
#     s3_service = S3Service()
#     files = s3_service.list_files(user_id)
#     return files
