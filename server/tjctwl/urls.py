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
from AppModel import admin as appadmin
# from AppModel.urls import router as app_router

# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns = [
    url('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.+)$', serve, {'document_root': settings.MEDIA_ROOT}),
    
    # url(r'^api/', include(app_router.urls)),
    url(r'^user_login/', views.user_login),
    url(r'^reset_password/', views.reset_password),
    url(r'^get_user_device_index_info/', views.get_user_device_index_info),
    path('user_opt_device/', views.user_opt_device),
    path('user_opt_device/<int:pk>/', views.user_opt_device_detail),
    path('device/', views.device_detail),
    path('device/<int:sn>/', views.device_opt_detail),
    path('danger/', views.danger_detail),
    path('event/<int:user_id>/<int:start_index>/<int:num>/<start_time>/<end_time>', views.event_detail),
    url(r'^update_event_read_state/', views.update_event_read_state),
    url(r'^update_event_read_state_all/', views.update_event_read_state_all),
    path('install_device/<int:start_index>/<int:num>', views.install_device_detail),
    path('install_device/<int:sn>', views.install_device_get_by_sn),
    path('install_device/<phone_number>', views.install_device_update),
    url(r'^get_install_by_device_sn/', views.get_install_by_device_sn),
    path('admin_danger/<int:start_index>/<int:num>/<status>', views.admin_danger_detail),
    path('admin_danger/<int:danger_id>', views.admin_danger_modify),
    url(r'^update_danger_status/', views.update_danger_status),
    
    
    
    

] 
 
