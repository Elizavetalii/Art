from django.shortcuts import redirect
from functools import wraps


def role_required(role_name: str):
    """
    Decorator to ensure user has role_name (case-insensitive).
    Expects user model with many-to-many to Role via roles.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect("/login/")
            if not user.roles.filter(name__iexact=role_name).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator


def roles_required(role_names):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect("/login/")
            if not user.roles.filter(name__in=role_names).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
