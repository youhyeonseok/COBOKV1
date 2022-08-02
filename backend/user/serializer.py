from rest_framework import serializers
from .models import User

class UserSerialrizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','password','date']