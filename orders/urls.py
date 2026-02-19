from django.urls import path
from .views import (
    order_list,
    order_create,
    order_edit,
    order_delete,
    order_archive,
    order_status_update,
    picker_orders,
    picker_order_detail,
    order_archive_toggle,
    order_bulk_delete,
)

urlpatterns = [
    path("", order_list, name="orders-list"),
    path("create/", order_create, name="orders-create"),
    path("archive/", order_archive, name="orders-archive"),
    path("bulk-delete/", order_bulk_delete, name="orders-bulk-delete"),
    path("picker/", picker_orders, name="orders-picker"),
    path("picker/<int:pk>/", picker_order_detail, name="orders-picker-detail"),
    path("<int:pk>/status/", order_status_update, name="orders-status"),
    path("<int:pk>/archive-toggle/", order_archive_toggle, name="orders-archive-toggle"),
    path("<int:pk>/edit/", order_edit, name="orders-edit"),
    path("<int:pk>/delete/", order_delete, name="orders-delete"),
]
