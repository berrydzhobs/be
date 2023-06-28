from django.contrib import admin
from django.urls import path,include

#Start My imports static files 
from django.conf import settings
from django.conf.urls.static import static
#End my static files imports


urlpatterns = [
    path('00-0-00/', admin.site.urls),
    path('', include('Content.urls')),
    path('', include('Feed.urls')),
    path('', include('Profile.urls')),
    path('', include('Core.urls')),
    path('', include('Page.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)