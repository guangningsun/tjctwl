# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin



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
