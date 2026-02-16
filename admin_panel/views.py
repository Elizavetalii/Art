import os
import shutil
from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator
from django.db import models as dj_models
from django.db.models import Q
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from accounts.utils import role_required
from crm.models import Role, Client, Order, Delivery
from .models import Backup, BackupSchedule
from .forms import UserCreateForm, UserUpdateForm, UserPasswordForm, RoleForm, BackupScheduleForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .entity_config import ENTITIES, EntityConfig
from crm.forms import BootstrapFormMixin

User = get_user_model()


@role_required("Администратор системы")
def admin_index(request):
    stats = {
        "users": User.objects.count(),
        "roles": Role.objects.count(),
        "backups": Backup.objects.count(),
    }
    entities = []
    for entity in ENTITIES:
        try:
            count = entity.model.objects.count()
        except Exception:
            count = 0
        entities.append({"slug": entity.slug, "label": entity.label, "count": count})
    return render(request, "admin_panel/index.html", {"stats": stats, "entities": entities})


@role_required("Администратор системы")
def users_list(request):
    qs = User.objects.all()
    return render(request, "admin_panel/users_list.html", {"users": qs})


@role_required("Администратор системы")
def user_create(request):
    form = UserCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        roles = form.cleaned_data.pop("roles")
        password = form.cleaned_data.pop("password")
        user = User.objects.create(**form.cleaned_data)
        user.set_password(password)
        user.save()
        user.roles.set(roles)
        messages.success(request, "Пользователь создан.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_form.html", {"form": form, "title": "Создать пользователя"})


@role_required("Администратор системы")
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserUpdateForm(request.POST or None, instance=user, initial={"roles": user.roles.all()})
    if request.method == "POST" and form.is_valid():
        roles = form.cleaned_data.pop("roles")
        form.save()
        user.roles.set(roles)
        messages.success(request, "Пользователь обновлён.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_form.html", {"form": form, "title": "Редактировать пользователя"})


@role_required("Администратор системы")
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        messages.success(request, "Пользователь удалён.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_delete.html", {"object": user})


