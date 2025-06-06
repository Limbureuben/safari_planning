from rest_framework import serializers # type: ignore
from .models import *

class RegisterOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRegistration
        fields = '__all__'

class BookingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingPackage
        fields = '__all__'