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
        read_only_fields = ['message_id', 'sender_id', 'sent_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['sender_id'] = user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('conversation_id', None)
        return super().update(instance, validated_data)

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = models.Conversation
        fields = ['conversation_id', 'participants_id', 'created_at', 'messages']


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