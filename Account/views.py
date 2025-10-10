from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response


class CustomTokenSerializerPair(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.first_name

        return token 
class CustomTokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenSerializerPair
    # override the post method here 
    def post(self,request,*args,**kwargs):
        response = super().post(request,*args,**kwargs)
        tokens = response.data
        return Response({"tokens":tokens},status=status.HTTP_200_OK)