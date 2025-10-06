from django.urls import path 
from Library.views import BookListApiView

urlpatterns=[
    path('books',BookListApiView.as_view(),name="books")
]