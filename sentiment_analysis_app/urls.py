from django.urls import path
from . import views

urlpatterns = [
  path('sentiment/', views.sentiment_analysis_view, name='sentiment_analysis'),
  path('sentiment_fin/', views.sentiment_analysis_fin_view, name='sentiment_analysis_fin')
]
