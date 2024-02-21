from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(default=0)
    title = serializers.CharField(max_length=200)
    body = serializers.CharField(max_length=200)
    
    class Meta:
        model = Post
        fields = ('userId','id', 'title', 'body')


    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.userId = validated_data.get('userId', instance.userId) 
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance