from rest_framework import serializers
from Institutions.models import Institution

class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields=['institution_name','location','county']


    #check if the organization exists 
    def validate(self,attrs):
        institution_name = attrs.get('institution_name')
        try:
            institution = Institution.objects.get(institution_name = institution_name)
            if institution:
                raise serializers.ValidationError({
                    "institution":"institution already exist. Choose a new name"
                    })
        except Institution.DoesNotExist:
            return attrs
    def create(self,validated_data):
        return Institution.objects.create(**validated_data)