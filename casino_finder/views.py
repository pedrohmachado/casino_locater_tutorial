from django.shortcuts import render
from rest_framework import generics
from .serializers import CasinoSerializer
from .models import Casino

# Create your views here.
class ListCreateCasino(generics.ListCreateAPIView):
    queryset = Casino.objects.all()
    serializer_class = CasinoSerializer