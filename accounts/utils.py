from functools import wraps
from django.shortcuts import redirect


def role_required(role_name: str):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("/login/")
            if not request.user.roles.filter(name__iexact=role_name).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator


def roles_required(role_names):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("/login/")
            if not request.user.roles.filter(name__in=role_names).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
