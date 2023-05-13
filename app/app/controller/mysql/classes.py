from app.module import Session, HTTPException, SQLAlchemyError, Any, List
from app.models import classes as ClassModel
from app.schemas import classes as ClassSchemas
from app.schemas import user as UserSchemas
from app.service.helper.exception import not_found_exception
from app.controller.mysql import auth as AuthController
from app.controller.nosql import classes as MongoService
from app.utils.design_generator import get_design


async def create_class(data: ClassSchemas.CreateClass, owner: str, db: Session):
    design = get_design()
    user = AuthController.get_user_by_username(username=owner, db=db)
    try:
        classes = ClassModel.Class(**data.dict(), owner_id=user.id, color_hex=design.color_hex)
        db.add(classes)
        db.commit()
        db.refresh(classes)
        try:
            join_class(class_id=classes.id, user_id=user.id, db=db)
        except SQLAlchemyError as e:
            db.rollback()
            print(e)
            return HTTPException(status_code=500, detail=e.orig)
        await MongoService.create_media_class(classes.id, media=design)
        return classes
    except Exception as e:
        db.rollback()
        print(e)
        return HTTPException(status_code=500, detail={"msg": "error"})


def join_class(class_id: Any, user_id: Any, db: Session):
    user_class = ClassModel.UserClass(**ClassSchemas.UserClassBase(class_id=class_id, user_id=user_id).dict())
    db.add(user_class)
    db.commit()


async def delete_class(class_id: str, db: Session):
    _class: ClassSchemas.ClassSchemas = db.query(ClassModel.Class).filter(ClassModel.Class.id == class_id).first()
    if _class:
        db.delete(_class)
        db.commit()
        db.refresh(_class)
        await MongoService.delete_media_class(class_id)
        return _class
    raise not_found_exception


async def get_all_class(db: Session):
    classes: List[ClassSchemas.ClassSchemas] = db.query(ClassModel.Class).all()
    if classes:
        media = await MongoService.get_media_class(str(_class.id))
        for _class in classes:
            _class.__setattr__("media", media)
            return classes
    raise not_found_exception


async def get_class_by_id(id: Any, db: Session):
    _class: ClassSchemas.ClassSchemas
    _class = db.query(ClassModel.Class).filter(ClassModel.Class.id == id).first()
    if _class:
        media = await MongoService.get_media_class(str(_class.id))
        _class.__setattr__("media", media)
        return _class
    raise not_found_exception


async def get_class_by_code(code: str, db: Session):
    _class: ClassSchemas.ClassSchemas
    _class = db.query(ClassModel.Class).filter(ClassModel.Class.code == code).first()
    if _class:
        media = await MongoService.get_media_class(str(_class.id))
        _class.__setattr__("media", media)
        return _class
    raise not_found_exception


async def get_classes(owner: str, db: Session):
    user = AuthController.get_user_by_username(username=owner, db=db)
    classes: List[ClassSchemas.ClassSchemas] = (
        db.query(ClassModel.Class).filter(ClassModel.Class.owner_id == user.id).all()
    )
    if classes:
        _class: ClassSchemas.ClassSchemas
        for _class in classes:
            media = await MongoService.get_media_class(str(_class.id))
            _class.__setattr__("media", media)
        return classes
    raise not_found_exception


async def get_joined_classes(user: str, db: Session):
    user = AuthController.get_user_by_username(username=user, db=db)
    user_class = db.query(ClassModel.UserClass).filter(ClassModel.UserClass.user_id == user.id).all()
    if len(user_class) == 0:
        raise not_found_exception
    classes = db.query(ClassModel.Class).filter(ClassModel.Class.id.in_([x.class_id for x in user_class])).all()
    if len(classes) == 0:
        raise not_found_exception
    _class: ClassSchemas.ClassSchemas
    for _class in classes:
        media = await MongoService.get_media_class(str(_class.id))
        _class.__setattr__("media", media)
    return classes


async def partial_update_class(data: ClassSchemas.UpdateClassSchemas, class_id: str, db: Session):
    _class = get_class_by_id(id=class_id, db=db)
    _class.__init__(**data.dict(exclude_none=True))
    db.merge(_class)
    db.commit()
    db.refresh(_class)
    return _class


async def delete_user_from_class(class_id: str, user_id: str, owner, db: Session):
    _user: UserSchemas.UserSchemas = AuthController.get_user_by_username(username=owner, db=db)
    _class: ClassSchemas.ClassSchemas = await get_class_by_id(id=class_id, db=db)
    if _class:
        if _user.id == _class.owner_id:
            user_class = (
                db.query(ClassModel.UserClass)
                .filter(ClassModel.UserClass.class_id == class_id, ClassModel.UserClass.user_id == user_id)
                .first()
            )
            if user_class:
                db.delete(user_class)
                db.commit()
                db.refresh(user_class)
            raise not_found_exception
        raise HTTPException(status_code=403, detail={"msg": "You are not the owner of this class"})
    raise not_found_exception
