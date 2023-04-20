from app.models.auth import Users, Profile, EmailVerification
from app.module import Session
from app.schemas.user import RegisterSchemas
from app.utils.code_generator import randomword_15, randomword_20
from app.controller.nosql.auth import create_media_profile
from app.service.helper.exception import not_found_exception


async def create_account(data: RegisterSchemas, db: Session):
    try:
        email = await create_email_verification(db)
        data.__setattr__("email_verification_id", email.id)
        user = await create_user(data, db)
        await create_profile(data.name, user.id, db)
    except:
        db.rollback()
    return user


async def create_email_verification(db: Session):
    email = EmailVerification(code=randomword_15())
    db.add(email)
    db.commit()
    db.refresh(email)
    return email


async def create_user(data: RegisterSchemas, db: Session):
    user = Users(**data.dict(exclude={"name"}))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


async def create_profile(name: str, id: str, db: Session):
    profile = Profile(id=randomword_20(), user_id=id, name=name)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    await create_media_profile(profile.id)
    return profile


def get_user_by_username(username: str, db: Session):
    user = db.query(Users).filter(Users.username == username).first()
    if user:
        return user
    raise not_found_exception

def get_user(_id: str, db: Session):
    user = db.query(Users).filter_by(id=_id).first()
    if user:
        return user
    raise not_found_exception