from app.module import jsonable_encoder, BaseSettings
from app.service.db.db_mongo import MongoClass, db
from app.schemas.media import MediaClass
from app.utils.design_generator import DesignSchema


class Base(BaseSettings):
    base_url: str


async def create_media_class(id: str, media: DesignSchema):
    mongo = MongoClass("media_class", db)
    data = MediaClass(
        class_id=id, name=media.name, path=media.image + ".png", url=Base().base_url + media.image + media.name + ".png"
    )
    await mongo.insert(jsonable_encoder(data))
    return data


async def get_media_class(class_id: str):
    mongo = MongoClass("media_class", db)
    data = await mongo.filter_by("class_id", class_id)
    return data
