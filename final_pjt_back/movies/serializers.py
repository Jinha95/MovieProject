from rest_framework import serializers
from .models import Movie, Genre, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)


class MovieSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('id', 'popularity', 'vote_count', 'vote_average', 'release_date', 'title', 'overview', 'poster_path', 'genre_ids',)

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    
    def get_user_name(self, obj):
        return obj.user.username
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'created_at', 'updated_at',)

