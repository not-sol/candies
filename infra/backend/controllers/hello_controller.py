from fastapi import APIRouter
from services.hello_service import HelloService
from schemas.hello_schema import HelloResponse

router = APIRouter()


@router.get("/", response_model=HelloResponse)
def hello():

    service = HelloService()

    result = service.get_hello()

    return HelloResponse(message=result.message)
