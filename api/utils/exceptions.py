
'''
这里新学到一个知识点就是我们可以自定义异常类型
来被异常处理捕获并展示我们自定义的展示信息！！！


'''
class PricePolicyError(Exception):
    def __init__(self):
        self.msg='该课程没有改价格策略，你他妈的想占老娘便宜？没门！！！'

class CommonException(Exception):
    def __init__(self,msg):
        self.msg=msg
