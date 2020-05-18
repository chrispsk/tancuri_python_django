from rest_framework import serializers
from .models import Panzer, Abrams


class PanzerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panzer
        fields = [
            'tureta',
            'engine',
            'tracks',
            'front',
            'health',
        ]

class AbramsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abrams
        fields = [
            'tureta',
            'engine',
            'tracks',
            'front',
            'health',
        ]

