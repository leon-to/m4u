from django.shortcuts import render
from movie.models import Movie

# Create your views here.
def search(request):
    query = request.GET.get('q')
    
    print(query)

    if query is None:
        return render(request, 'search.html')
    else:
        movies = Movie.objects.filter(title__contains=query)
        print(movies)
        return render(request, 'search_result.html', {'movies': movies})
