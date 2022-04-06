from django.shortcuts import render
from rest_framework import generics
from .models import Newton
from .serializers import NewtonSerializer

# Create your views here.

class ListNewton(generics.ListAPIView):
    queryset=Newton.objects.all()
    serializer_class = NewtonSerializer
class DetailedNewton(generics.RetrieveAPIView):
    queryset = Newton.objects.all()
    serializer_class = NewtonSerializer

