"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path 
#from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls import url

app_name='music'

urlpatterns = [
	#/music/
    path('', views.IndexView.as_view(),name='home'),


    #/music/21/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="details"),

    url(r'album/add/$',views.AlbumCreate.as_view(),name="album_add"),

  
]
