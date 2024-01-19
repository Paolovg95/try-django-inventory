from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def article_detail_view(request, slug=None):
    if slug is not None:
        try:
            article = Article.objects.get(slug=slug)
        except:
            raise Http404
    context = {
        "article": article
    }
    return render(request, "articles/detail.html", context)

@login_required
def article_create_view(request):
    # print(request.POST)
    # {'csrfmiddlewaretoken': ['someCSRFvalue'], 'title': ['another one'], 'content': ['like a dj ']}
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm() # Re-render empty form
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article = Article.objects.create(title=title, content=content)
        # article.save()
        context['article'] = article_object
        # context['created'] = True
    return render(request, "articles/create.html", context=context)

def articles_search_view(request):
    # print(dir(request))
    # dir() Attributes of the class
    # print(request.GET)
    query_dict = request.GET.get("q") # <input type="text" name="q">
    # query_dict is a QueryDict
    # Example : {'q': ['2']}

    # print(query_dict)
    # try:
    #     query = query_dict.get("q") # <input type="text" name="q">
    # except:
    #     query = None
    qs = Article.objects.all()
    if qs is not None:
        lookup = Q(title__icontains=query_dict) | Q(content__icontains=query_dict)
        qs = Article.objects.filter(lookup)
    context = {
        'objects': qs
    }
    return render(request, "articles/search.html", context)
