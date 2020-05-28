from news.models import Headline, UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untt.settings")
django.setup()

import math
import requests
import urllib3
import textwrap

from bs4 import BeautifulSoup
from datetime import timedelta, timezone, datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    req = requests.get("https://dailypost.ng/hot-news/page/")
except requests.exceptions.ConnectionError:
    print("Connection refused")



def home(request):


    headlines_list = Headline.objects.all().order_by('-id')
    paginator = Paginator(headlines_list, 10)
    page = request.GET.get('page')
    try:
        headlines = paginator.page(page)
    except PageNotAnInteger:
        headlines = paginator.page(1)
    except EmptyPage:
        headlines = paginator.page(paginator.num_pages)

    context = {
        'object_list': headlines,

    }

    return render(request, "home.html", context)


def details(request, any):
    qs = Headline.objects.get(slug=any)
    return render(request, 'detail.html', {'qs': qs})



def scrape(request):
    headlines = list()
    articles = list()

    user_p = UserProfile.objects.filter(user=request.user).first()

    user_p.last_scrape = datetime.now(timezone.utc)
    user_p.save()
    for i in range(1):
        r = requests.get("https://dailypost.ng/hot-news/page/{}".format(i))
        soup = BeautifulSoup(r.content, "html.parser")
        mydivs = soup.findAll("span", {"class": "mvp-cd-date left relative"})
    for div in mydivs:
        mytags = div.findNext('h2')
        for tag in mytags:
            headlines.append(tag.strip())

    z = [linkk.get('href', '/') for linkk in soup.find_all("a", {"rel": "bookmark"})]
    for url in z:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        conteent = soup.find(id="mvp-content-main")
        article = ''
        line_size = 80

        for i in conteent.findAll('p'):
            w = textwrap.TextWrapper(width=line_size, break_long_words=False, replace_whitespace=False)
            body = '\n'.join(w.wrap(i.text))
            article += body + "\n\n"
        articles.append(article)

    for i in range(len(headlines)):
        news_headline = Headline()
        news_headline.title = headlines[i]
        news_headline.contentt = articles[i]
        news_headline.save()

    return redirect('/')

@login_required
def artnews(request):
    user_p = UserProfile.objects.get(user=request.user)
    now = datetime.now(timezone.utc)
    time_difference = now - user_p.last_scrape
    time_difference_in_hours = time_difference / timedelta(minutes=60)
    next_scrape = 24 - time_difference_in_hours
    if time_difference_in_hours <= 24:
        hide_me = True
    else:
        hide_me = False

    context = {
        'hide_me': hide_me,
    'next_scrape': math.ceil(next_scrape)

    }
    return render(request, "articlenews.html", context)

# Create your views here.
