from fastapi import APIRouter
from services.aws.hello_service import HelloService
from models.hello_model import HelloResponse

router = APIRouter()


@router.get("/", response_model=HelloResponse)
def hello():

    service = HelloService()

    result = service.get_hello()

    return HelloResponse(message=result.message)
