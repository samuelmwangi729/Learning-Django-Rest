from django.urls import path 
from Library.views import BookListApiView,AuthorsListView

urlpatterns=[
    path('books',BookListApiView.as_view(),name="books"),
    path('authors',AuthorsListView.as_view(),name="authors"),
    path('author/<str:username>',AuthorsListView.as_view(),name="author-update"),
]