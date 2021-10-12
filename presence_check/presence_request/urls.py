
from os import name
from django.urls import path

from .views import ApproveRequestView, RefuseRequestView, CreateRequestView


urlpatterns = [
    path('approve/<str:request_pk>/', ApproveRequestView.as_view(), name='approve-request'),
    path('refuse/<str:request_pk>/', RefuseRequestView.as_view(), name='refuse-request'),
    path('request/', CreateRequestView.as_view(), name='create-request'),
]