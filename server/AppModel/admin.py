# -*- coding:UTF-8 -*-
from django.contrib import admin
from AppModel.models import UserInfo



class UserInfoAdmin(admin.ModelAdmin):
    list_display=['user_id','login_name','username']
    list_editable = ['login_name', 'username']
    search_fields =('login_name', 'username')
    fieldsets = [
        ('Date information', {'fields': ['login_name'], 'classes': ['collapse']}),
    ]


# Register your models here.
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.site_title = "天津城投物联后台管理"
admin.site.site_header = "天津城投物联"
