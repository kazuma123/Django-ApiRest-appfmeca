from rest_framework import serializers
from origen.models import Origen


class OrigenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Origen
        fields = '__all__'