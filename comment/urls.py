from django.urls import path
from comment import views


urlpatterns = [
    # http://127.0.0.1:8000/comment/post
    path('post', views.post_comment)
]