from django.urls import path
from news.api.views import *

app_name = 'news'

urlpatterns = [
    path('<slug:any>/', api_detail, name='details'),
    path('', api_head, name='api_head'),


]