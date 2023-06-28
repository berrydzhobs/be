from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports

from . import views


urlpatterns = [
    path('i/starter', views.contact,name='Start'),
    path('><int:pk>',views.Funnel_Detail.as_view(),name='funnel'),
    ]