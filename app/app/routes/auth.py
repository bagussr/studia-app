from app.module import APIRouter, Depends, AuthJWT, HTTPException, status, Request, Optional, List
from app.schemas.form import LoginForm
from app.schemas.user import RegisterSchemas, UserSchemas, ProfileSchemas
from app.service.auth.jwt import create_access_token, LoginRequired, AdminRequired, RefreshRequired
from app.service.db.db_sql import Db
from app.controller.mysql.auth import create_account, get_user, get_user_by_username, get_user_profile, get_user_all
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


@router.get("/user/current", response_model=UserSchemas)
def current_user(db: Db, auth: LoginRequired):
    user = get_user_by_username(auth, db)
    return user


@router.get("/user/profile")
async def current_profile(db: Db, auth: LoginRequired, populate: Optional[str] = None):
    profile = await get_user_profile(auth, db)
    if populate == "*":
        return profile
    if populate == "media":
        profile.__delattr__("user")
        return profile
    if populate == "user":
        profile.__delattr__("media")
        return profile
    if populate is None:
        profile.__delattr__("user")
        profile.__delattr__("media")
        return profile


@router.get("/user/list", response_model=List[UserSchemas])
def read_all_user(db: Db, auth: AdminRequired):
    return get_user_all(db)


@router.get("/user/{id}", response_model=UserSchemas)
def read_user(id: str, db: Db, auth: AdminRequired):
    user = get_user(id, db)
    return user


@router.post("/refresh-token")
def refresh_token(auth: RefreshRequired, request: Request):
    return auth
