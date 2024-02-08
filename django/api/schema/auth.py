# User Auth 와 관련한 Schema
from ninja import Schema


class LoginSchema(Schema):
    email: str
    password: str


class RegistSchema(Schema):
    email: str
    username: str
    password: str


class JWTPairSchema(Schema):
    # client_id: str
    # refresh: str
    access: str


class JWTTokenSchema(Schema):
    token_type: str
    user_id : str
    exp : str
    iat : str
    jti : str
