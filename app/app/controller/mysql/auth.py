from app.models import auth as AuthModel
from app.module import Session
from app.schemas.user import RegisterSchemas, ProfileSchemas, UserSchemas
from app.utils import code_generator as Utils
from app.controller.nosql import auth as MongoService
from app.service.helper.exception import not_found_exception


def get_user_all(db: Session):
    user = db.query(AuthModel.AuthModel.Users).all()
    if user:
        return user
    else:
        raise not_found_exception


async def create_account(data: RegisterSchemas, db: Session):
    try:
        email = await create_email_verification(db)
        data.__setattr__("email_verification_id", email.id)
        user = await create_user(data, db)
        await create_profile(data.name, user.id, db)
        return user
    except:
        db.rollback()


async def create_email_verification(db: Session):
    email = AuthModel.EmailVerification(code=Utils.randomword_15())
    db.add(email)
    db.commit()
    db.refresh(email)
    return email


async def create_user(data: RegisterSchemas, db: Session):
    user = AuthModel.AuthModel.Users(**data.dict(exclude={"name"}))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def create_profile(name: str, id: str, db: Session):
    profile = AuthModel.Profile(id=Utils.randomword_20(), user_id=id, name=name)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    await MongoService.create_media_profile(profile.id)
    return profile


def get_user_by_username(username: str, db: Session):
    user = (
        db.query(AuthModel.Users).filter(AuthModel.Users.username == username).first()
    )
    if user:
        return user
    raise not_found_exception


def get_user(_id: str, db: Session) -> UserSchemas:
    user: UserSchemas = db.query(AuthModel.Users).filter_by(id=_id).first()
    if user:
        return user
    raise not_found_exception


async def get_user_profile(username: str, db: Session):
    user = (
        db.query(AuthModel.Users).filter(AuthModel.Users.username == username).first()
    )
    if user is None:
        raise not_found_exception
    profile = (
        db.query(AuthModel.Profile).filter(AuthModel.Profile.user_id == user.id).first()
    )
    if profile is None:
        raise not_found_exception
    media = await MongoService.get_media_profile(profile.id)
    data = ProfileSchemas(
        id=profile.id,
        name=profile.name,
        no=profile.no,
        address=profile.address,
        birth_date=profile.birth_date,
        user=user,
        media=media,
        created_at=profile.created_at,
        updated_at=profile.updated_at,
    )
    return data


async def get_user_profile_id(id: str, db: Session):
    user = db.query(AuthModel.Users).filter(AuthModel.Users.id == id).first()
    if user is None:
        raise not_found_exception
    profile = (
        db.query(AuthModel.Profile).filter(AuthModel.Profile.user_id == user.id).first()
    )
    if profile is None:
        raise not_found_exception
    media = await MongoService.get_media_profile(profile.id)
    data = ProfileSchemas(
        id=profile.id,
        name=profile.name,
        no=profile.no,
        address=profile.address,
        birth_date=profile.birth_date,
        user=user,
        media=media,
        created_at=profile.created_at,
        updated_at=profile.updated_at,
    )
    return data
