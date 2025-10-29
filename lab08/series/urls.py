# En: series/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # Esta ruta será: /api/
    path('', views.IndexView.as_view(), name='index'), 

    # Esta ruta será: /api/series/
    path('serie/', views.SeriesView.as_view(), name='serie'), 

    # Esta ruta será: /api/series/1/ (por ejemplo)
    path('serie/<int:serie_id>/', views.SerieDetailView.as_view())
]