from app.module import BaseModel, datetime, uuid, Optional, Field, validator
from app.utils.code_generator import randomword_10
from app.schemas import media as Media
from app.schemas import user as User


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

    def __init__(self, color_hex, name, detail):
        super().__init__(color_hex=color_hex, name=name, detail=detail)


class DetailClassSchemas(ClassSchemas):
    members: Optional[User.UserSchemas] = None


class UpdateClassSchemas(ClassBase):
    name: Optional[str] = None
    color_hex: str | None = Field(default=None)

    @validator("name")
    def string_check_name(cls, v):
        if v == "string":
            return None
        return v

    @validator("color_hex")
    def string_check_color(cls, v):
        if v == "string":
            return None
        return v

    @validator("detail")
    def string_check_detail(cls, v):
        if v == "string":
            return None
        return v


class UserClassBase(BaseModel):
    class_id: uuid.UUID
    user_id: uuid.UUID

    class Config:
        orm_mode = True


class UserClassSchemas(UserClassBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class JoinClass(BaseModel):
    code: str
