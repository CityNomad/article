from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_v2.serializers import ArticleSerializer, CommentSerializer
from webapp.models import Article, Comment


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            article = get_object_or_404(Article, pk=pk)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        Article.delete(article)
        return Response({"pk": pk}, status=status.HTTP_204_NO_CONTENT)


class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            comment = get_object_or_404(Comment, pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def put(self, request, *args, pk, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, *args, pk, **kwargs):
        comment = get_object_or_404(Comment, pk=pk)
        Comment.delete(comment)
        return Response({"pk": pk}, status=status.HTTP_204_NO_CONTENT)






