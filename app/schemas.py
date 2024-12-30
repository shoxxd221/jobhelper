from pydantic import BaseModel
from datetime import datetime


class BaseSchema(BaseModel):
    id: int
    url: str
    date_publication: datetime
    title: str

    class Config:
        orm_mode = True


class HHSchema(BaseSchema):
    pass


class YCRSchema(BaseSchema):
    active: bool
    description: str
