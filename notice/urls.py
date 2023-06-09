"""
URL configuration for mmaiback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import NoticeView,NoticeAdminView,versionView,versionPostView

noticelist=NoticeView.as_view({
    'get': 'get_filter'
    
})
returnversion = versionView.as_view({
    'get':'get_version',
    'post':'create',
    'delete':'destroy'
})
postversion = versionPostView.as_view({
    'post':'create'
})
noticedetail=NoticeView.as_view({
    'get': 'retrieve',
    'delete':'destroy'
    
})
admincreatenotice = NoticeAdminView.as_view({
    'post': 'create' 
})

urlpatterns = [
    path('create/',admincreatenotice ),
    path('',noticelist),
    path('<int:pk>/',noticedetail),
    path('version/',returnversion),
    path('version/post/',postversion),
]

