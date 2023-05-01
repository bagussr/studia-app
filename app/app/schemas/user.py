from app.module import BaseModel, datetime, validator, Field, PrivateAttr, uuid, Optional, EmailStr
from app.models.types import Role, Status
from app.utils.password import password_hash, verify_password
from .media import MediaProfile
from .object import ObjectId


class UserBase(BaseModel):
    username: str
    password: str

    class Config:
        use_enum_values = True
        orm_mode = True


class LoginSchemas(UserBase):
    pass


class RegisterSchemas(UserBase):
    email: EmailStr
    role: Role = Role.STUDENT
    _password2: str = PrivateAttr()
    name: str
    email_verification_id: str = None

    @validator("_password2", check_fields=False)
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and not verify_password(v, values["password"]):
            raise ValueError("passwords do not match")
        return v

    @validator("password")
    def password_hash(cls, v):
        return password_hash(v)

    class Config:
        schema_extra = {
            "example": {
                "username": "string",
                "name": "string",
                "email": "string",
                "role": Role.STUDENT,
                "password": "string",
                "password2": "string",
            }
        }


class UserSchemas(UserBase):
    id: uuid.UUID
    email: EmailStr
    role: Role
    password: str = Field(exclude=True)
    created_at: datetime.datetime
    updated_at: datetime.datetime


class ProfileSchemas(BaseModel):
    id: str
    name: str
    no: Optional[int] = None
    address: Optional[str] = None
    birth_date: Optional[datetime.date] = None
    user: Optional[UserSchemas] = None
    media: Optional[MediaProfile] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @validator("user")
    def remove_password(cls, v):
        del v.password
        return v

    def __call__(self):
        del self.user.password

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        allow_mutations = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
