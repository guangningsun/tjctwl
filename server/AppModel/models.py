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


class CompanyInfo(models.Model):
    fire_rating_number = (('0', u'一级'), ('1', u'二级'))
    company_id = models.CharField(max_length=200,verbose_name='联网单位ID')
    company_name = models.CharField(max_length=200,verbose_name='单位全称')
    established_time = models.CharField(max_length=200,verbose_name='成立时间')
    company_address = models.CharField(max_length=200,verbose_name='单位地址')
    post_number =  models.CharField(max_length=200,verbose_name='邮政编码')
    floor_area = models.CharField(max_length=200,verbose_name='占地面积')
    fire_rating = models.CharField(max_length=200,choices=fire_rating_number,verbose_name='防火等级')
    detectors_number = models.CharField(max_length=200,verbose_name='探测器数量')
    fire_brigade = models.CharField(max_length=200,verbose_name='所属消防队')
    region = models.CharField(max_length=200,verbose_name='所属区域')
    class Meta:
        verbose_name = '联网单位'
        verbose_name_plural = '联网单位'


class DeviceInfo(models.Model):
    device_id = models.CharField(max_length=200,verbose_name='设备ID')
    device_name = models.CharField(max_length=200,verbose_name='设备名称')
    device_sn = models.CharField(max_length=200,verbose_name='设备编号')
    tenantId = models.CharField(max_length=200,verbose_name='租户Id')
    productId = models.CharField(max_length=200,verbose_name='产品Id')
    imei = models.CharField(max_length=200,verbose_name='IMEI号')
    deviceStatus = models.CharField(max_length=200,verbose_name='设备状态')
    autoObserver = models.CharField(max_length=200,verbose_name='是否订阅')
    createTime = models.CharField(max_length=200,verbose_name='创建时间')
    createBy = models.CharField(max_length=200,verbose_name='创建者')
    updateTime = models.CharField(max_length=200,verbose_name='更新时间')
    updateBy = models.CharField(max_length=200,verbose_name='更新者')
    netStatus = models.CharField(max_length=200,verbose_name='状态')
    onlineAt = models.CharField(max_length=200,verbose_name='最后上线时间')
    offlineAt = models.CharField(max_length=200,verbose_name='最后离线时间')

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'
        
    
class InstitutionInfo(models.Model):
    institution_id = models.CharField(max_length=200,verbose_name='组织机构ID')
    company_name = models.CharField(max_length=200,verbose_name='公司名称')
    superior_department = models.CharField(max_length=200,verbose_name='上级部门')
    create_time = models.CharField(max_length=200,verbose_name='创建时间')
    create_user = models.CharField(max_length=200,verbose_name='创建者')
    connact_number = models.CharField(max_length=200,verbose_name='联系电话')
    class Meta:
        verbose_name = '组织机构'
        verbose_name_plural = '组织机构'


class Patrolscheme(models.Model):
    scheme_id = models.CharField(max_length=200,verbose_name='巡检ID')
    scheme_name = models.CharField(max_length=200,verbose_name='巡检名称')
    scheme_frequency = models.CharField(max_length=200,verbose_name='巡检频率')
    scheme_start_time = models.CharField(max_length=200,verbose_name='开始时间')
    scheme_end_time = models.CharField(max_length=200,verbose_name='结束时间')
    scheme_devices = models.CharField(max_length=200,verbose_name='巡检设备')
    scheme_desc = models.CharField(max_length=200,verbose_name='巡检描述')
    class Meta:
        verbose_name = '巡检计划'
        verbose_name_plural = '巡检计划'


class Dangerrectification(models.Model):
    danger_id = models.CharField(max_length=200,verbose_name='隐患ID')
    danger_level = models.CharField(max_length=200,verbose_name='隐患级别')
    danger_type = models.CharField(max_length=200,verbose_name='隐患类型')
    danger_create_user = models.CharField(max_length=200,verbose_name='创建者')
    danger_floor_level = models.CharField(max_length=200,verbose_name='楼层')
    danger_address_detail = models.CharField(max_length=200,verbose_name='具体位置')
    danger_status = models.CharField(max_length=200,verbose_name='隐患状态')
    danger_create_time = models.CharField(max_length=200,verbose_name='创建时间')
    if_reject = models.CharField(max_length=200,verbose_name='是否驳回')
    class Meta:
        verbose_name = '隐患整改'
        verbose_name_plural = '隐患整改'


class AlarmInfo(models.Model):
    pre_handling_text = fire_rating_number = (('0', u'真实警情-小型'), \
                                      ('1', u'真实警情-大型'), \
                                      ('2', u'真实警情-大型（不启预案）'),\
                                      ('3', u'真实故障'),\
                                      ('4', u'人为误报'))
    alarm_id =  models.CharField(max_length=200,verbose_name='报警ID')
    company_name =  models.CharField(max_length=200,verbose_name='联网单位')
    device_sn =  models.CharField(max_length=200,verbose_name='设备编码')
    alarm_time =  models.CharField(max_length=200,verbose_name='报警时间')
    alarm_status =  models.CharField(max_length=200,verbose_name='状态')
    alarm_desc =  models.CharField(max_length=200,verbose_name='报警详情')
    alarm_handling =  models.CharField(max_length=200,choices=pre_handling_text,verbose_name='警情处理')
    class Meta:
        verbose_name = '报警中心'
        verbose_name_plural = '报警中心'

