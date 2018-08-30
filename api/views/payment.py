from rest_framework.views import APIView
# 购买购物车里面的课程商品同样需要在已登陆条件下，所以需要使用认证类
from api.utils.auth_class import AuthLogin
# 导入能产生固定格式回复消息类
from api.utils.response import BaseResponse
# 导入django的redis模块
from django_redis import get_redis_connection

from django.conf import settings
from rest_framework.response import Response
import json
from api import models

'''
用户想购买添加到购物车的某些商品
'''


class PaymentView(APIView):
    authentication_classes = [AuthLogin, ]
    response = BaseResponse()
    conn = get_redis_connection('default')

    def get(self, request):
        pass


    def post(self, request):
        '''
        当用户点击购物车购买按钮时，并不是跳转到结算页面
        而是需要先跳转到一个过渡页面来让用户自主选择各种优惠策略之后
        再点击购买调用支付接口
        :param request:
        :return:
        '''
        # 获取课程列表
        course_id_list = request.data.get("course_id_list")
        # 获取当前用户id 通过我们的认证组件给我们返回的数据中获取
        login_user_id = request.user.pk

        # 获取即将存入redis中的键值
        luffy_payment_key = settings.LUFFY_GLOBAL_COUPON_KEY % login_user_id
        # 构造数据结构
        payment_dict = {}

        # 挨个获取课程id
        for course_id in course_id_list:
            course_dict = {}
            shopping_cart_key = settings.SHOPPING_CART_KEY % (login_user_id, course_id)
            # 生成购物车键 校验本次提交的课程id是否在之前购物车数据中
            if not self.conn.exists(shopping_cart_key):
                self.response.code = 2000
                self.response.error_msg = '课程不在购物车中'
                return Response(self.response.dict)

            # 课程详细字典
            course_detail = self.conn.hgetall(shopping_cart_key)
            course_detail_dict = {}
            # 循环获取key值，注意获取到的都是bytes格式，所以我们需要对其进行转换
            for key, val in course_detail.items():
                key = key.decode('utf-8')
                val = val.decode('utf-8')
                # 如果key是价格策略，由于价格策略键对应的值也是一个字典格式字符串，所以这里需要额外再做一步json序列化
                if key == 'price_policy':
                    val = json.loads(val)
                # 重新构建出字典格式
                course_detail_dict[key] = val
            # 查询登陆用户所有有效优惠券
            import datetime
            # 优惠券都是相应的时效性，所以需要知道用户操作到此步骤时对应的时间来筛选过滤优惠券
            current_time = datetime.datetime.now().date()
            # 数据库获取该用户所有符合条件的优惠券记录
            coupon_record_list = models.CouponRecord.objects.filter(user=request.user, status=0,
                                                                    coupon__valid_begin_date__lt=current_time,
                                                                    coupon__valid_begin_date__gt=current_time)
            # 构建数据结构保存到redis中
            course_coupons_dict={}
            global_coupons_dict={}

            for coupon_record in coupon_record_list:
                #获取该优惠券是否绑定了课程id，没有则是通用优惠券
                object_id=coupon_record.coupon.object_id
                #构建优惠券信息数据
                tmp={
                    "name":coupon_record.coupon.name,
                    "coupon_type":coupon_record.coupon.coupon_type,
                    "money_equivalent_value":coupon_record.coupon.money_equivalent_value or "",
                    "off_percent":coupon_record.coupon.off_percent or "",
                    "minimum_consume":coupon_record.coupon.minimum_consume or "",
                    "object_id":object_id or "",
                }
                #判断通用优惠券
                if not object_id:
                    #优惠券没有绑定任何课程，说明是通用优惠券
                    global_coupons_dict[coupon_record.pk]=json.dumps(tmp,ensure_ascii=False)
                else:
                    #针对某一课程的优惠券
                    course_coupons_dict[coupon_record.pk]=json.dumps(tmp,ensure_ascii=False)
            #该用户的通用优惠券写入redis
            name=settings.LUFFY_GLOBAL_COUPON_KEY%login_user_id
            self.conn.hmset(name,global_coupons_dict)

            #构建循环的课程字典
            course_dict["course_detail"]=json.dumps(course_detail_dict,ensure_ascii=False)
            course_dict["coupons"]=json.dumps(course_coupons_dict,ensure_ascii=False)

            #将课程字典写入redis中
            payment_dict[course_id]=course_dict
        self.conn.hmset(luffy_payment_key,payment_dict)
        '''
        存入的数据格式如下
        luffy_payment_1:{

             course_id:{

                        course_detail:{
                           },
                        coupons:{
                                 1：{
                                            "name":coupon_record.coupon.name,
                                            "coupon_type":coupon_record.coupon.coupon_type,
                                            "money_equivalent_value":coupon_record.coupon.money_equivalent_value,
                                            "off_percent":coupon_record.coupon.off_percent,
                                            "minimum_consume":coupon_record.coupon.minimum_consume,
                                            "object_id":coupon_record.coupon.object_id,
                                        }
                                 }

                        },
             course_id:{

                  },

             ....

         }

         2 通用优惠券的redis存储:
         global_coupons_1:{
                 global_coupon_id:{}

                 }
        
        '''
        return Response("success")

