from django.shortcuts import render
from django.http import Http404


from .models import Article
# Create your views here.

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {
        'latest_article_list': latest_article_list,
    }
    return render(request,'blog/index.html',context)

def detail(request,article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/detail.html', {'article': article})