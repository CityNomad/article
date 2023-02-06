from rest_framework import serializers
from webapp.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['tags']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'article', 'author', 'created_at', 'updated_at', 'favourite']
        read_only_fields = ['favourite', 'author']
