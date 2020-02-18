# coding: utf-8
from rest_framework import routers
from tjctwl.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'userinfo', UserViewSet)