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

@admin.register(DeviceInfo)
class DeviceInfoAdmin(ImportExportModelAdmin):
    list_display = ['device_id','device_address','device_name','device_status','device_address_detail']
    # list_editable = ['device_id','device_address','device_name','device_status','device_address_detail']
    search_fields =('device_id','device_address','device_name','device_status','device_address_detail')
    fieldsets = [
        ('Date information', {'fields': ['device_id','device_address', \
            'device_name','device_status','device_address_detail'], 'classes': ['collapse']}),
    ]


@admin.register(InstitutionInfo)
class InstitutionInfoAdmin(ImportExportModelAdmin):
    list_display = ['institution_id','company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region']
    # list_editable = ['institution_id','company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region']
    search_fields =('institution_id','company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region')
    fieldsets = [
        ('Date information', {'fields': ['institution_id','company_name','established_time','company_address','post_number','floor_area','fire_rating','detectors_number','fire_brigade','region'], 'classes': ['collapse']}),
    ]


# Register your models here.
#admin.site.register(UserInfo, UserInfoAdmin)
#admin.site.register(DeviceInfo, DeviceInfoAdmin)
admin.site.site_title = "天津城投物联后台管理"
admin.site.site_header = "天津城投物联"
