from django.http import Http404
from requests import HTTPError
from django.shortcuts import render

from .models import Article


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(
        request, 'articles/list.html',
        {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except HTTPError:
        raise Http404("Aricle not found")

    return render(request, 'articles/detail.html', {'article': a})
