from django.urls import path
from .views import PostListView, LandingView
from .decorators import authenticated_user_redirect

urlpatterns = [
    path('', authenticated_user_redirect(LandingView.as_view()), name='landing'),
    path('social/', PostListView.as_view(), name='post-list'),

]
