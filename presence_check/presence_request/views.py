from django.shortcuts import render
from django.views.generic.base import View
from rest_framework import generics

from presence_request.models import PresenceRequest

from .serializers import CreateRequestSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from presence_check import settings


class ApproveRequestView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        request_pk = kwargs.get('request_pk')
        presence_request = generics.get_object_or_404(PresenceRequest,
                                                      pk=request_pk)
        presence_request.approve()
        return redirect(presence_request)


class RefuseRequestView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        request_pk = kwargs.get('request_pk')
        presence_request = generics.get_object_or_404(PresenceRequest,
                                                      pk=request_pk)
        presence_request.refuse()
        return redirect(presence_request)


class CreateRequestView(generics.CreateAPIView):
    serializer_class = CreateRequestSerializer
    queryset = PresenceRequest.objects.all()
