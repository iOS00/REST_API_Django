from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta: #define which fields json should include
        model = Drink
        fields = ['id', 'name', 'description']