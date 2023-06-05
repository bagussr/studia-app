from app.module import (
    BaseSettings,
    Annotated,
    HTTPBearer,
    Depends,
    BaseModel,
    Any,
    AuthJWT,
    HTTPException,
    status,
    JWTDecodeError,
    RefreshTokenRequired,
    datetime,
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


def get_current_user(authorize: AuthJWT = Depends(), token=Depends(security)):
    try:
        authorize.jwt_required()
        username = authorize.get_jwt_subject()
        return username
    except JWTDecodeError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="JWT decode error")


def teacher_access(authorize: AuthJWT = Depends(), token=Depends(security)):
    try:
        authorize.jwt_required()
        username = authorize.get_jwt_subject()
        role = authorize.get_raw_jwt()["role"]
        if role == str(Role.ADMIN) or role == str(Role.TEACHER):
            return username
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to this",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTDecodeError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="JWT decode error")


def admin_access(authorize: AuthJWT = Depends(), token=Depends(security)):
    try:
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
    except JWTDecodeError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="JWT decode error")


def refresh_access(authorize: AuthJWT = Depends(), token=Depends(security)):
    try:
        authorize.jwt_refresh_token_required(token=token.credentials)
        username = authorize.get_jwt_subject()
        role = authorize.get_raw_jwt()["role"]
        new_token = authorize.create_access_token(
            subject=username,
            fresh=True,
            algorithm=Settings().authjwt_algorithm,
            user_claims={"role": role},
            expires_time=datetime.timedelta(minutes=60),
        )
        return TokenSchemas(access_token=new_token, refresh_token=token.credentials)
    except RefreshTokenRequired:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Refresh token required")
    except JWTDecodeError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="JWT decode error")


LoginRequired = Annotated[Any, Depends(get_current_user)]
AdminRequired = Annotated[Any, Depends(admin_access)]
TeacherRequired = Annotated[Any, Depends(teacher_access)]
RefreshRequired = Annotated[Any, Depends(refresh_access)]


def create_access_token(username: str, role, authorize: AuthJWT):
    token = authorize.create_access_token(
        subject=username,
        fresh=True,
        algorithm=Settings().authjwt_algorithm,
        user_claims={"role": role},
        expires_time=datetime.timedelta(minutes=60),
    )
    refresh_token = authorize.create_refresh_token(
        subject=username, algorithm=Settings().authjwt_algorithm, user_claims={"role": role}, expires_time=False
    )
    return TokenSchemas(access_token=token, refresh_token=refresh_token)
