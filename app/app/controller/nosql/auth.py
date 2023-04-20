from app.module import jsonable_encoder
from app.service.db.db_mongo import MongoClass, db
from app.schemas.media import MediaProfile


async def create_media_profile(id: str):
    mongo = MongoClass("media_profile", db)
    data = MediaProfile(profile_id=id)
    await mongo.insert(jsonable_encoder(data))
    return data
