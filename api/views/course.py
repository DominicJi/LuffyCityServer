from api import models
from rest_framework.views import APIView
from rest_framework.response import Response
from api.utils.Seralizers import CoursesSer,CourseDetailSer
class CourseView(APIView):
    def get(self,request,*args,**kwargs):
        course_list=models.Course.objects.all()
        cs=CoursesSer(course_list,many=True)
        return Response(cs.data)

class CourseDetailView(APIView):
    def get(self,request,pk,*args,**kwargs):
        course_detail_obj=models.CourseDetail.objects.filter(course_id=pk).first()
        cds=CourseDetailSer(course_detail_obj)
        return Response(cds.data)