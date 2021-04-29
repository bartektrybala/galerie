"""Defines URL patterns for chapters."""

from django.urls import path


from . import views

urlpatterns = [
    path('', views.distance, name='distance'),
    path('ankieta/', views.ankieta, name='ankieta'),
    path('galerie/', views.galerie, name='galerie'),
    path('ranking/', views.ranking, name='ranking'),
    path('galerie/<int:galeria_id>', views.galeria, name='galeria'),
]