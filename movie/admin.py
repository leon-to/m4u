from django.contrib import admin
from .models import Movie, Genre, MovieGenre

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release']

    search_fields = ['title', 'description']

    list_filter = ['release']

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(MovieGenre)