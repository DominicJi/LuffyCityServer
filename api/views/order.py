from rest_framework.views import APIView
from api.utils.auth_class import AuthLogin
#获取回复详细类
from api.utils.response import BaseResponse
#导入自定义报错信息类
from api.utils.exceptions import CommonException
import datetime
from api import models
from django.http import JsonResponse
class OrderView(APIView):
    '''
    这个视图类是专门用来用户在支付实际金额之前的计算操作
    包括 优惠券计算 贝利计算
    '''
    authentication_classes = [AuthLogin,]
    def post(self,request):
        '''
        大致思路:前端传过来的数据对于我们来说都可能存在恶意串改行为
        所以我们需要对这些数据都进行一次校验，自己计算出实际金额
        与前端传过来的金额做比较，最终再确定是否展示真正的交易二维码
        :param request:
        :return:
        '''
        #先获取用户的贝利数 总交易金额 通用优惠券 课程详细信息(包括各个课程id 价格策略等)
        bely=request.data.get('bely')
        #前端总金额
        balance=request.data.get('balance')
        #通用优惠券
        global_coupon_id=request.data.get('global_coupon_id')
        #课程详细
        courses_detail=request.data.get("courses_detail")
        #产生回复消息对象
        response=BaseResponse()
        try:
            #由于使用了认证功能，所以拿到用户对象 即可做相应查询操作
            if bely>request.user.bely:
                raise CommonException('贝里数据有问题')

            #由于用户可能一次交易买了多门课程。我们应该将没门课程的价格算出来再求和
            price_list=[]
            current_time=datetime.datetime.now().date()
            for course_id,course_info in courses_detail.items():
                #校验课程是否存在
                course_obj=models.Course.objects.filter(pk=course_id).first()
                if not course_obj:
                    raise CommonException("课程不存在")

                #校验价格策略是否正常
                price_policy_id=int(course_info.get("price_policy_id"))
                price_policy_set=course_obj.price_policy.all()
                #判断价格策略是否是该课程真实拥有的
                if price_policy_id not in [price_policy.pk for price_policy in price_policy_set]:
                    raise CommonException('价格策略有问题')

                #先获取该课程的实际价格策略对应的价格
                price = models.PricePolicy.objects.filter(pk=price_policy_id).first().price
                # 校验课程优惠券是否有效
                coupon_record_id=int(course_info.get('coupon_record_id'))
                #如果获取不到优惠券id，说明用户没有使用优惠券。直接将原价放入价格列表中
                if not coupon_record_id:
                    price_list.append(price)
                    continue
                coupon_record_obj = models.CouponRecord.objects.filter(pk=coupon_record_id,
                                                                       user=request.user,
                                                                       coupon__valid_begin_date__lt=current_time,
                                                                       coupon__valid_begin_date__gt=current_time,
                                                                       ).first()
                if not coupon_record_obj:
                    raise CommonException('优惠券有问题')

                # 校验该优惠券是否属于该课程
                if coupon_record_obj.coupon.object_id != int(course_id):
                    raise CommonException('优惠券与课程不匹配')

                # 计算该循环课程经过课程优惠券处理后的价格

                counted_price = self.account_price(coupon_record_obj, price)
                # 将优惠券相关的计算最终得到的结果存放到价格列表中
                price_list.append(counted_price)

            #校验通用优惠券
            if not global_coupon_id:
                #用户没有使用通用优惠券
                account_price=sum(price_list)
            else:
                global_coupon_record_obj=models.CouponRecord.objects.filter(pk=global_coupon_id,
                                                                            user=request.user,
                                                                            coupon__valid_begin_date__lt=current_time,
                                                                            coupon__valid_begin_date__gt=current_time,
                                                                            ).first()
                if not global_coupon_record_obj:
                    raise CommonException('通用优惠券有问题')

                #将价格列表求和后再经过通用优惠券处理出一个实际价格
                account_price=self.account_price(global_coupon_record_obj,sum(price_list))

            #校验前端传过来的实际价格与我们计算的动啊的价格是否一致
            final_price=account_price-bely/10
            if final_price<0:
                final_price=0

            if final_price!=balance:
                raise CommonException('提交的价格有问题')

            '''
            价格计算准确无误后，创建相应订单，这里订单有两张表，一张是总的订单表
            还有一张是针对某个课程的单一订单表
            '''

            '''
            订单创建完毕后应调用支付宝接口来使用户完成订单金额支付
            '''
            return JsonResponse(self.response.dict)

        except CommonException as e:
            self.response.error_msg=e.msg
            self.response.code=2000


    def get(self,request):
        pass

    #计算各种优惠之后的价格
    def account_price(self,coupon_record_obj,price):
        #获取优惠券类型
        coupon_type=coupon_record_obj.coupon.coupon_type
        #与人民币比值
        money_equivalent_value=coupon_record_obj.counpon.money_equivalent_value
        #优惠折扣百分比
        off_percent=coupon_record_obj.coupon.off_percent
        #最低消费多少可用
        minimum_consume=coupon_record_obj.coupon.minimum_consume
        real_price=0
        #如果是0表示是立减券
        if coupon_type==0:
            #有一个原则就是实际消费价格肯定要比优惠券的多，哪有不赚倒贴的买卖呀
            if price>money_equivalent_value:
                real_price=price-money_equivalent_value
        #如果是满减券
        elif coupon_type==1:
            if price>minimum_consume:
                real_price=price-money_equivalent_value
            else:
                raise CommonException('优惠券无效')
        #折扣券
        elif coupon_type==2:
            real_price=price*(off_percent/100)

        return real_price