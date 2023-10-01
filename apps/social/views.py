from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from apps.social.models import Post


# Create your views here.
class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')

        context = {
            'post_list': posts,
        }

        return render(request, 'social/post_list.html', context)
