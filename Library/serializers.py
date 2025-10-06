from rest_framework import serializers
from Institutions.models import Institution

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields  = '__all__'