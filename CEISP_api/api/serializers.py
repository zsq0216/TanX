from rest_framework import serializers
from account.models import Account,EnterpriseUser,Scope1emissions,Scope2emissions,Scope3emissions,offset
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields= '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterpriseUser
        fields= '__all__'

class Scope1emissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope1emissions
        fields= '__all__'

class Scope2emissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope2emissions
        fields= '__all__'

class Scope3emissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scope3emissions
        fields= '__all__'

class offsetSerializer(serializers.ModelSerializer):
    class Meta:
        model = offset
        fields= '__all__'

class roleTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # 添加额外的返回信息
        data['is_Enterprise'] = self.user.is_Enterprise
        return data