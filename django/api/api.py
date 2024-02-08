import orjson
from ninja import NinjaAPI
from ninja.renderers import BaseRenderer
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from core.models import User


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json; charset=utf-8"
    def render(self, request, data, *, response_status):
        return orjson.dumps(data)


# Auth User Login
# https://docs.djangoproject.com/ko/4.2/topics/auth/customizing/
class UserAuth(BaseBackend):

    def authenticate(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password): return user
            else: return None
        except:   return None


api = NinjaAPI(
    title = "API Ninja",
    version = "0.0.1",
    docs_url = "docs",
    description = "게시만 만들기 연습",
    urls_namespace = "api",
    renderer = ORJSONRenderer(),
    csrf = False, 
    openapi_url=settings.DEBUG and "/openapi.json" or "",
)
