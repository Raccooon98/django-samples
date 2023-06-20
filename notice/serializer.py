from .models import notice
from rest_framework import serializers

class noticeSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    def get_date(self,obj):
        return obj.date.strftime('%Y-%m-%d')
    class Meta:
        model=notice
        fields='__all__'
