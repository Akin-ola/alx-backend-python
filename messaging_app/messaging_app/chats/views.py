from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from . import serializers
from . import models

# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = models.Conversation.objects.all()
    serializer_class = serializers.ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset= models.User.objects.all()
    serializer_class= serializers.UserSerializer