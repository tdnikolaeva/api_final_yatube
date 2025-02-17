from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions,\
    status, viewsets
from rest_framework.exceptions import PermissionDenied,\
    ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from posts.models import Comment, Follow,\
    Group, Post
from .serializers import CommentSerializer,\
    FollowSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'author__username']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        limit = request.query_params.get('limit')
        offset = request.query_params.get('offset')
        if limit is not None and offset is not None:
            try:
                limit = int(limit)
                offset = int(offset)
            except ValueError:
                return Response({
                    "error": "limit и offsetдолжны быть целыми числами."
                },
                    status=400)
            queryset = queryset[offset:offset + limit]
            serializer = self.get_serializer(queryset, many=True)
            return Response({'results': serializer.data})
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения данного действия.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения данного действия.")
        instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'author__username']

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        queryset = Comment.objects.filter(post=post)
        return self.filter_queryset(queryset)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения данного действия.")
        serializer.save()

    def perform_destroy(self, instance):
        comment = self.get_object()
        if comment.author != self.request.user:
            raise PermissionDenied(
                "У вас недостаточно прав для выполнения данного действия.")
        instance.delete()

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        comment_id = self.kwargs.get('pk')
        return get_object_or_404(Comment,
                                 post_id=post_id, pk=comment_id)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username', 'user__username']

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return self.filter_queryset(queryset)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        except Exception:
            raise ValidationError({
                'detail': 'You are already following this user.'
            })

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
