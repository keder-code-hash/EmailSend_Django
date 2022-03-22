from rest_framework import serializers
from .models import EmailStore

class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailStore 
        fields = ['username', 'send_to']