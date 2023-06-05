from app.module import APIRouter, Optional, JSONResponse, HTTPException, List, Query
from app.service.db.db_sql import Db
from app.controller.mysql import classes as ClassController
from app.controller.mysql import auth as AuthController
from app.service.auth import jwt as Auth
from app.schemas import classes as ClassSchema
from app.schemas import user as AuthSchema

router = APIRouter(
    prefix="/class",
    tags=["class"],
)

{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiYWd1c3NyIiwiaWF0IjoxNjgzNTEzNTYyLCJuYmYiOjE2ODM1MTM1NjIsImp0aSI6IjBlNjhhOWU4LWMzMmItNDgyMy04NzZkLTk2YWY1NGUyNDFmZiIsImV4cCI6MTY4MzUxNzE2MiwidHlwZSI6ImFjY2VzcyIsImZyZXNoIjp0cnVlLCJyb2xlIjoiUm9sZS5URUFDSEVSIn0.7a8knujbSUcAm7hbiCful92gFbSV26ycmOXsgoZLFqY",
    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJiYWd1c3NyIiwiaWF0IjoxNjgzNTA5ODM2LCJuYmYiOjE2ODM1MDk4MzYsImp0aSI6Ijk4MGVkZmI2LWZiOTEtNDBiYS1iMDUzLWNlZjBiYjE2Y2U3NiIsInR5cGUiOiJyZWZyZXNoIiwicm9sZSI6IlJvbGUuVEVBQ0hFUiJ9.BAqis1u9FWnXUOmmrmCIzhux6d6GUqmlK9fxTWPgV_o",
}


@router.get("/")
async def get_all_class(db: Db, authorize: Auth.AdminRequired):
    return await ClassController.get_all_class(db)


@router.get("/x/{class_id}")
async def read_class(
    class_id: str,
    db: Db,
    authorize: Auth.LoginRequired,
    populate: Optional[str] = Query(
        default=None,
        examples={
            "none": {"value": None},
            "member": {"value": "member"},
            "*": {"value": "*"},
        },
    ),
):
    _class: ClassSchema.DetailClassSchemas = await ClassController.get_class_by_id(class_id, db)
    if populate is None:
        return _class
    else:
        _members = ClassController.get_member(class_id, db)
        _users: List[AuthSchema.UserSchemas] = []
        for member in _members:
            if populate == "member":
                _user: AuthSchema.UserSchemas = AuthController.get_user(member.user_id, db)
                _user.__delattr__("password")
                _user.__delattr__("email_verification_id")
            elif populate == "*":
                _user: AuthSchema.ProfileSchemas = await AuthController.get_user_profile_id(member.user_id, db)
            _users.append(_user)
        _class.__setattr__("members", _users)
        return _class


@router.get("/joined_class")
async def get_all_joined_class(db: Db, authorize: Auth.LoginRequired):
    return await ClassController.get_joined_classes(authorize, db)


@router.get("/owned_class")
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


@router.patch("/update/{class_id}")
async def partial_update(class_id: str, data: ClassSchema.UpdateClassSchemas, db: Db, authorize: Auth.TeacherRequired):
    return await ClassController.partial_update_class(data, class_id, db)


@router.delete("/delete/{class_id}")
async def delete_class(class_id: str, db: Db, authorize: Auth.TeacherRequired):
    return await ClassController.delete_class(class_id, db)


@router.delete("/delete/class/{class_id}/user/{user_id}")
async def delete_user_from_class(user_id: str, class_id, db: Db, authorize: Auth.TeacherRequired):
    _data = await ClassController.delete_user_from_class(class_id=class_id, user_id=user_id, owner=authorize, db=db)
    if _data:
        return JSONResponse(status_code=200, content={"message": "Delete user from class success"})
    raise HTTPException(status_code=400, detail="Delete user from class failed")
