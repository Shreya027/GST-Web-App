"""Tax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from TaxApp import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index2/', views.index2),
    url(r'^inventory/', views.inventory),
    url(r'^index/', views.index),
    
    url(r'^login/', views.gst_login),
    url(r'^register/', views.gst_register),
    url(r'^logout_page/', views.gst_logout),
   
    url(r'^about/', views.about),

    url(r'^maps/', views.map),
    #url(r'^logincss/', views.logincss),
    url(r'^bill/', views.bill),
   
  
]





if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
