from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from apps.social.models import Post


# Create your views here.
# class LandingView(View):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             user = get_object_or_404(User, id=request.user.id)
#             context = {
#                 'user': user
#             }
#             return render(request, 'social/post_list.html', context)
#         else:
#             return render(request, 'landing.html')


class PostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')

        context = {
            'post_list': posts,

        }

        return render(request, 'social/post_list.html', context)
