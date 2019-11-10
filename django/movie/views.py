from django.shortcuts import render, get_object_or_404
from .models import Movie, Genre, MovieGenre

def index(request):
    return render(request, 'index.html')

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie': movie})