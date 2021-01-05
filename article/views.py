from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from .models import Article,Comment
def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request,'articles/list.html',{'latest_articles_list':latest_articles_list})
def details(request, article_id):
    try :
        a = Article.objects.get(pk = article_id)
        latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    except:
        raise Http404("Not Found")
    return render(request,'articles/detail.html',{'articles':a,'latest_articles_list':latest_articles_list})    
