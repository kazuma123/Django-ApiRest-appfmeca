from rest_framework import serializers
from falla.models import Falla
#from falla.models import MaquinaFmeca


class FmecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Falla
        fields = '__all__'

