# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
import logging,json
import AppModel.aeptools as aeptools


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("tjctwl.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


SECRET_ID = "un2puu02Ml"
APPLICATION_ID = "AMQROxaUNh"
VERSION = "20181031202055"
MasterKey = "ffd9c7a217004acc87f2df46c348e8d2"
PRODUCTID = 10035737

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display=['user_id','login_name','username']
    list_editable = ['login_name', 'username']
    search_fields =('login_name', 'username')
    fieldsets = [
        ('Date information', {'fields': ['login_name'], 'classes': ['collapse']}),
    ]

@admin.register(Patrolscheme)
class PatrolschemeAdmin(admin.ModelAdmin):
    list_display=['scheme_id','scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc']
    list_editable = ['scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc']
    search_fields =('scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc')
    fieldsets = [
        ('Date information', {'fields': ['scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc'], 'classes': ['collapse']}),
    ]


@admin.register(DeviceInfo)
class DeviceInfoAdmin(ImportExportModelAdmin):
    list_display = ['device_id','device_address','device_name','device_status','device_address_detail']
    list_editable = ['device_address','device_name','device_status','device_address_detail']
    search_fields =('device_id','device_address','device_name','device_status','device_address_detail')
    fieldsets = [
        ('Date information', {'fields': ['device_id','device_address', \
            'device_name','device_status','device_address_detail'], 'classes': ['collapse']}),
    ]
    #actions = ["delete_model"]
    #delete_model.icon = 'fas fa-delete'
    def save_model(self, request, obj, form, change):
        version = 20181031202117
        path = "/aep_device_management/device"
        param = {}
        body = '{"deviceName": "ttttt","deviceSn": "MQTT","imei": "866971036327615","operator": "szy","other": {"autoObserver": 0},"productId": 10035737}'
        logger.info("create device in aep platform============")
        res =  aeptools.sendSDKRequest(path,{},param,body,version,APPLICATION_ID,MasterKey,SECRET_ID)
        logger.info("save device test============")
        logger.info(json.loads(res.read()))
        super().save_model(request, obj, form, change)
    

    def delete_model(self, request, obj):
        logger.info("delete device test============")
        super().delete_model(request, obj)
    

    def delete_queryset(self, request, queryset):
        logger.info("delete device query test============")
        super().delete_queryset(request, queryset)

    def get_search_results(self, request, queryset, search_term):
        logger.info("get all device test============")
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(age=search_term_as_int)
        return queryset, use_distinct
    
    


@admin.register(Dangerrectification)
class DangerrectificationAdmin(ImportExportModelAdmin):
    list_display = ['danger_id','danger_level','danger_type','danger_create_user','danger_floor_level','danger_address_detail','danger_status','danger_create_time','if_reject']
    list_editable = ['danger_level','danger_type','danger_create_user','danger_floor_level','danger_address_detail','danger_status','danger_create_time','if_reject']
    search_fields =('danger_level','danger_type','danger_create_user','danger_floor_level','danger_address_detail','danger_status','danger_create_time','if_reject')
    fieldsets = [
        ('Date information', {'fields': ['danger_level','danger_type','danger_create_user',\
            'danger_floor_level','danger_address_detail','danger_status','danger_create_time','if_reject'], 'classes': ['collapse']}),
    ]



@admin.register(InstitutionInfo)
class InstitutionInfoAdmin(ImportExportModelAdmin):
    list_display = ['institution_id','company_name','superior_department','create_time','create_user','connact_number']
    list_editable = ['company_name','superior_department','create_time','create_user','connact_number']
    search_fields =('company_name','superior_department','create_time','create_user','connact_number')
    fieldsets = [
        ('Date information', {'fields': ['company_name','superior_department','create_time','create_user','connact_number'], 'classes': ['collapse']}),
    ]


@admin.register(CompanyInfo)
class CompanyInfoAdmin(ImportExportModelAdmin):
    list_display = ['company_id','company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region']
    list_editable = ['company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region']
    search_fields =('institution_id','company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region')
    fieldsets = [
        ('Date information', {'fields': ['institution_id','company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region'], 'classes': ['collapse']}),
    ]


@admin.register(AlarmInfo)
class AlarmInfoAdmin(ImportExportModelAdmin):
    list_display = ['alarm_id','company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling']
    list_editable = ['company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling']
    search_fields =('company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling')
    fieldsets = [
        ('Date information', {'fields': ['company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling'], 'classes': ['collapse']}),
    ]


# Register your models here.
#admin.site.register(UserInfo, UserInfoAdmin)
#admin.site.register(DeviceInfo, DeviceInfoAdmin)
admin.site.site_title = "天津城投物联后台管理"
admin.site.site_header = "天津城投物联"
