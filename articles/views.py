from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404, HttpResponse
from .models import Article
from .forms import ArticleForm
from django.urls import reverse

# Create your views here.
def article_detail_view(request, slug=None):
    hx_url = reverse("articles:hx-detail", kwargs={"slug": slug})
    obj = Article.objects.get(slug=slug)
    context = {
        "hx_url": hx_url,
        "obj": obj
    }
    return render(request, "articles/detail.html", context)

def article_hx_detail_view(request, slug=None):
    if not request.htmx:
        raise Http404
    try:
        obj = Article.objects.get(slug=slug)
    except:
        obj = None
    if obj is  None:
        return HttpResponse("Not found.")
    context = {
        "object": obj
    }
    return render(request, "articles/partials/detail.html", context)

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
    qs = Article.objects.search(query_dict)
        # lookup = Q(title__icontains=query_dict) | Q(content__icontains=query_dict)
        # qs = Article.objects.filter(lookup)
    context = {
        'objects': qs
    }
    return render(request, "articles/search.html", context)
