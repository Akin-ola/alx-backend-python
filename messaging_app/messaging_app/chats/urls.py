from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth.views import LoginView

router = DefaultRouter()
router.register(r'conversations', views.ConversationViewSet, basename='conversation')
router.register(r'messages', views.MessageViewSet, basename='message')
router.register(r'users', views.UserViewSet, basename= 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view(), name='login')
]
