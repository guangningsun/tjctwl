# -*- coding:UTF-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page


class DeviceInfo(models.Model):
    id = models.CharField(max_length=200,verbose_name='设备ID',primary_key=True)
    device_name = models.CharField(max_length=200,verbose_name='设备名称')
    device_sn = models.CharField(max_length=200,verbose_name='设备编号')
    tenantId = models.CharField(max_length=200,verbose_name='租户Id')
    productId = models.CharField(max_length=200,verbose_name='产品Id')
    imei = models.CharField(max_length=200,verbose_name='IMEI号')
    category = TreeForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True,verbose_name='所属单位')
    deviceStatus = models.CharField(max_length=200,verbose_name='设备状态')
    autoObserver = models.CharField(max_length=200,verbose_name='是否订阅')
    createTime = models.CharField(max_length=200,verbose_name='创建时间')
    createBy = models.CharField(max_length=200,verbose_name='创建者')
    updateTime = models.CharField(max_length=200,verbose_name='更新时间')
    updateBy = models.CharField(max_length=200,verbose_name='更新者')
    netStatus = models.CharField(max_length=200,verbose_name='信号状态')
    onlineAt = models.CharField(max_length=200,verbose_name='最后上线时间')
    offlineAt = models.CharField(max_length=200,verbose_name='最后离线时间')
    isOnline = models.CharField(max_length=200,verbose_name='是否已上线')
    
    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'
    
    def profile(self):
        return str()
    
    def __str__(self):
        return self.device_name


class OnlineDeviceInfo(models.Model):
    device_name = models.CharField(max_length=200,verbose_name='设备名称')
    device_sn = models.CharField(max_length=200,verbose_name='设备编码')
    createTime = models.CharField(max_length=200,verbose_name='创建时间')
    updateTime = models.CharField(max_length=200,verbose_name='更新时间')
    deviceStatus = models.CharField(max_length=200,verbose_name='设备状态')
    netStatus = models.CharField(max_length=200,verbose_name='信号强度')
    onlineAt = models.CharField(max_length=200,verbose_name='最后上线时间')
    offlineAt = models.CharField(max_length=200,verbose_name='最后离线时间')
    deviceOnlineStatus = models.CharField(max_length=200,verbose_name='设备上线状态')
    deviceVoltageStatus = models.CharField(max_length=200,verbose_name='设备电压状态')
    lastUploadTime = models.CharField(max_length=200,verbose_name='上报时间')
    userinfo = models.ForeignKey('UserInfo',on_delete=models.CASCADE,null=True,blank=True,verbose_name='业主姓名')
    companyinfo = models.ForeignKey('CompanyInfo',on_delete=models.CASCADE,null=True,blank=True,verbose_name='联网单位')

    class Meta:
        verbose_name = '上线设备信息'
        verbose_name_plural = '上线设备信息'
    
    def profile(self):
        return str()
    
    def __str__(self):
        return self.device_name


class UserInfo(models.Model):
    id = models.CharField(max_length=200,verbose_name='用户ID',primary_key=True)
    login_name = models.CharField(max_length=200,verbose_name='用户名')
    username = models.CharField(max_length=200,verbose_name='姓名')
    password = models.CharField(max_length=200,verbose_name='密码')
    user_permission = models.CharField(max_length=200,verbose_name='权限')
    phone_number = models.CharField(max_length=200,verbose_name='手机号')
    create_time = models.CharField(max_length=200,verbose_name='创建时间')
    description = models.CharField(max_length=200,verbose_name='用户描述')
    user_sex = models.CharField(max_length=200,verbose_name='性别')
    user_age = models.CharField(max_length=200,verbose_name='年龄')
    #device_name = models.ForeignKey(DeviceInfo,on_delete="CASCADE",null=True, blank=True,verbose_name='设备名字')
    device_name = models.ManyToManyField(DeviceInfo,null=True, blank=True,verbose_name='设备名字')

    filter_horizontal = ('device_name',)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    
    def __str__(self):
        return self.username


class CompanyInfo(models.Model):
    # fire_rating_number = (('0', u'一级'), ('1', u'二级'))
    company_id = models.CharField(max_length=200,verbose_name='联网单位ID')
    company_name = models.CharField(max_length=200,verbose_name='单位全称')
    category = TreeForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True,verbose_name='上级部门')
    company_address = models.CharField(max_length=200,verbose_name='单位地址')
    latitude =  models.CharField(max_length=200,verbose_name='经纬度')
    # fire_rating = models.CharField(max_length=200,choices=fire_rating_number,verbose_name='防火等级')
    detectors_number = models.CharField(max_length=200,verbose_name='探测器数量')
    fire_brigade = models.CharField(max_length=200,verbose_name='所属消防队')
    fire_number = models.CharField(max_length=200,verbose_name='消防队电话')
    responsible_person = models.CharField(max_length=200,verbose_name='安全责任人')
    responsible_number = models.CharField(max_length=200,verbose_name='责任人电话')
    class Meta:
        verbose_name = '联网单位'
        verbose_name_plural = '联网单位'
    
    def __str__(self):
        return self.company_name


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
    
    def __str__(self):
        return self.company_name


class Patrolscheme(models.Model):
    scheme_frequency_list = (('0', u'一天'), ('1', u'一周'), ('1', u'一月'))
    scheme_name = models.CharField(max_length=200,verbose_name='巡检名称')
    scheme_frequency = models.CharField(max_length=200,choices=scheme_frequency_list,verbose_name='巡检频率')
    scheme_start_time = models.DateField(verbose_name='开始时间')
    scheme_end_time = models.DateField(verbose_name='结束时间')
    scheme_devices = models.ForeignKey('OnlineDeviceInfo',on_delete=models.CASCADE,null=True,blank=True,verbose_name='巡检设备')
    scheme_desc = models.CharField(max_length=200,verbose_name='巡检描述')
    class Meta:
        verbose_name = '巡检计划'
        verbose_name_plural = '巡检计划'
    
    def __str__(self):
        return self.scheme_name


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
    

class MappingUserinfoDeviceName(models.Model):
    userinfo = models.ForeignKey(UserInfo, models.DO_NOTHING,verbose_name='用户名')
    deviceinfo = models.ForeignKey(DeviceInfo, models.DO_NOTHING,verbose_name='设备名称')

    class Meta:
        managed = False
        db_table = 'AppModel_userinfo_device_name'
        unique_together = (('userinfo', 'deviceinfo'),)



# 联网单位
# class Genre(MPTTModel):
#     name = models.CharField(max_length=50, unique=True)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

#     class MPTTMeta:
#         level_attr = 'mptt_level'
#         order_insertion_by = ['name']

# 组织机构详细信息
class Post(models.Model):
      name = models.CharField(max_length=120,verbose_name='单位名称')
      category = TreeForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True,verbose_name='上级部门')
      createtime = models.CharField(max_length=200,verbose_name='创建时间')
      createuser = models.CharField(max_length=200,verbose_name='创建者')
      connected_number = models.CharField(max_length=200,verbose_name='联系电话')
      slug = models.SlugField(verbose_name='标签')
      
      def __str__(self):
          return self.name


# 组织机构
class Category(MPTTModel):
      name = models.CharField(max_length=50, unique=True,verbose_name='名称')
      parent = TreeForeignKey('self', null=True, blank=True,on_delete=models.CASCADE, related_name='children', db_index=True,verbose_name='上级部门')
      slug = models.SlugField(verbose_name='标签')
    
      class MPTTMeta:
        order_insertion_by = ['name']
    
      class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'
        verbose_name = '组织机构'
    
      def get_slug_list(self):
        try:
          ancestors = self.get_ancestors(include_self=True)
        except:
          ancestors = []
        else:
          ancestors = [ i.slug for i in ancestors]
        slugs = []
        for i in range(len(ancestors)):
          slugs.append('/'.join(ancestors[:i+1]))
        return slugs
    
      def __str__(self):
        return self.name

