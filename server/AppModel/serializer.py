from rest_framework import serializers
from AppModel.models import *

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print (validated_data)
        return UserInfo.objects.save()
        # return Userinfo.objects.save(**validated_data)
    class Meta:
        model = UserInfo
        fields = ('username',)