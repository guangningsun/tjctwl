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



class DeviceInfo(models.Model):
    device_id = models.CharField(max_length=200,verbose_name='设备ID')
    device_name = models.CharField(max_length=200,verbose_name='设备名称')
    device_address = models.CharField(max_length=200,verbose_name='部件地址')
    device_address_detail = models.CharField(max_length=200,verbose_name='具体位置')
    device_status = models.CharField(max_length=200,verbose_name='设备状态')
    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'
        
    
class InstitutionInfo(models.Model):
    fire_rating_number = (('0', u'一级'), ('1', u'二级'))
    institution_id = models.CharField(max_length=200,verbose_name='组织机构ID')
    company_name = models.CharField(max_length=200,verbose_name='单位全称')
    established_time = models.CharField(max_length=200,verbose_name='成立时间')
    company_address = models.CharField(max_length=200,verbose_name='单位全称')
    post_number =  models.CharField(max_length=200,verbose_name='邮政编码')
    floor_area = models.CharField(max_length=200,verbose_name='占地面积')
    fire_rating = models.CharField(max_length=200,choices=fire_rating_number,verbose_name='防火等级')
    detectors_number = models.CharField(max_length=200,verbose_name='探测器数量')
    fire_brigade = models.CharField(max_length=200,verbose_name='所属消防队')
    region = models.CharField(max_length=200,verbose_name='所属区域')
    class Meta:
        verbose_name = '组织机构'
        verbose_name_plural = '组织机构'
    





