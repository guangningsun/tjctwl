# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin, ExportActionModelAdmin
import logging,json
import AppModel.aeptools as aeptools
from django.utils.html import format_html
from django import forms
from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin
from feincms.module.page.models import Page


logger = logging.getLogger(__name__)
logger.setLevel(level = logging.DEBUG)
handler = logging.FileHandler("tjctwl.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


SECRET_ID = "un2puu02Ml"
APPLICATION_ID = "AMQROxaUNh"
VERSION = "20181031202055"
MasterKey = "ffd9c7a217004acc87f2df46c348e8d2"
PRODUCTID = 10035737


def _if_exist(str):
    if str is not None:
        return str
    else:
        return ""

@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin):
    list_display=['id','login_name','username','user_permission','phone_number','create_time','user_sex','user_age','description']
    #list_editable = ['login_name','username','user_permission','phone_number','user_sex','user_age','description']
    #search_fields =('login_name','username','user_permission','phone_number','create_time','user_sex','user_age','description')
    #fieldsets = [
     #   ('用户数据', {'fields': ['login_name','username','user_permission','phone_number','create_time','user_sex','user_age','description'], 'classes': ['collapse']}),
    #]
    #filter_horizontal = ('device_name',)
    def save_model(self, request, obj, form, change):
        logger.info("save user info  in tjctwl platform")
        # 若绑定了设备则将设备的已上线状态修改为true
        for i in range(0,len(obj.device_name.get_queryset())):
            device_obj = obj.device_name.get_queryset()[i]
            DeviceInfo.objects.filter(id=device_obj.id).update(isOnline='0')
        # 更新设备监控表，将用户信息和设备信息同时记录
        OnlineDeviceInfoAdmin.save_model(request, obj, form, change)
        super().save_model(request, obj, form, change)


@admin.register(Patrolscheme)
class PatrolschemeAdmin(admin.ModelAdmin):
    list_display=['scheme_id','scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc']
    list_editable = ['scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc']
    search_fields =('scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc')
    fieldsets = [
        ('Date information', {'fields': ['scheme_name','scheme_frequency','scheme_start_time','scheme_end_time','scheme_devices','scheme_desc'], 'classes': ['collapse']}),
    ]


class UserInfoInline(admin.TabularInline):
    model = UserInfo
    #filter_horizontal = ('device_name',)
    #raw_id_fields = ("device_name","device_name")


@admin.register(DeviceInfo)
class DeviceInfoAdmin(ImportExportModelAdmin):
    #list_display = ['id','device_name','productId','imei','deviceStatus','trans_autoObserver','createTime','createBy','netStatus','onlineAt','offlineAt','operation','isOnline']
    list_display = ['id','device_name','productId','imei','category','deviceStatus','trans_autoObserver','createTime','createBy','netStatus','onlineAt','offlineAt','trans_isOnline']
    list_filter = ('device_name','imei')
    #list_editable = ['device_name','productId','imei','autoObserver']
    search_fields =('id','device_name','device_sn','tenantId','productId','imei','deviceStatus','autoObserver','createTime','createBy','updateTime','updateBy','netStatus','onlineAt','offlineAt')
    fieldsets = [
        ('创建设备', {'fields': ['device_name','productId','imei','autoObserver','category'], 'classes': ['collapse']}),
    ]
    #actions = ["delete_model"]
    list_per_page = 10
    list_display_links = ('id', 'device_name')
    
    # 修改返回值的展示内容
    def trans_autoObserver(self, obj):
        if obj.autoObserver == '0':
            return "已订阅"
        else:
            return "未订阅"
    trans_autoObserver.short_description = '是否订阅'

    def trans_isOnline(self, obj):
        if obj.isOnline == '0':
            return "已上线"
        else:
            return "未上线"
    trans_isOnline.short_description = '是否上线'
    
    #def operation(self, obj):
    #    parameter_str = 'id={}'.format(str(obj.id))
    #    color_code = ''
    #    btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
    #              '<input name="绑定用户"' \
    #              'type="button" id="passButton" ' \
    #              'title="passButton" value="绑定用户">' \
    #              '</a>'
    #    return format_html(btn_str, '/pass_audit/?{}'.format(parameter_str))
    #operation.short_description = '上线绑定'

    # 增加自定义按钮
    #def save(self, request):
    #		# 禁用添加按钮
    #    return True
    
    # 重写已有CRUD方法
    def save_model(self, request, obj, form, change):
        version = 20181031202117
        path = "/aep_device_management/device"
        param = {}
        if request.POST:
            body = "{\"deviceName\": \""+request.POST["device_name"]+"\",\"deviceSn\": \"MQTT\",\"imei\": \""+ \
                        request.POST["imei"]+"\",\"operator\": \""+request.user.username+"\",\"other\": {\"autoObserver\": "+ \
                        request.POST["autoObserver"]+"},\"productId\": "+request.POST["productId"]+"}"
            logger.info("create device in aep platform")
            try:
                logger.debug("create device in aep platform %s" % (body))
                res =  aeptools.sendSDKRequest(path,{},param,body,version,APPLICATION_ID,MasterKey,SECRET_ID)
                res_json = json.loads(res.read())
                if res_json["msg"] == "ok":
                    response_device_data = res_json["result"]
                    obj.id = response_device_data["deviceId"]
                    obj.tenantId = _if_exist(response_device_data["tenantId"])
                    obj.deviceStatus = _if_exist(response_device_data["deviceStatus"])
                    obj.createBy = _if_exist(response_device_data["createBy"])
                    obj.netStatus = _if_exist(response_device_data["netStatus"])
                    obj.createTime = _if_exist(response_device_data["createTime"])
                    obj.lastTime = _if_exist(response_device_data["lastTime"])
                    obj.onlineAt = _if_exist(response_device_data["onlineAt"])
                    obj.offlineAt = _if_exist(response_device_data["offlineAt"])    
                    logger.info("update obj whitch will create in tjctwl platform")            
                else:
                    logger.info("aep platform create device failed")
            except:
                logger.info("create device in aep platform failed")
        logger.info("save device in tjctwl platform")
        super().save_model(request, obj, form, change)
    

    def delete_model(self, request, obj):
        logger.info("delete device test============")
        super().delete_model(request, obj)
    

    def delete_queryset(self, request, queryset):
        logger.info("delete device query test============")
        version = 20181031202131
        path = "/aep_device_management/device"
        if request.POST:
            for i in range(0,len(queryset)):
                #param ={}
                param = {
                         'deviceIds': queryset[i].id ,
                         'productId': queryset[i].productId 
                         }
                #body = "{\"deviceIds\": \""+queryset[i].device_id+"\",\"productId\": "+queryset[i].productId+"}"
                body = '{}'
                try:
                    logger.debug("delete device in aep platform %s" % (param))
                    res =  aeptools.sendSDKRequest(path,{},param,body,version,APPLICATION_ID,MasterKey,SECRET_ID,'DELETE')
                except:
                    logger.info("delete device in aep platform failed")
        logger.info("delete device in tjctwl platform")
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
    

