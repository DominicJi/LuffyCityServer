
class BaseResponse(object):
    '''
    定义一个产生固定格式的回复消息类
    这样每次就需要我们自己定义回复消息数据
    直接实例化该类即可获取相应数据结构的回复消息格式
    '''
    def __init__(self):
        self.data=None
        self.error_msg=''
        self.code=1000

    @property
    def dict(self):
        return self.__dict__