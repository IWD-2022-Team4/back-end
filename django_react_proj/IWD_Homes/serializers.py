from rest_framework import serializers

from .models import User, Host

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'name', 'email', 'city', 'phone','disability', 'other')



class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        fields = ('pk', 'name', 'email', 'city', 'phone','disability', 'other')