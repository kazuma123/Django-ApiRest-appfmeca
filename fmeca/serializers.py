from rest_framework import serializers
from fmeca.models import FMeca
from fmeca.models import MaquinaFmeca


class FmecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = FMeca
        fields = '__all__'


class MaquinaFmecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaquinaFmeca
        fields = '__all__'