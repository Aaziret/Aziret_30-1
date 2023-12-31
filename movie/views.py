from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movie import models, serializers


@api_view(['GET'])
def directors_list_api_view(request):
    directors = models.Director.objects.all()
    serializer = serializers.DirectorSerializer(directors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movies_list_api_view(request):
    movies = models.Movie.objects.all()
    serializer = serializers.MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = models.Review.objects.all()
    serializer = serializers.ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def director_detail_api_view(request, pk):
    try:
        director = models.Director.objects.get(id=pk)
    except models.Director.DoesNotExist:
        return Response({'error': 'Director object does not found'}, status=404)
    serializer = serializers.DirectorSerializer(director)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail_api_view(request, pk):
    try:
        movie = models.Movie.objects.get(id=pk)
    except models.Movie.DoesNotExist:
        return Response({'error': 'Movie object does not found'}, status=404)
    serializer = serializers.MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_detail_api_view(request, pk):
    try:
        review = models.Review.objects.get(id=pk)
    except models.Review.DoesNotExist:
        return Response({'error': 'Review object does not found'}, status=404)
    serializer = serializers.ReviewSerializer(review)
    return Response(serializer.data)