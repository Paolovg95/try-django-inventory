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
    # print(request.POST)
    # {'csrfmiddlewaretoken': ['someCSRFvalue'], 'title': ['another one'], 'content': ['like a dj ']}
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content)
        article.save()
        context['article'] = article
        context['created'] = True
    return render(request, "articles/create.html", context=context)

def articles_search_view(request):
    # print(dir(request))
    # dir() Attributes of the class
    # print(request.GET)

    query_dict = request.GET # query_dict is a QueryDict
    # Example : {'q': ['2']}

    # print(query_dict)
    try:
        query = int(query_dict.get("q")) # <input type="text" name="q">
        article = Article.objects.get(id=query)
    except:
        article = None
    context = {
        'object': article
    }
    return render(request, "articles/search.html", context)
