from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):    
    user_name = serializers.SerializerMethodField()
    
    def get_user_name(self, obj):
        return obj.user.username
        
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('user', 'title', 'content', 'created_at', 'updated_at', 'user_ids',)
        read_only_fields = ('user', 'created_at', 'updated_at',)
        


class CommentSerializer(serializers.ModelSerializer):    
    user_name = serializers.SerializerMethodField()
    
    def get_user_name(self, obj):
        return obj.user.username
    class Meta:
        model = Comment
        # fields = ('article', 'user', 'content', 'created_at', 'updated_at',)
        fields = '__all__'
        read_only_fields = ('user', 'article', 'created_at', 'updated_at',)
