from django.urls import path 
from Institutions.views import InstitutionApiView
urlpatterns = [
   path("institutions",InstitutionApiView.as_view(),name="institutions")
]
