from app.module import (
    datetime,
    BaseSettings,
    Annotated,
    HTTPBearer,
    Depends,
    BaseModel,
    Any,
    AuthJWT,
    HTTPException,
    status,
)
from app.models.types import Role


class Settings(BaseSettings):
    authjwt_secret_key: str
    authjwt_algorithm: str


class Token(BaseModel):
    credentials: str


class TokenSchemas(BaseModel):
    access_token: str
    refresh_token: str


security = HTTPBearer()


@AuthJWT.load_config
def get_config():
    return Settings()


def get_current_user(authorize: AuthJWT = Depends(), token=Depends):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()
    return username


def teacher_access(authorize: AuthJWT = Depends(), token=Depends(security)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()
    role = authorize.get_raw_jwt()["role"]
    if role == str(Role.ADMIN) and role == str(Role.TEACHER):
        return username
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You do not have permission to this",
        headers={"WWW-Authenticate": "Bearer"},
    )


def admin_access(authorize: AuthJWT = Depends(), token=Depends(security)):
    authorize.jwt_required()
    username = authorize.get_jwt_subject()
    role = authorize.get_raw_jwt()["role"]
    if role == str(Role.ADMIN):
        return username
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You do not have permission to this",
        headers={"WWW-Authenticate": "Bearer"},
    )


LoginRequired = Annotated[Any, Depends(get_current_user)]
AdminRequired = Annotated[Any, Depends(admin_access)]
TeacherRequired = Annotated[Any, Depends(teacher_access)]


def create_access_token(username: str, role, authorize: AuthJWT):
    token = authorize.create_access_token(
        subject=username, fresh=True, algorithm=Settings().authjwt_algorithm, user_claims={"role": role}
    )
    refresh_token = authorize.create_refresh_token(subject=username, algorithm=Settings().authjwt_algorithm)
    return TokenSchemas(access_token=token, refresh_token=refresh_token)
