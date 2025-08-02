from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    message = MessageSerializer(read_only=True)

    class Meta:
        model = models.Conversation
        fields = ['conversation_id', 'created_at', 'message']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Property
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'

class ReviewSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'