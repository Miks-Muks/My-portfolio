from django.urls import path
from .views import all_article, detail

urlpatterns = [
    path('', all_article, name='all_blogs'),
    path('<int:blog_id>/', detail, name='detail'),
]