"""luffy_boy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api.views import course
from api.views import auth
from api.views import shoppingcart
from api.views import payment
from api.views import alipay
from api.views import order
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^courses/',course.CourseView.as_view()),
    url(r'^course_detail/(?P<pk>\d+)',course.CourseDetailView.as_view()),
    url(r'^login/',auth.LoginView.as_view()),
    url(r'^purchase/',shoppingcart.Purchase.as_view()),
    url(r'^payment/',payment.PaymentView.as_view()),
    #结算接口 优惠券 贝利数 折扣券
    url(r'^order/',order.OrderView.as_view()),
    #调用支付宝支付接口演示
    url(r'^page1/', alipay.page1),
    url(r'^page2/', alipay.page2),

]
