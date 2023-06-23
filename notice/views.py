from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import noticeSerializer,versionSerializer
from django.http import Http404, HttpResponse, HttpResponseForbidden,JsonResponse
from rest_framework import viewsets,status,serializers
from .models import notice,version
from django.contrib.auth.decorators import login_required

class NoticeView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset= notice.objects.all().order_by('-date')
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1 
        instance.save()
        
        return super().retrieve(request, *args, **kwargs)
    
    def get_filter(self,request):
        category = request.GET.get('category')
        queryset = self.get_queryset()
        if category:
            queryset = queryset.filter(category=category)
        serialized_data = self.serializer_class(queryset, many=True)
        return Response(serialized_data.data, status=200)



class NoticeAdminView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset= notice.objects.all()
    def create(self,request,*args, **kwargs):
        data = request.data
        super().create(request, *args, **kwargs)
        return HttpResponse({"success"},status=200)
        
        
class versionView(viewsets.ModelViewSet):
    serializer_class = versionSerializer
    queryset = version.objects.all().order_by('-id')

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.first()  # 첫 번째 객체만 반환
        return obj   
    
    def get_version(self, request):
        serialized_data = self.serializer_class(self.get_object())
        return Response(serialized_data.data, status=200)

class versionPostView(viewsets.ModelViewSet):
    serializer_class = versionSerializer
    queryset = version.objects.all()