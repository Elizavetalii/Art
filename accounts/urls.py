from django.urls import path
from .views import login_view, logout_view, dashboard_root

urlpatterns = [
    path("", login_view, name="root-login"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_root, name="dashboard-root"),
]
