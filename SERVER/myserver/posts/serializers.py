from rest_framework import serializers
from posts import models as Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')

#def create(self, validated_data):
#    return Post.objects.create(**validated_data)

#def update(self, instance, validated_data):
#    instance.title = validated_data.get('title', instance.title)
#    instance.body = validated_data.get('body', instance.body)
#    return instance