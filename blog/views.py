from django.shortcuts import render, get_object_or_404
from blog.models import Article


# Create your views here.

def all_article(request):
    article = Article.objects.order_by('-date')
    return render(request, 'blog/home blog.html', {'blogs': article})


def detail(request, blog_id):
    article = get_object_or_404(Article, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': article})
