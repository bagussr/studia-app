from app.module import (
    BaseModel,
    Field,
    datetime,
    BaseSettings,
    ObjectId,
    Optional,
    uuid,
)
from .object import PyObjectId


class Base(BaseSettings):
    base_url: str
    default_profile: str
    default_content_type: str


class MediaBase(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: Optional[str] = None
    size: int = 0
    base_url: str = Base().base_url
    path: Optional[str] = None
    url: Optional[str] = None
    content_type: str = Base().default_content_type
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    update_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class MediaProfile(MediaBase):
    name: str = "default"
    profile_id: str
    path: Optional[str] = Base().default_profile
    url: Optional[str] = Base().base_url + Base().default_profile


class MediaClass(MediaBase):
    class_id: uuid.UUID


class GetMediaClass(MediaClass):
    id: str = Field(alias="_id")
