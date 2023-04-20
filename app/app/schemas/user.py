from app.module import BaseModel, datetime, validator, Field, PrivateAttr, uuid
from app.models.types import Role, Status
from app.utils.password import password_hash, verify_password


class UserBase(BaseModel):
    username: str
    password: str

    class Config:
        use_enum_values = True
        orm_mode = True


class LoginSchemas(UserBase):
    pass


class RegisterSchemas(UserBase):
    email: str
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
    email: str
    role: Role
    password: str = Field(exclude=True)
    created_at: datetime.datetime
    updated_at: datetime.datetime
