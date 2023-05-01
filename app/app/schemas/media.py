from app.module import ObjectId
from app.module import BaseModel, Field, datetime, BaseSettings
from .object import PyObjectId


class Base(BaseSettings):
    base_url: str
    default_profile: str
    default_content_type: str


class MediaBase(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = "default"
    size: int = 0
    base_url: str = Base().base_url
    path: str = Base().default_profile
    url: str = Base().base_url + Base().default_profile
    content_type: str = Base().default_content_type
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    update_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class MediaProfile(MediaBase):
    profile_id: str
