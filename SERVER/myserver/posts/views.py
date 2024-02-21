from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from posts.serializers import PostSerializer
import json
import requests

@api_view(['GET', 'POST'])
def post_list(request, format=None):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("ERROR", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_posts(request, format=None):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response("ERROR", status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def update_post(request, *args, **kwargs):
    if request.method == 'PUT':
        pk = kwargs.get("pk", None)
        if not pk:
            return Response("ERROR", status = status.HTTP_400_BAD_REQUEST)
        
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response("ERROR", status = status.HTTP_400_BAD_REQUEST)
        
        serializer = PostSerializer(data=request.data, instance = instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK) 
        return Response("ERROR", status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pk = kwargs.get("pk", None)
        if not pk:
            return Response("ERROR", status = status.HTTP_400_BAD_REQUEST)
        try:
            instance = Post.objects.get(pk=pk)
        except:
            return Response("ERROR", status = status.HTTP_400_BAD_REQUEST)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_posts(request):
    url = 'https://jsonplaceholder.typicode.com/posts'
    post = requests.get(url)
    response = post.json()
    for request in response:
        serializer = PostSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response("ERROR", status = status.HTTP_400_BAD_REQUEST)