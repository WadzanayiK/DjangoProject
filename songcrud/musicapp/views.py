from django.shortcuts import render
from django.shortcuts import get_object_or_404   
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status  
from .models import Artiste 
from .models import Song
from .models import Lyric
from .serializers import ArtisteSerializer
from .serializers import SongSerializer
from .serializers import LyricSerializer
  
 
  
class ArtisteView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Artiste.objects.all()  
        serializers = ArtisteSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = ArtisteSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):  
        result = Artiste.objects.get(id=id)  
        serializer = ArtisteSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors}) 
    
    def delete(self, request, id=None):  
        result = get_object_or_404(Artiste, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})
         


class LyricView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Lyric.objects.all()  
        serializers = LyricSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = LyricSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):  
        result = Lyric.objects.get(id=id)  
        serializer = LyricSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})
    
    def delete(self, request, id=None):  
        result = get_object_or_404(Lyric, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})



class SongView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Song.objects.all()  
        serializers = SongSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = SongSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):  
        result = Song.objects.get(id=id)  
        serializer = SongSerializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})  
    
    def delete(self, request, id=None):  
        result = get_object_or_404(Song, id=id)  
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})
