from django.shortcuts import render
from rest_framework.response import Response
from .serializer import noticeSerializer
from django.http import Http404, HttpResponse, HttpResponseForbidden
from rest_framework import viewsets,status
from .models import notice
from django.contrib.auth.decorators import login_required

class NoticeView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset= notice.objects.all()
    
class NoticeAdminView(viewsets.ModelViewSet):
    serializer_class = noticeSerializer
    queryset= notice.objects.all()
    @login_required
    def create_post(self,request):
        if not request.user.is_superuser:
            return HttpResponseForbidden()
        data=request.data
        