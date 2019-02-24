from django.shortcuts import render
from .models import MyUser, Entry
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import viewsets

class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()