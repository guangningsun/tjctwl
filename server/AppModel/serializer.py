from rest_framework import serializers
from AppModel.models import *
from rest_framework.decorators import api_view

class UserSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):

    #     print (validated_data)

    #     # DeviceInfo.objects.filter(id=1).update(name='Google')
    #     # return UserInfo.objects.save()
    #     # return Userinfo.objects.save(**validated_data)

    class Meta:
        model = UserInfo
        fields = ('device_sn',)


class DeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeviceInfo
        fields = ('device_name','install_location','device_address')


class DangerSerializer(serializers.ModelSerializer):
    danger_status = serializers.CharField(required=False)
    danger_level = serializers.CharField(required=False)
    danger_type = serializers.CharField(required=False)
    id = serializers.CharField(required=False)
    danger_create_user = serializers.CharField(required=False)
    danger_floor_level = serializers.CharField(required=False)
    danger_address_detail = serializers.CharField(required=False)
    danger_desc = serializers.CharField(required=False)
    danger_image = serializers.ImageField(required=False)
    danger_create_time = serializers.CharField(required=False)

    class Meta:
        model = Dangerrectification
        fields = ('id','danger_create_user','danger_floor_level','danger_address_detail','danger_desc', \
        'danger_image','danger_create_time','danger_status','danger_level','danger_type')

class EventSerializer(serializers.ModelSerializer):
    # event_create_time = serializers.CharField(required=False)
    # event_device_location = serializers.CharField(required=False)
    # event_msg = serializers.CharField(required=False)
    # if_read = serializers.CharField(required=False)

    class Meta:
        model = EventInfo
        fields = ('id','if_read','event_create_time','event_device_location','event_msg')


class InstallDeviceSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    deviceStatus = serializers.CharField(required=False)
    construction_image = serializers.CharField(required=False)
    # device_sn = serializers.CharField(required=False)
    # device_name = serializers.CharField(required=False)
    # construction_worker = serializers.CharField(required=False)
    # install_location = serializers.CharField(required=False)
    # device_address = serializers.CharField(required=False)

    class Meta:
        model = DeviceInfo
        fields = ('id','construction_createtime','deviceStatus','construction_image','device_sn','device_name',\
            'construction_worker','install_location','device_address')

