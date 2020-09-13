# from django.shortcuts import render
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .serializer import OfficeFactSerializer
from .models import Office_facts

# Create your views here.


class OfficeFactList(generics.ListCreateAPIView):
    queryset = Office_facts.objects.all()

    serializer_class = OfficeFactSerializer


class OfficeFactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office_facts.objects.all()
    serializer_class = OfficeFactSerializer
