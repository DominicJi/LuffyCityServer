from rest_framework.views import APIView
from api.utils.auth_class import AuthLogin
from api import models
#导入我们自己定义的用来产生回复消息的回复类
from api.utils.response import BaseResponse
from django.core.exceptions import ObjectDoesNotExist
#导入django版本的redis模块
from django_redis import get_redis_connection
#导入我们自定义的异常类型
from api.utils.exceptions import PricePolicyError
#导入配置文件中购物车redis键
from django.conf import settings
import json
from django.http import JsonResponse
class Purchase(APIView):
    authentication_classes = [AuthLogin,]
    #提前实例化出回复信息数据机构对象
    response=BaseResponse()
    #获取操作reids数据库的对象
    conn=get_redis_connection('default')
    #get_redis_connection会自动去配置文件中去找CACHES变量配置
    def get(self,request):
        course_id=request.user.pk
        shopping_cart_key=settings.SHOPPING_CART_KEY%(course_id,'\d+')
        import re
        raw_dict={}
        for key in self.conn.keys():  #keys:b'shoppingcart_1_1'
            res=re.match(r'%s'%shopping_cart_key,key.decode('utf-8'))
            if res:
                total_data=self.conn.hgetall(key)
                for key,val in total_data.items():
                    key=key.decode('utf-8')
                    val=val.decode('utf-8')
                    if key=='price_policy':
                        val=json.loads(val)
                    raw_dict[key]=val
        print(raw_dict['price_policy']['1'])


        '''
        针对我们通过django模块简介操作redis获取的数据都是bytes类型，我们需要做一步解码转换，其次对于多层字典数据结构嵌套应该
        考虑在存的时候先序列化多层结构，在取得时候再反序列化出来
         {'course_img': 'http://127.0.0.1:8000/static/Django.png', 
         'default_price_policy_id': '1',
          'course_name': 'Django框架学习',
           'price_policy': {'1': {'price': 100.0, 'valid_period': 7, 'valid_period_text': '1周'},
                                '2': {'price': 200.0, 'valid_period': 14, 'valid_period_text': '2周'},
                                '3': {'price': 300.0, 'valid_period': 30, 'valid_period_text': '1个月'}}}
        '''
        return JsonResponse({})
    def post(self,request):
        '''
        添加购物车信息，需要校验提交数据课程id和关联价格策略的合法性
        :param request:
        :return:
        '''
        course_id=request.data.get('course_id')
        price_policy_id=request.data.get('price_policy_id')

        #先校验课程id的合法性
        try:
            #直接用get去获取课程数据的合法性，不合法直接异常捕获
            course_obj=models.Course.objects.get(pk=course_id)
            #课程存在的话，获取该课程对应的所有价格策略信息
            price_policy_list=course_obj.price_policy.all()
            #构建价格策略的详细信息展示格式
            price_policy_dict={}
            #这里之所以将该课程所有的价格信息都构建出来是由于
            #用户在加入购物车时候可以直接修改价格策略并且我们在购物车界面需要展示相应详细信息
            for price_policy_item in price_policy_list:
                price_policy_dict[price_policy_item.pk]={
                    "price":price_policy_item.price,
                    "valid_period":price_policy_item.valid_period,
                    "valid_period_text":price_policy_item.get_valid_period_display()
                }
            #校验该课程下是否有提交过来的对应的价格策略，防止提交过来的价格策略是其他优惠课程价格策略
            if not price_policy_id in price_policy_dict:
                '''这里如果价格策略与该课程不符合，应该抛出异常
                    至于异常类型如何被捕获，我们可以自定义异常类型的类来被except捕获到
                '''
                raise PricePolicyError()

            '''
            我们需要将用户添加到购物车中的数据添加到缓存数据库redis,首先需要确定的
            就是用什么数据结构去存储每个用户的购物车数据  需要唯一标识每个用户，肯定需要用到
            用户id，并且还需要用到课程id 之后再是该课程下的信息信息。为了简化结构
            我们可以将用户id和课程id利用字符串拼接成一个联合键
            对于这种不变的配置变量名，我们应该首先考虑的是存入配置文件中
            '''
            user_id=request.user.pk
            #构建redis数据键key
            shopping_cart_key=settings.SHOPPING_CART_KEY%(user_id,course_id)
            #构建数据的val
            val={
                "course_name":course_obj.name,
                "course_img":course_obj.course_img,
                #针对字典中某一项键值对中值还是字典结构格式时，建议直接将其序列胡
                "price_policy":json.dumps(price_policy_dict),
                #标识出用户一开始选择的价格策略id
                "default_price_policy_id":price_policy_id
            }
            self.conn.hmset(shopping_cart_key,val)
            self.response.data='success!'


        #捕获我们自己定义的异常
        except PricePolicyError as a:
            #a就是我们自定义异常类的对象
            self.response.code=3000
            self.response.error_msg=a.msg

        except ObjectDoesNotExist as e:
            #课程数据校验错误
            self.response.code=2000
            self.response.error_msg='该课程不存在！！！'
        #提前在回复类中定义一个静态方法展示类对象所有的键值信息
        return JsonResponse(self.response.dict)

