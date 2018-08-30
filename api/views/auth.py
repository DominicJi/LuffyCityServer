from rest_framework.views import APIView
from django.shortcuts import HttpResponse,render,redirect
from api import models
import uuid
from django.http import JsonResponse

class LoginView(APIView):
    def post(self,request):
        username=request.data.get('user')
        password=request.data.get('pwd')
        # 根据restful规范 返回信息应该设置成字典格式并有相应提示信息
        response = {'code': 200, 'user': '', 'token': '', 'msg': ''}
        try:
            user=models.User.objects.filter(user=username,pwd=password).first()
            if user:
                #如果用户存在，则利用uuid模块生成属于该用户的token信息
                random_str=uuid.uuid4()
                #利用特定语法，检查token表中有无该用户的token信息，有则更新，没有则创建
                models.Token.objects.update_or_create(user=user,defaults={'token':random_str})
                #设置回复信息
                response['token']=random_str
                response['user']=user.user
            else:
                response['code']='403'
                response['msg']='用户名或密码错误'
        except Exception as e:
            response['code']='404'
            response['msg']=str(e)
        return JsonResponse(response)

