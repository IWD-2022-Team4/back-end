from rest_framework import serializers


from .models import User, Host




class UserSerializer(serializers.ModelSerializer):
    disability = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('pk', 'name', 'email', 'city', 'phone','disability', 'other', 'bio', 'host')

    def get_disability(self,obj):
        return obj.get_disability_display()



class HostSerializer(serializers.ModelSerializer):
    disability = serializers.SerializerMethodField()

    class Meta:
        model = Host
        fields = ('pk', 'name', 'email', 'city', 'phone','disability', 'other', 'bio', 'host', 'available')
    
    def get_disability(self,obj):
        return obj.get_disability_display()


