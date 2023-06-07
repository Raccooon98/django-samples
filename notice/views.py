from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from .serializer import noticeSerializer
from django.http import Http404, HttpResponse, HttpResponseForbidden
from rest_framework import viewsets,status,serializers
from .models import notice
from django.contrib.auth.decorators import login_required

class NoticeView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset= notice.objects.all().order_by('-date')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class NoticeAdminView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset= notice.objects.all()
    def create_post(self,request,*args, **kwargs):
        if request.user.is_superuser:
            data = request.data
            return super().create(request, *args, **kwargs)
        return HttpResponseForbidden()
    
    def delete(self,request,pk,*args,**kwargs):
        
        if request.user.is_superuser:
            del_object = notice.objects.filter(id=pk)
            del_object.delete()
            return HttpResponse({"response":"success"},status=status.HTTP_200_OK)
        return HttpResponseForbidden()
        
        
        