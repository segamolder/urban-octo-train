import os

from django.shortcuts import get_object_or_404, render
from django.conf import settings
from .models import Group, Post


def index(request):
    posts = Post.objects.all()[:settings.POSTS_PER_PAGE]

    return render(
        request,
        'posts/index.html',
        {
            'posts': posts,
            'title': 'Последние обновления на сайте'
        }
    )


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    return render(
        request,
        'posts/group_list.html',
        {
            'group': group,
            'posts': group.group_posts.all()[:settings.POSTS_PER_PAGE],
            'title': 'Записи сообщества ' + group.title
        }
    )
