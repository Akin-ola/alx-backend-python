from django.contrib import admin
from chats.models import Conversation, Message

# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    ...

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    ...