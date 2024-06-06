from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from posts.models import Post
from accounts.models import User
from apis.serialziers import PostSerializer, CreateUserSerializer, OtpRequestSerializer \
    ,ProfileSerializer, CreatePostSerializer, RetrievePostSerializer


class CreateUserAPIView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class OtpRequestView(APIView):
    def post(self, request):
        ser_data = OtpRequestSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_published=True)


class ProfileApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()


class CreatePostAPIView(CreateAPIView):
    serializer_class = CreatePostSerializer
    queryset = Post.objects.all()


class RetrievePostAPIView(RetrieveAPIView):
    serializer_class = RetrievePostSerializer
    queryset = Post.objects.filter(is_published=True)