from django.urls import path

from backend import views

urlpatterns = [
    path('', views.ProfHome.as_view(), name='home'),
    path('news/', views.ProfNews.as_view(), name='news'),
]