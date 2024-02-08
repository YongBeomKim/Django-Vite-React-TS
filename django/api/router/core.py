from .base import *
router_core = Router()


# Login of Get Token
# 인터넷이 안되는 경우 로그인 활성화
@router_core.post('/token', auth=None) # response=JWTPairSchema, 
def login(request, auth: LoginSchema):

    r"""사용자 로그인시 Token 발급"""
    user = UserAuth().authenticate(**auth.dict())
    if user is not None:
        try:
            token = AccessToken.for_user(user)
            return {'token': str(token)}
        except Exception as E:
            return {'message': E}
    else:
        return {'token':''}