@role_required("Администратор системы")
def user_toggle_active(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.is_active = not user.is_active
        user.save(update_fields=["is_active"])
        messages.success(request, "Статус пользователя обновлён.")
    return redirect("/admin-panel/users/")


@role_required("Администратор системы")
def user_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserPasswordForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user.set_password(form.cleaned_data["password"])
        user.save()
        messages.success(request, "Пароль обновлён.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_password.html", {"form": form, "user_obj": user})


@role_required("Администратор системы")
def roles_list(request):
    qs = Role.objects.all()
    return render(request, "admin_panel/roles_list.html", {"roles": qs})


@role_required("Администратор системы")
def role_create(request):
    form = RoleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Роль создана.")
        return redirect("/admin-panel/roles/")
    return render(request, "admin_panel/role_form.html", {"form": form, "title": "Создать роль"})


@role_required("Администратор системы")
def backup_list(request):
    qs = Backup.objects.all().order_by("-created_at")
    schedule = BackupSchedule.objects.first()
    backups = []
    for b in qs:
        try:
            size = os.path.getsize(b.file_path) if os.path.exists(b.file_path) else 0
        except OSError:
            size = 0
        backups.append({"obj": b, "size": size})
    return render(request, "admin_panel/backups.html", {"backups": backups, "schedule": schedule})


@role_required("Администратор системы")
def backup_create(request):
    db_path = settings.DATABASES["default"]["NAME"]
    if not db_path or not os.path.exists(db_path):
        messages.error(request, "Файл базы данных не найден.")
        return redirect("/admin-panel/backups/")
    os.makedirs(settings.MEDIA_ROOT / "backups", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = settings.MEDIA_ROOT / "backups" / f"backup_{ts}.sqlite3"
    shutil.copy2(db_path, dest)
    Backup.objects.create(file_path=str(dest), created_by=request.user, status="created")
    messages.success(request, "Резервная копия создана.")
    return redirect("/admin-panel/backups/")


@role_required("Администратор системы")
def backup_restore(request, pk):
    backup = get_object_or_404(Backup, pk=pk)
    db_path = settings.DATABASES["default"]["NAME"]
    if request.method == "POST":
        if os.path.exists(backup.file_path) and db_path:
            shutil.copy2(backup.file_path, db_path)
            backup.status = "restored"
            backup.save(update_fields=["status"])
            messages.success(request, "Резервная копия восстановлена.")
        else:
            messages.error(request, "Файл резервной копии не найден.")
    return redirect("/admin-panel/backups/")


@role_required("Администратор системы")
def backup_schedule(request):
    schedule = BackupSchedule.objects.first()
    form = BackupScheduleForm(request.POST or None, instance=schedule)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Настройки резервного копирования сохранены.")
        return redirect("/admin-panel/backups/")
    return render(request, "admin_panel/backup_schedule.html", {"form": form, "title": "Расписание бэкапов"})


@role_required("Администратор системы")
def access_matrix(request):
    roles = Role.objects.all()
    rows = [
        {"name": "Клиенты", "url": "/clients/", "allowed": ["Менеджер", "Администратор системы"]},
        {"name": "Заказы", "url": "/orders/", "allowed": ["Менеджер", "Сборщик заказов", "Администратор системы"]},
        {"name": "Доставки", "url": "/logistics/", "allowed": ["Логист", "Администратор системы"]},
        {"name": "Маршруты", "url": "/logistics/routes/", "allowed": ["Логист", "Администратор системы"]},
        {"name": "Отчёты", "url": "/reports/", "allowed": ["Менеджер", "Администратор системы"]},
        {"name": "Аналитика", "url": "/reports/analytics/", "allowed": ["Менеджер", "Администратор системы"]},
        {"name": "Админ‑панель", "url": "/admin-panel/", "allowed": ["Администратор системы"]},
    ]
    return render(request, "admin_panel/access.html", {"rows": rows, "roles": roles})


@role_required("Администратор системы")
def data_check(request):
    report = {"errors": [], "warnings": []}
    if request.method == "POST":
        if Order.objects.filter(client__isnull=True).exists():
            report["errors"].append("Есть заказы без клиента.")
        if Delivery.objects.filter(order__isnull=True).exists():
            report["errors"].append("Есть доставки без заказа.")
        if Delivery.objects.filter(courier__isnull=True, status__in=["Запланировано", "В пути", "Доставлено"]).exists():
            report["errors"].append("Есть доставки со статусом в работе без курьера.")
        if Client.objects.filter(phone="").exists():
            report["warnings"].append("Есть клиенты без телефона.")
        if Client.objects.filter(email="").exists():
            report["warnings"].append("Есть клиенты без email.")
        if not report["errors"] and not report["warnings"]:
            report["warnings"].append("Критичных проблем не найдено.")
    return render(request, "admin_panel/data_check.html", {"report": report})

def _get_entity(slug: str) -> EntityConfig:
    for entity in ENTITIES:
        if entity.slug == slug:
            return entity
    return None


def _resolve_accessor(obj, accessor):
    if callable(accessor):
        value = accessor(obj)
        if isinstance(value, bool):
            return "Да" if value else "Нет"
        return value
    if isinstance(accessor, str):
        display_method = f"get_{accessor}_display"
        if hasattr(obj, display_method):
            value = getattr(obj, display_method)()
            return value
        value = getattr(obj, accessor, "")
        if callable(value):
            value = value()
        if isinstance(value, bool):
            return "Да" if value else "Нет"
        return value
    return ""


def _field_label(model, accessor):
    if isinstance(accessor, str):
        try:
            field = model._meta.get_field(accessor)
            return field.verbose_name.capitalize()
        except Exception:
            return accessor.replace("_", " ").capitalize()
    if callable(accessor):
        return getattr(accessor, "__name__", "Поле").replace("_", " ").capitalize()
    return "Поле"


def _build_filter_options(model, field_name):
    field = model._meta.get_field(field_name)
    if field.choices:
        return [{"value": choice[0], "label": choice[1]} for choice in field.choices]
    if isinstance(field, dj_models.BooleanField):
        return [{"value": "1", "label": "Да"}, {"value": "0", "label": "Нет"}]
    if field.is_relation:
        qs = field.remote_field.model.objects.all()
        return [{"value": str(obj.pk), "label": str(obj)} for obj in qs]
    return []


def _entity_form_class(model, exclude_fields=None):
    exclude_fields = exclude_fields or []
    for field in model._meta.fields:
        if not field.editable or field.auto_created:
            exclude_fields.append(field.name)
    for field in model._meta.many_to_many:
        if not field.editable:
            exclude_fields.append(field.name)
        if field.remote_field.through and not field.remote_field.through._meta.auto_created:
            exclude_fields.append(field.name)

    meta_class = type(
        "Meta",
        (),
        {
            "model": model,
            "fields": "__all__",
            "exclude": list(set(exclude_fields)),
        },
    )

    class EntityForm(BootstrapFormMixin, forms.ModelForm):
        Meta = meta_class

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._init_bootstrap()
            for field in self.fields.values():
                if isinstance(field.widget, forms.Textarea):
                    field.widget.attrs.setdefault("rows", 3)
                    field.widget.attrs.setdefault("data-size", "full")
                if isinstance(field, forms.DateField) and not isinstance(field, forms.DateTimeField):
                    field.widget.attrs.setdefault("type", "date")
                if isinstance(field, forms.DateTimeField):
                    field.widget.attrs.setdefault("type", "datetime-local")

    return EntityForm


@role_required("Администратор системы")
def entity_list(request, slug):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    model = entity.model
    qs = model.objects.all()

    query = request.GET.get("q", "").strip()
    if query and entity.search_fields:
        q_obj = Q()
        for field in entity.search_fields:
            q_obj |= Q(**{f"{field}__icontains": query})
        qs = qs.filter(q_obj)

    filters = []
    for field_name in entity.filter_fields:
        value = request.GET.get(field_name, "")
        field = model._meta.get_field(field_name)
        if value != "":
            if isinstance(field, dj_models.BooleanField):
                qs = qs.filter(**{field_name: value in ["1", "true", "True"]})
            elif field.is_relation:
                qs = qs.filter(**{field_name: value})
            else:
                qs = qs.filter(**{field_name: value})
        filters.append(
            {
                "name": field_name,
                "label": field.verbose_name.capitalize(),
                "value": value,
                "options": _build_filter_options(model, field_name),
            }
        )

    date_filters = []
    for field_name in entity.date_fields:
        start = request.GET.get(f"{field_name}_from", "")
        end = request.GET.get(f"{field_name}_to", "")
        field = model._meta.get_field(field_name)
        if start:
            key = f"{field_name}__date__gte" if isinstance(field, dj_models.DateTimeField) else f"{field_name}__gte"
            qs = qs.filter(**{key: start})
        if end:
            key = f"{field_name}__date__lte" if isinstance(field, dj_models.DateTimeField) else f"{field_name}__lte"
            qs = qs.filter(**{key: end})
        date_filters.append({"name": field_name, "label": field.verbose_name.capitalize(), "from": start, "to": end})

    allowed_sort = {f.name for f in model._meta.fields}
    sort_field = request.GET.get("sort", "")
    sort_dir = request.GET.get("dir", "desc")
    if sort_field in allowed_sort:
        ordering = f"-{sort_field}" if sort_dir == "desc" else sort_field
        qs = qs.order_by(ordering)

    paginator = Paginator(qs, 20)
    page_obj = paginator.get_page(request.GET.get("page"))
    query_params = request.GET.copy()
    if "page" in query_params:
        query_params.pop("page")
    query_string = query_params.urlencode()
    rows = []
    for obj in page_obj:
        cells = []
        for _, accessor in entity.list_display:
            cells.append(_resolve_accessor(obj, accessor))
        rows.append({"obj": obj, "cells": cells})

    sort_options = [
        {"value": f.name, "label": f.verbose_name.capitalize()}
        for f in model._meta.fields
        if f.name in allowed_sort
    ]

    return render(
        request,
        "admin_panel/entities/list.html",
        {
            "entity": entity,
            "headers": [header for header, _ in entity.list_display],
            "rows": rows,
            "filters": filters,
            "date_filters": date_filters,
            "query": query,
            "page_obj": page_obj,
            "paginator": paginator,
            "sort_options": sort_options,
            "sort_field": sort_field,
            "sort_dir": sort_dir,
            "query_string": query_string,
        },
    )


@role_required("Администратор системы")
def entity_detail(request, slug, pk):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    obj = get_object_or_404(entity.model, pk=pk)
    fields = []
    for field in obj._meta.fields:
        if field.choices:
            value = getattr(obj, f"get_{field.name}_display")()
        else:
            value = getattr(obj, field.name)
        if field.is_relation:
            value = str(value) if value else "—"
        elif isinstance(field, dj_models.BooleanField):
            value = "Да" if value else "Нет"
        fields.append({"label": field.verbose_name.capitalize(), "value": value})

    inline_sections = []
    for inline in entity.inlines:
        qs = inline.get_queryset(obj)
        rows = []
        for row in qs:
            values = [_resolve_accessor(row, f) for f in inline.fields]
            rows.append(values)
        model = getattr(qs, "model", None)
        headers = [_field_label(model, f) for f in inline.fields] if model else [str(f) for f in inline.fields]
        count = qs.count() if hasattr(qs, "count") else len(rows)
        inline_sections.append({"label": inline.label, "headers": headers, "rows": rows, "count": count})

    return render(
        request,
        "admin_panel/entities/detail.html",
        {"entity": entity, "obj": obj, "fields": fields, "inline_sections": inline_sections},
    )


@role_required("Администратор системы")
def entity_create(request, slug):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    form_class = entity.create_form_class or _entity_form_class(entity.model)
    form = form_class(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            if hasattr(obj, "created_at") and not getattr(obj, "created_at"):
                obj.created_at = timezone.now()
            if isinstance(form, UserCreateForm):
                roles = form.cleaned_data.pop("roles", [])
                password = form.cleaned_data.pop("password")
                user = User.objects.create(**form.cleaned_data)
                user.set_password(password)
                user.save()
                user.roles.set(roles)
            else:
                obj.save()
                if hasattr(form, "save_m2m"):
                    form.save_m2m()
            messages.success(request, "Сохранено.")
            return redirect(f"/admin-panel/entities/{entity.slug}/")
        messages.error(request, "Ошибка валидации.")
    return render(request, "admin_panel/entities/form.html", {"entity": entity, "form": form, "is_edit": False})


@role_required("Администратор системы")
def entity_edit(request, slug, pk):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    obj = get_object_or_404(entity.model, pk=pk)
    form_class = entity.edit_form_class or _entity_form_class(entity.model)
    if form_class is UserUpdateForm:
        form = form_class(request.POST or None, instance=obj, initial={"roles": obj.roles.all()})
    else:
        form = form_class(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            if isinstance(form, UserUpdateForm):
                roles = form.cleaned_data.pop("roles", [])
                form.save()
                obj.roles.set(roles)
            else:
                form.save()
            messages.success(request, "Сохранено.")
            return redirect(f"/admin-panel/entities/{entity.slug}/{obj.pk}/")
        messages.error(request, "Ошибка валидации.")
    return render(request, "admin_panel/entities/form.html", {"entity": entity, "form": form, "is_edit": True})


@role_required("Администратор системы")
def entity_delete(request, slug, pk):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    obj = get_object_or_404(entity.model, pk=pk)
    blockers = []
    if isinstance(obj, Client):
        count = obj.orders.count()
        if count:
            blockers.append(f"Есть связанные заказы: {count}. Удаление запрещено.")
    if isinstance(obj, Order):
        items = obj.items.count()
        deliveries = obj.deliveries.count()
        if items:
            blockers.append(f"Есть позиции заказа: {items}.")
        if deliveries:
            blockers.append(f"Есть доставки: {deliveries}.")
        if items or deliveries:
            blockers.append("Рекомендуется архивировать заказ вместо удаления.")

    if request.method == "POST":
        if blockers:
            messages.error(request, "Удаление запрещено из‑за связанных данных.")
            return redirect(f"/admin-panel/entities/{entity.slug}/{obj.pk}/")
        try:
            obj.delete()
            messages.success(request, "Удалено.")
        except Exception:
            messages.error(request, "Ошибка удаления.")
        return redirect(f"/admin-panel/entities/{entity.slug}/")

    return render(
        request,
        "admin_panel/entities/delete.html",
        {"entity": entity, "obj": obj, "blockers": blockers},
    )
