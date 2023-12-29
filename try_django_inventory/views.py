import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

HTML_STRING = "<h1>HEY YOW sup</h1>"

def home(request):
    random_id = random.randint(1,2)
    article = Article.objects.get(id=random_id)
    articles = Article.objects.all()
    context = {
        "articles": articles,
        "object": article,
        "id": article.id,
        "title": article.title,
        "content": article.content
    }
    # template = get_template("home.html")
    HTML_STRING = render_to_string("home.html", context=context)
    return HttpResponse(HTML_STRING)
