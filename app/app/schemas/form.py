from app.module import Annotated, Body
from .user import LoginSchemas

LoginForm = Annotated[
    LoginSchemas,
    Body(
        examples={
            "username": {"summary": "login with username", "value": {"username": "foo", "password": "*******"}},
            "email": {
                "summary": "login with email",
                "value": {"username": "foo@example.com", "password": "*******"},
            },
        }
    ),
]
