from django.shortcuts import render
from django.views.generic import ListView

from backend.models import News
from backend.utils import DataMixin


def main_page_view(request):
    return render(request, 'backend/index.html')


def news_page(request):
    return render(request, 'backend/news.html')


class ProfHome(DataMixin, ListView):
    template_name = "backend/index.html"
    context_object_name = 'news'
    title_page = 'Сервисы Профсоюзной организации'
    selected_cat = 0

    def get_queryset(self):
        return News.objects.all()[:3]


class ProfNews(DataMixin, ListView):
    template_name = "backend/news.html"
    context_object_name = 'news'
    title_page = 'Сервисы Профсоюзной организации | Новости'
    selected_cat = 0

    def get_queryset(self):
        return News.objects.all()


