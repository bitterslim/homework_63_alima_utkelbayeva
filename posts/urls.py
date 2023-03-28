from django.urls import path

from posts.views.index import IndexView
from posts.views.post_views import PostCreateView, PostDetailView, CommentCreateView, like_post, SubscribeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("posts/add", PostCreateView.as_view(), name="add_post"),
    path("detail/<int:pk>", PostDetailView.as_view(), name='post_detail'),
    path("detail/<int:pk>/comment/add/", CommentCreateView.as_view(), name="comment_add"),
    path("detail/<int:post_id>", like_post, name="like_add"),
    path('detail/<int:pk>/subs/', SubscribeView.as_view(), name='subscribe'),
]