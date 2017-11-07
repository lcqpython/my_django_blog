from django.http import HttpResponse
from .models import Article
from datetime import datetime
from django.template.loader import get_template
from django.shortcuts import redirect


# Create your views here.
def homepage(request):
    template = get_template('index.html')
    articles = Article.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
    # post_lists = list()
    # for count, article in enumerate(articles):
    #     post_lists.append("No.{}:".format(str(count)) + str(article) + "<br>")
    #     post_lists.append("<small>" + str(article.content)+"</small><br>")
    # return HttpResponse(post_lists)


def show_article(request, category):
    template = get_template('post.html')
    try:
        article = Article.objects.get(category=category)
        if article:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')