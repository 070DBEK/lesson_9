from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie


def home(request):
    return render(request, 'index.html')


def movie_list(request):
    movies = Movie.objects.all()
    ctx = {'movies': movies}
    return render(request, 'movies/list.html', ctx)


def create_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        director = request.POST.get('director')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        if name and director and year and genre:
            Movie.objects.create(
                name=name,
                director=director,
                year=year,
                genre=genre,
            )
            return redirect('movies:list')
    return render(request, 'movies/form.html')


def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "POST":
        name = request.POST.get('name')
        director = request.POST.get('director')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        if name and director and year and genre:
            movie.name = name
            movie.director = director
            movie.year = year
            movie.genre = genre
            movie.save()
            return redirect(movie.get_detail_url())
    ctx = {'movie': movie}
    return render(request, 'movies/form.html', ctx)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    ctx = {'movie': movie}
    return render(request, 'movies/detail.html', ctx)


def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return redirect('movies:list')
