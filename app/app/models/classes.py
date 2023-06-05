from app.service.db.db_sql import Base
from app.module import String, UUID, uuid, Column, Text, DateTime, func, ForeignKey, relationship, Integer


class Class(Base):
    __tablename__ = "class"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    owner_id = Column(ForeignKey("users.id", ondelete="CASCADE"))
    name = Column(String(255))
    code = Column(String(10), unique=True)
    detail = Column(Text)
    color_hex = Column(String(7))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user_class = relationship("UserClass", back_populates="_class")


class UserClass(Base):
    __tablename__ = "user_class"

    id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(ForeignKey("class.id", ondelete="CASCADE"))
    user_id = Column(ForeignKey("users.id"))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    _class = relationship("Class", back_populates="user_class")
    _user = relationship("Users", back_populates="user_class")
