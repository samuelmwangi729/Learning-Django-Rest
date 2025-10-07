from .serializers import BookSerializer,AuthorSerializer
from rest_framework.generics import GenericAPIView,ListAPIView
from rest_framework import status,response
from rest_framework.views import APIView
from Library.models import Books,Author
class BookListApiView(APIView):
    serializer_class = BookSerializer

    def get(self,request):
        queryset = Books.objects.all()
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
class AuthorsListView(ListAPIView):
    serializer_class = AuthorSerializer

    def get(self,request):
        queryset = Author.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return response.Response({
            "status":"success",
            "message":"completed the fetching",
            "data":serializer.data
            },status=status.HTTP_200_OK)
    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                "status":"success",
                "message":"successfully created the author",
                "data":serializer.data
                },status=status.HTTP_201_CREATED)
        return response.Response({
                "status":"success",
                "message":serializer.errors,
            },status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,username=None):
        #get the author 
        try:
            author = Author.objects.get(name=username)
        except Author.DoesNotExist:
            return response.Response({
                "status":"error",
                "message":"author not found",
            },status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(author,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                "status":"success",
                "message":"successfully created the author",
                "data":serializer.data
                },status=status.HTTP_201_CREATED)
        return response.Response({
                "status":"success",
                "message":serializer.errors,
            },status=status.HTTP_400_BAD_REQUEST)