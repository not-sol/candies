from pydantic import BaseModel


class FileResponse(BaseModel):
    size: int
    key: str
