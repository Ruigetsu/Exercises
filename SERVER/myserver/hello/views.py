from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from models import Post 
from hello.serializers import PostSerializer

@api_view(['GET', 'POST'])
def posts(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)
    
    #elif request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)