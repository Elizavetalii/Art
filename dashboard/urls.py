from django.urls import path
from .views import manager_dashboard, logistic_dashboard, picker_dashboard, admin_dashboard

urlpatterns = [
    path("manager/", manager_dashboard, name="manager"),
    path("logistic/", logistic_dashboard, name="logistic"),
    path("picker/", picker_dashboard, name="picker"),
    path("admin/", admin_dashboard, name="admin"),
]
