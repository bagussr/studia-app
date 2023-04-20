from app.module import APIRouter, Depends, AuthJWT, HTTPException, status
from app.schemas.form import LoginForm
from app.schemas.user import RegisterSchemas, UserSchemas
from app.service.auth.jwt import create_access_token
from app.service.db.db_sql import Db
from app.controller.mysql.auth import create_account, get_user, get_user_by_username
from app.utils.password import verify_password


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login")
def login(data: LoginForm, db: Db, authorize: AuthJWT = Depends()):
    user = get_user_by_username(data.username, db)
    if verify_password(data.password, user.password):
        token = create_access_token(user.username, str(user.role), authorize)
        return token
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong password")


@router.post("/register")
async def register(data: RegisterSchemas, db: Db):
    user = await create_account(data=data, db=db)
    return user


@router.get("/user/{id}", response_model=UserSchemas)
def read_user(id: str, db: Db):
    user = get_user(id, db)
    return user
