from rest_framework import serializers
from service.models import ServiceModel

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('id','service', 'version','status' )
        read_only_fields = ( 'status',)
