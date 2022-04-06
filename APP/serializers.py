from rest_framework import serializers
from .models import Newton


class NewtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newton
        fields = ('id', 'title', 'body')
        