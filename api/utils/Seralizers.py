from rest_framework import serializers
from api import models

#序列化Course表的所有字段数据
class CoursesSer(serializers.ModelSerializer):
    class Meta:
        model=models.Course
        fields='__all__'

class CourseDetailSer(serializers.ModelSerializer):
    class Meta:
        model=models.CourseDetail
        fields='__all__'
    #我们需要额外提供一些课程表的字段信息,sourse里面跟的是该表对象要点的后续字段
    course_name=serializers.CharField(source='course.name')
    course_img=serializers.CharField(source='course.course_img')
    course_brief=serializers.CharField(source='course.brief')
    #针对多对多的外键字段需要用以下的方式,前面的变量名必须是字段名
    teachers=serializers.SerializerMethodField()
    #定义函数，函数名后缀也必须是字段名
    def get_teachers(self,obj):
        '''
        这里的obj就是循环的当前表对象
        :param obj:
        :return:
        '''
        tmp=[]
        for i in obj.teachers.all():
            tmp.append(i.name)
        return tmp
    #还需要给出相关联的课程名称
    recommend_courses=serializers.SerializerMethodField()
    def get_recommend_courses(self,obj):
        '''
        在给前端构造数据时应该考虑到需要什么样的数据，已经改数据是否还需要关联其他数据，
        如果是则应该将该数据的主键也一并给出
        :param obj:
        :return:
        '''
        tmp=[]
        for i in obj.recommend_courses.all():
            tmp.append({
                'name':i.name,
                'pk':i.pk
            })
        return tmp
    #课程详细展示页面还需要向用户展示具体课程章节以及课时，常见问题等
    chapter_section=serializers.SerializerMethodField()
    def get_chapter_section(self,obj):
        data_list={}
        for i in obj.course.chapter_set.all():
            tmp=[]
            for j in i.course_sections.all():
                tmp.append(j.name)
            data_list[i.name]=tmp
        return data_list
    price_policy=serializers.SerializerMethodField()
    def get_price_policy(self,obj):
        tmp=[]
        for i in obj.course.price_policy.all():
            tmp.append([i.price,i.get_valid_period_display()])
        return tmp
    questions=serializers.SerializerMethodField()
    def get_questions(self,obj):
        tmp=[]
        for i in models.OftenAskedQuestion.objects.filter(object_id=obj.course.pk):
            tmp.append([i.question,i.answer])
        return tmp
