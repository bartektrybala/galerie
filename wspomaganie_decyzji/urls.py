"""Defines URL patterns for chapters."""

from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('galerie/', views.galerie, name='galerie'),
    path('galerie/<int:galeria_id>', views.galeria, name='galeria'),
]