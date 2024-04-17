from django.urls import path

from backend import views

urlpatterns = [
    path('', views.main_page_view, name='home'),
]