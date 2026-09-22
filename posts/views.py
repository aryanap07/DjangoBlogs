from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Post


def index(request):
    paginator = Paginator(Post.objects.all(), 5)
    page_obj = paginator.get_page(request.GET.get('page'))
    return render(request, 'index.html', {'page_obj': page_obj})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts.html', {'post': post})
