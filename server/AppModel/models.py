# -*- coding:UTF-8 -*-
from django.db import models


# 0 超级管理员
# 1 管理员
# 2 老师
# 3 普通用户，学生
# 用户类
class UserInfo(models.Model):
    user_id = models.CharField(max_length=200)
    login_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_permission = models.CharField(max_length=200)
    create_time = models.CharField(max_length=200)
    is_deleted = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    class_id = models.CharField(max_length=200)



