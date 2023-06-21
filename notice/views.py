from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import noticeSerializer
from django.http import Http404, HttpResponse, HttpResponseForbidden,JsonResponse
from rest_framework import viewsets,status,serializers
from .models import notice
from django.contrib.auth.decorators import login_required

class NoticeView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset= notice.objects.all().order_by('-date')
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1 
        instance.save()
        
        return super().retrieve(request, *args, **kwargs)
    


class NoticeQueryView(viewsets.ModelViewSet):
    serializer_class =noticeSerializer
    queryset = notice.objects.all().order_by('-date')
    
    @action(detail=False, methods=['get'])
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
        print(data)
        super().create(request, *args, **kwargs)
        return HttpResponse({"success"},status=status.HTTP_200_OK)
        
        
        
