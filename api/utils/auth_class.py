from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models
#定义验证类 在用户点击添加购物车时验证用户是否登陆

class AuthLogin(BaseAuthentication):
    def authenticate(self, request):
        #通过获取token信息来实现判定
        token=request.GET.get("token")
        token_obj=models.Token.objects.filter(token=token).first()
        #验证成功，给request添加几组新的键值对信息
        if token_obj:
            #新增获取的用户token信息以及对于用户用户名
            return token_obj.user,token_obj.token
            #后续即可通过request.user获取到用户对象，request.auth获取到token字符串信息
        else:
            raise AuthenticationFailed('认证失败！滚去登陆！！！')
