from django.contrib import admin
from chats.models import Conversation, Message, User

# Register your models here.
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    ...

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    ...

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ...