from app.service.db.db_sql import Base
from app.module import (
    String,
    UUID,
    uuid,
    Column,
    DateTime,
    func,
    Enum,
    ForeignKey,
    relationship,
    Session,
    Integer,
    Date,
)
from .types import Role, Status


class Profile(Base):
    __tablename__ = "profile"

    id = Column(String(length=20), primary_key=True)
    user_id = Column(ForeignKey("users.id"))
    name = Column(String(255), nullable=False)
    no = Column(Integer(), nullable=True)
    address = Column(String(255), nullable=True)
    birth_date = Column(Date, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())


class EmailVerification(Base):
    __tablename__ = "email_verification"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    status = Column(Enum(Status), default=Status.WAITING)
    code = Column(String(15), nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user = relationship("Users", back_populates="email_verification")


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    email_verification_id = Column(ForeignKey(EmailVerification.id))
    username = Column(String(length=255), unique=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=False)
    role = Column(Enum(Role), default=Role.STUDENT)
    password = Column(String(length=255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    email_verification = relationship("EmailVerification", back_populates="user")
    profile = relationship(Profile, backref="users")
