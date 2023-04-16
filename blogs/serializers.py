from rest_framework import serializers, viewsets 
from blogs.models import Blog
 
class BlogSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=70)
    description = serializers.CharField(max_length=200, style={'base_template': 'textarea.html'})
    published = serializers.BooleanField()
    
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)
    
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'published')
        
# ViewSets define the view behavior.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer