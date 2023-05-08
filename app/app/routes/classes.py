from app.module import APIRouter, List, Depends, Body
from app.service.db.db_sql import Db
from app.controller.mysql import classes as ClassController
from app.controller.mysql import auth as AuthController
from app.service.auth import jwt as Auth
from app.schemas import classes as ClassSchema

router = APIRouter(
    prefix="/class",
    tags=["class"],
)

{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiYWd1c3NyIiwiaWF0IjoxNjgzNTA5ODM2LCJuYmYiOjE2ODM1MDk4MzYsImp0aSI6ImIyMzIyNTJiLTlhZjMtNDBkYy1hYjdjLTk0YzRmMjIzYWQ1MyIsImV4cCI6MTY4MzUxMzQzNiwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjp0cnVlLCJyb2xlIjoiUm9sZS5URUFDSEVSIn0.ubcLOO8Pbc0bhFu-JC-_7XWEUQ4dfm4U1HAPiqRdMiU",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiYWd1c3NyIiwiaWF0IjoxNjgzNTA5ODM2LCJuYmYiOjE2ODM1MDk4MzYsImp0aSI6Ijk4MGVkZmI2LWZiOTEtNDBiYS1iMDUzLWNlZjBiYjE2Y2U3NiIsInR5cGUiOiJyZWZyZXNoIiwicm9sZSI6IlJvbGUuVEVBQ0hFUiJ9.BAqis1u9FWnXUOmmrmCIzhux6d6GUqmlK9fxTWPgV_o",
}


@router.get("/")
def get_all_class(db: Db):
    return ClassController.get_all_class(db)


@router.get("/joined_class", response_model=List[ClassSchema.ClassSchemas])
async def get_all_joined_class(db: Db, authorize: Auth.LoginRequired):
    return await ClassController.get_joined_classes(authorize, db)


@router.get("/owned_class", response_model=List[ClassSchema.ClassSchemas])
async def get_all_owned_class(db: Db, authorize: Auth.TeacherRequired):
    return await ClassController.get_classes(authorize, db)


@router.post("/")
async def create_class(data: ClassSchema.CreateClass, db: Db, authorize: Auth.TeacherRequired):
    return await ClassController.create_class(data, authorize, db)


@router.post("/join", response_model=ClassSchema.ClassSchemas)
async def join_class(code: ClassSchema.JoinClass, db: Db, authorize: Auth.LoginRequired):
    _class = await ClassController.get_class_by_code(code.code, db)
    _user = AuthController.get_user_by_username(authorize, db)
    ClassController.join_class(_class.id, _user.id, db)
    return _class
