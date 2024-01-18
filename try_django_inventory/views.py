import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from articles.models import Article


def home(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "home.html", context)
    # template = get_template("home.html")
    # HTML_STRING = render_to_string("home.html", context=context)
    # return HttpResponse(HTML_STRING)
