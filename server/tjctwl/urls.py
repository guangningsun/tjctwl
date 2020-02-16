"""apollo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from tjctwl import views
from django.conf.urls import include, url
from django.urls import path,re_path
from django.views.static import serve
# from django.conf.urls.static import static
from django.conf import settings

# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.init_web),
    re_path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT}),

    url(r'^user_login/', views.user_login),
    url(r'^reset_password/', views.reset_password),
    url(r'^get_user_device_index_info/', views.get_user_device_index_info),
    
] 
 