@admin.register(MappingUserinfoDeviceName)
class MappingUserinfoDeviceNameAdmin(ImportExportModelAdmin):
    list_display = ['userinfo','deviceinfo']

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
    #change_form_template = 'area.html'


@admin.register(CompanyInfo)
class CompanyInfoAdmin(ImportExportModelAdmin):
    list_display = ['company_name','category','latitude','company_address','responsible_person','responsible_number','detectors_number','fire_brigade','fire_number']
    #list_editable = ['company_name','category','latitude','company_address','responsible_person','responsible_number','detectors_number','fire_brigade','fire_number']
    search_fields =('company_name','category','latitude','company_address','responsible_person','responsible_number','detectors_number','fire_brigade','fire_number')
    fieldsets = [
        ('联网单位信息', {'fields': ['company_name','category','latitude','company_address','responsible_person','responsible_number','detectors_number','fire_brigade','fire_number'], 'classes': ['collapse']}),
    ]
    list_display_links = ('company_name',)


@admin.register(OnlineDeviceInfo)
class OnlineDeviceInfoAdmin(ImportExportModelAdmin):
    list_display = ['device_name','device_sn','updateTime','deviceStatus','netStatus','onlineAt','offlineAt','bond_user','deviceOnlineStatus','deviceVoltageStatus','address_desc','charge_phonenumber','charge_person','company_name','company_id','ownerName','lastUploadTime','ownerPhoneNumber','longitude_latitude']
    #list_editable = ['device_name','device_sn','updateTime','deviceStatus','netStatus','onlineAt','offlineAt','bond_user','deviceOnlineStatus','deviceVoltageStatus','address_desc','charge_phonenumber','charge_person','company_name','company_id','ownerName','lastUploadTime','ownerPhoneNumber','longitude_latitude']
    search_fields =('device_name','device_sn','updateTime','deviceStatus','netStatus','onlineAt','offlineAt','bond_user','deviceOnlineStatus','deviceVoltageStatus','address_desc','charge_phonenumber','charge_person','company_name','company_id','ownerName','lastUploadTime','ownerPhoneNumber','longitude_latitude')
    fieldsets = [
        ('Date information', {'fields': ['device_name','device_sn','updateTime','deviceStatus','netStatus','onlineAt','offlineAt','bond_user','deviceOnlineStatus','deviceVoltageStatus','address_desc','charge_phonenumber','charge_person','company_name','company_id','ownerName','lastUploadTime','ownerPhoneNumber','longitude_latitude'], 'classes': ['collapse']}),
    ]
 
    #inlines = [
    #    UserInfoInline,
    #]
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


@admin.register(AlarmInfo)
class AlarmInfoAdmin(ImportExportModelAdmin):
    list_display = ['alarm_id','company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling']
    list_editable = ['company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling']
    search_fields =('company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling')
    fieldsets = [
        ('Date information', {'fields': ['company_name','device_sn','alarm_time','alarm_status','alarm_desc','alarm_handling'], 'classes': ['collapse']}),
    ]


# 联网单位设置
#
# 'indented_title'
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','category','createtime','createuser','connected_number','slug']


admin.site.register(Category , MPTTModelAdmin)


admin.site.site_title = "天津城投物联后台管理"
admin.site.site_header = "天津城投物联"


