from app.module import jsonable_encoder, json
from app.service.db.db_mongo import MongoClass, db
from app.schemas.media import MediaProfile


async def create_media_profile(id: str):
    mongo = MongoClass("media_profile", db)
    data = MediaProfile(profile_id=id)
    await mongo.insert(jsonable_encoder(data))
    return data


async def get_media_profile(profile_id):
    mongo = MongoClass("media_profile", db)
    data = await mongo.filter_by("profile_id", profile_id)

    return data
