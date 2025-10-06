from Institutions.models import Institution
from .serializers import BookSerializer
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework import status,response
from rest_framework.views import APIView
class BookListApiView(APIView):
    serializer_class = BookSerializer

    def get(self,request):
        queryset = Institution.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return response.Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                "status":"success",
                "message":"institution successfully created",
                "data":serializer.data
            },status=status.HTTP_201_CREATED)
        return response.Response({
                "status":"error",
                "message":serializer.errors
            },status=status.HTTP_201_CREATED)