# -*- coding:UTF-8 -*-
from django.db import models


# 0 超级管理员
# 1 管理员
# 2 老师
# 3 普通用户，学生
# 用户类
class UserInfo(models.Model):
    user_id = models.CharField(max_length=200,verbose_name='用户ID')
    login_name = models.CharField(max_length=200,verbose_name='登录名')
    username = models.CharField(max_length=200,verbose_name='用户名')
    password = models.CharField(max_length=200,verbose_name='用户名')
    user_permission = models.CharField(max_length=200,verbose_name='用户名')
    create_time = models.CharField(max_length=200,verbose_name='用户名')
    is_deleted = models.CharField(max_length=200,verbose_name='用户名')
    description = models.CharField(max_length=200,verbose_name='用户名')
    class_id = models.CharField(max_length=200,verbose_name='用户名')
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'



