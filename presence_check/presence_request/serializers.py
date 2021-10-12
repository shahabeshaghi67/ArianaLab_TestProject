from .models import PresenceRequest
from rest_framework import serializers


class CreateRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresenceRequest
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'is_approved']
