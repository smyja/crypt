"""untt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from news import views
from news.views import scrape, home, artnews, news, asyncnews,slownews
app_name = 'index'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scrape/', scrape, name='scrape'),
    path('', home),
    path('news/', news, name='news'),
    path('asyncnews/', asyncnews, name='asyncnews'),
    path('slownews/', asyncnews, name='slownews'),
    path('details/<slug:any>/', views.details, name='details'),
    path('articlenews/', artnews, name='artnews'),

    #REST FRAMEWORRK URL
    path('api/', include('news.api.urls', 'news_api')),



]
