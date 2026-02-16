from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages


def _role_redirect(user):
    if user.roles.filter(name__iexact="Менеджер").exists():
        return "/dashboard/manager/"
    if user.roles.filter(name__iexact="Логист").exists():
        return "/dashboard/logistic/"
    if user.roles.filter(name__iexact="Сборщик заказов").exists():
        return "/dashboard/picker/"
    if user.roles.filter(name__iexact="Курьер").exists():
        return "/logistics/courier/routes/"
    if user.roles.filter(name__iexact="Администратор системы").exists():
        return "/dashboard/admin/"
    return None


def login_view(request):
    if request.user.is_authenticated:
        target = _role_redirect(request.user)
        if target:
            return redirect(target)
        logout(request)
        messages.error(request, "У вашего аккаунта нет роли. Войдите под другой учётной записью.")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = None
        if "@" in username:
            User = get_user_model()
            candidate = User.objects.filter(email__iexact=username).first()
            if candidate:
                user = authenticate(request, username=candidate.username, password=password)
        else:
            user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Неверный логин или пароль.")
        else:
            login(request, user)
            target = _role_redirect(user)
            if target:
                return redirect(target)
            logout(request)
            messages.error(request, "Нет прав доступа. У пользователя не назначена роль.")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


def dashboard_root(request):
    # редирект на соответствующую роль
    if not request.user.is_authenticated:
        return redirect("/login/")
    target = _role_redirect(request.user)
    if target:
        return redirect(target)
    logout(request)
    messages.error(request, "Нет прав доступа. У пользователя не назначена роль.")
    return redirect("/login/")

# Create your views here.
