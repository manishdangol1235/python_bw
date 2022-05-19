from django.urls import path
from news import views

urlpatterns = [
    # http://127.0.0.1:8000/news/
    path('', views.show_news),

    # http://127.0.0.1:8000/news/category/3
    path('category/<cid>', views.show_news_by_category),

    # http://127.0.0.1:8000/news/single/2
    path('single/<nid>', views.show_single_news),

    # http://127.0.0.1:8000/news/searched/election
]
