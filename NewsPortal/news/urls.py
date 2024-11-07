from django.urls import path
from .views import PostsList, PostDetail, NewsCreate

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('articles/create/', NewsCreate.as_view(), name='news/articles_create'),
]