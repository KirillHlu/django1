from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news-home'),  # Добавлено имя для главной страницы
    path('about/', views.about, name='about'),    # Добавлено слэш в конце для согласованности
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail')
]
