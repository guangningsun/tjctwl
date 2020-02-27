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
    
    class Meta:
        model = Dangerrectification
        fields = ('danger_create_user','danger_floor_level','danger_address_detail','danger_desc', \
        'danger_image','danger_create_time','danger_status','danger_level','danger_type')

class EventSerializer(serializers.ModelSerializer):
    # event_create_time = serializers.CharField(required=False)
    # event_device_location = serializers.CharField(required=False)
    # event_msg = serializers.CharField(required=False)
    # if_read = serializers.CharField(required=False)

    class Meta:
        model = EventInfo
        fields = ('if_read','event_create_time','event_device_location','event_msg')