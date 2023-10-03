from django.shortcuts import redirect


def authenticated_user_redirect(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('post-list')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func