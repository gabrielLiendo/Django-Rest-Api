from models import Blog
from rest_framework import viewsets
from rest_framework import permissions
from blogs.serializers import BlogSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]