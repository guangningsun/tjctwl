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