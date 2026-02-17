from django.contrib.auth import get_user_model
from .models import Post
from rest_framework import viewsets #new
from rest_framework.permissions import IsAdminUser #new
from .permissions import IsAuthorOrReadOnly 
from .serializers import PostSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)# new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


