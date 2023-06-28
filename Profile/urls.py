from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports

from . import views



urlpatterns = [
        path('author/<str:slug>/articles/', views.Authorarticles.as_view(),name='Authorarticles'),
        path('author/<str:slug>/tools/', views.Authortools.as_view(),name='Authortools'),
        path('author/<str:slug>/items/', views.Authoritems.as_view(),name='Authoritems'),
        path('author/<str:slug>/projects/', views.Authorprojects.as_view(),name='Authorprojects'),
        path('author/<str:slug>/services/', views.Authorservices.as_view(),name='Authorservices'),
        path('author/<str:slug>/',views.AuthorView.as_view(),name='profile'),
    ]