from rest_framework import serializers
from .models import Log


class ReadSerializer(serializers.ModelSerializer):
    """Currency request serializer"""

    _from = serializers.CharField(required=True, label='From')
    to = serializers.CharField(required=True, label='To')
    # q = serializers.IntegerField(min_value=1, max_value=5, required=True, label='Quote')
    ans = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Log
        fields = ['_from', 'to', 'ans', 'created_at']