from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
from django.template.loader import get_template


# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Article.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)