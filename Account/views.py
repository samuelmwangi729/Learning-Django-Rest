from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status


class CustomTokenSerializerPair(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.first_name

        return token 
class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenSerializerPair