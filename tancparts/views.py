from django.shortcuts import render
from .serializers import PanzerModelSerializer, AbramsModelSerializer
from .models import Panzer, Abrams
from rest_framework import generics

class PanzerListAPIView(generics.ListAPIView):
    serializer_class = PanzerModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Panzer.objects.all()
        return qs


class AbramsListAPIView(generics.ListAPIView):
    serializer_class = AbramsModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Abrams.objects.all()
        return qs

