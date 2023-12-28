import random
from django.http import HttpResponse
from articles.models import Article
HTML_STRING = "<h1>HEY YOW sup</h1>"

def home(request):
    random_id = random.randint(1,2)
    article = Article.objects.get(id=random_id)
    h_tag = f"<h1>{article.title}</h1>"
    p_tag = f"<p>{article.content}</p>"
    HTML_STRING = h_tag + p_tag
    return HttpResponse(HTML_STRING)
