from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="portal-login"),
    path("logout/", views.logout_view, name="portal-logout"),
    path("manager/", views.manager_dashboard, name="portal-manager"),
    path("manager/clients/", views.clients_list, name="portal-clients"),
    path("manager/clients/create/", views.client_create, name="portal-client-create"),
    path("manager/clients/<int:pk>/edit/", views.client_edit, name="portal-client-edit"),
    path("manager/orders/", views.order_list, name="portal-orders"),
    path("manager/orders/create/", views.order_create, name="portal-order-create"),
    path("manager/orders/<int:pk>/edit/", views.order_edit, name="portal-order-edit"),
    path("logistic/", views.logistic_dashboard, name="portal-logistic"),
    path("logistic/delivery/<int:pk>/", views.delivery_plan, name="portal-delivery-plan"),
    path("picker/", views.picker_dashboard, name="portal-picker"),
    path("picker/orders/<int:pk>/status/", views.picker_update_status, name="portal-picker-status"),
    path("admin-panel/", views.sysadmin_dashboard, name="portal-sysadmin"),
]
