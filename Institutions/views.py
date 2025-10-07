from django.shortcuts import render
from rest_framework.views import APIView
from Institutions.models import Institution
from Institutions.serializers import InstitutionSerializer
from rest_framework import status,response
class InstitutionApiView(APIView):
    serializer_class = InstitutionSerializer

    def get(self,request):
        queryset = Institution.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return response.Response({
            "status":"success",
            "message":"successfully fetched the data",
            "data":serializer.data
            },status=status.HTTP_200_OK)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                "status":"success",
                "message":"successfully fetched the data",
                "data":serializer.data
                },status=status.HTTP_200_OK)
        return response.Response({
            "status":"error",
            "message":serializer.errors
            },status=status.HTTP_200_OK)
            