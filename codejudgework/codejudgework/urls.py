"""codejudgework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path

from recruiter import views

urlpatterns = [
    url(r'^$',views.register,name='register'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^recruiter/',include('recruiter.urls')),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^dashboard/createtest/$',views.createtest, name='createtest'),
    url(r'^dashboard/assignment/$',views.assignment,name='assignments'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),

]
