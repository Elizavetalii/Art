from django.urls import path
from .views import client_list, client_create, client_edit, client_delete, client_detail

urlpatterns = [
    path("", client_list, name="clients-list"),
    path("create/", client_create, name="clients-create"),
    path("<int:pk>/", client_detail, name="clients-detail"),
    path("<int:pk>/edit/", client_edit, name="clients-edit"),
    path("<int:pk>/delete/", client_delete, name="clients-delete"),
]
