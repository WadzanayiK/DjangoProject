from rest_framework import serializers
from .models import Artiste,Lyric,Song

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ["first_name", "last_name", "age"]

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ["content", "song_id"]

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["artiste_id", "title", "release_date", "likes"]