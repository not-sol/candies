from pydantic import BaseModel


class FileResponse(BaseModel):
    key: str
    size: int
