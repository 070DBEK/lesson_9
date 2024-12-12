from django.shortcuts import render, redirect, get_object_or_404
from .models import Music


def music_list(request):
    musics = Music.objects.all()
    ctx = {'musics': musics}
    return render(request, 'musics/list.html', ctx)


def create_music(request):
    if request.method == "POST":
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        date = request.POST.get('date')
        genre = request.POST.get('genre')
        if album_title and artist and date and genre:
            Music.objects.create(
                album_title=album_title,
                artist=artist,
                date=date,
                genre=genre,
            )
            return redirect('musics:music_list')
    return render(request, 'musics/form.html')


def update_music(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        artist = request.POST.get('artist')
        date = request.POST.get('date')
        genre = request.POST.get('genre')
        if album_title and artist and date and genre:
            music.album_title = album_title
            music.artist = artist
            music.date = date
            music.genre = genre
            music.save()
            return redirect(music.get_detail_url())
    ctx = {'music': music}
    return render(request, 'musics/form.html', ctx)

def music_detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    ctx = {'music': music}
    return render(request, 'musics/detail.html', ctx)


def music_delete(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    music.delete()
    return redirect('musics:music_list')
