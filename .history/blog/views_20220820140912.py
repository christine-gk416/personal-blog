from django.views.generic.list import ListView

from .models import Post

class PostList(ListView):
    model = Post()
    queryset = Post.objects.filter(status=1).order_by('likes')
    template_name = 'templates/index.html'
    paginate_by = 6
