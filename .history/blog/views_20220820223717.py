from django.views.generic.list import ListView

from .models import Post

class PostList(ListView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'blog/post-list.html'
    paginate_by = 6
