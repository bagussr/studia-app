from app.module import BaseModel, datetime, uuid, Optional, List
from app.utils.code_generator import randomword_10
from app.schemas import media as Media


class ClassBase(BaseModel):
    name: str
    detail: Optional[str]

    class Config:
        orm_mode = True


class CreateClass(ClassBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, "code", randomword_10())


class ClassSchemas(ClassBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    color_hex: str
    code: str
    media: Optional[Media.GetMediaClass] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UpdateClassSchemas(ClassBase):
    color_hex: str
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserClassBase(BaseModel):
    class_id: uuid.UUID
    user_id: uuid.UUID

    class Config:
        orm_mode = True


class UserClassSchemas(UserClassBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
