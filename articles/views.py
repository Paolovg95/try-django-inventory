from django.shortcuts import render
from .models import Article
# Create your views here.
def article_detail_view(request, id=None):
    if id is not None:
        article = Article.objects.get(id=id)

    context = {
        "article": article
    }
    return render(request, "articles/detail.html", context)
def article_create_view(request):
    context = {
    }
    return render(request, "articles/create.html", context)

def articles_search_view(request):
    # print(dir(request))
    # dir() Attributes of the class
    # print(request.GET)
    query_dict = request.GET #query_dict is a dictionary
    # query = query_dict.get("q") # <input type="text" name="q">
    try:
        query = int(query_dict.get("q"))
    except:
        query = None
    if query is not None:
        try:
            article = Article.objects.get(id=query)
        except:
            article = None
    else:
        article = None
    context = {
        'object': article
    }
    return render(request, "articles/search.html", context)
