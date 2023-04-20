from app.module import EnumClass


class Role(EnumClass):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    ADMIN = "ADMIN"


class Status(EnumClass):
    VERIFIED = "VERIFIED"
    DONE = "DONE"
    WAITING = "WAITING"
    FAILED = "FAILED"
