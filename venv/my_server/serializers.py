from .models import MyUser, Entry
from rest_framework import serializers

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'name', 'state', 'email')

class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = '__all__'

