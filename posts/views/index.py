
from django.views.generic import ListView

from posts.models import Post


class IndexView(ListView):
    template_name = 'index.html'
    model = Post
    context_object_name = 'post'
    ordering = ('-created_at',)
    queryset = Post.objects.all()
    paginate_by = 2
    allow_empty = True