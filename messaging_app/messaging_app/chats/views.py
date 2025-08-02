from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models

# Create your views here.
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = models.Conversation.objects.all()
    serializer_class = serializers.ConversationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
