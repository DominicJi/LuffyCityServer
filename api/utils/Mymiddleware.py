from django.utils.deprecation import MiddlewareMixin

class CorsMiddleWare(MiddlewareMixin):
    def process_response(self,request,response):
        #回复客户端允许在请求头中带有自定义添加的内容
        if request.method=='OPTIONS':
            #允许请求头里面带有内容
            response['Access-Control-Allow-Headers']='Content-Type'
        response['Access-Control-Allow-Origin']='http://localhost:8080'
        return response