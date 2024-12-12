from django.urls import path
from . import views


app_name = 'sports'


urlpatterns = [
    path('list/', views.sport_list, name='sport_list'),
    path('create/', views.create_sport, name='create_sport'),
    path('update/<int:sport_id>/', views.update_sport, name='update_sport'),
    path('detail/<int:sport_id>/', views.sport_detail, name='sport_detail'),
    path('delete/<int:sport_id>/', views.sport_delete, name='sport_delete'),
]
