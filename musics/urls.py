from django.urls import path
from . import views


app_name = 'musics'


urlpatterns = [
    path('list/', views.music_list, name='music_list'),
    path('create/', views.create_music, name='create_music'),
    path('update/<int:music_id>/', views.update_music, name='update_music'),
    path('detail/<int:music_id>/', views.music_detail, name='music_detail'),
    path('delete/<int:music_id>/', views.music_delete, name='music_delete'),
]
