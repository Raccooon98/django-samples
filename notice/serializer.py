from .models import notice
from rest_framework import serializers

class noticeSerializer(serializers.ModelSerializer):
    class Meta:
        model=notice
        fields='__all__'
