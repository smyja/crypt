from django.urls import path
from news.api.views import api_detail

app_name = 'news'

urlpatterns = [
    path('<slug:any>/', api_detail, name='details'),


]