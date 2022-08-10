from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'name', 'message',)
        read_only_fields = ('id',)