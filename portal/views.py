from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from crm.models import Client, Order, Delivery
from .forms import ClientForm, OrderForm, OrderStatusForm, DeliveryPlanForm
from .utils import role_required, roles_required


@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        # если уже менеджер, ведём в кабинет
        if request.user.roles.filter(name__iexact="Менеджер").exists():
            return redirect("/manager/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Неверные логин или пароль.")
        else:
            login(request, user)
            # маршрутизация по роли
            if user.roles.filter(name__iexact="Менеджер").exists():
                return redirect("/manager/")
            if user.roles.filter(name__iexact="Логист").exists():
                return redirect("/logistic/")
            if user.roles.filter(name__iexact="Сборщик заказов").exists():
                return redirect("/picker/")
            if user.roles.filter(name__iexact="Администратор системы").exists():
                return redirect("/admin-panel/")
            messages.error(request, "Нет прав для доступа.")
    return render(request, "portal/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


@role_required("Менеджер")
def manager_dashboard(request):
    stats = {
        "clients": Client.objects.count(),
        "orders": Order.objects.count(),
        "active_orders": Order.objects.filter(status__in=["confirmed", "in_progress"]).count(),
    }
    return render(request, "portal/manager_dashboard.html", {"stats": stats})


@role_required("Менеджер")
def clients_list(request):
    qs = Client.objects.all()
    q = request.GET.get("q")
    status = request.GET.get("status")
    if q:
        qs = qs.filter(name__icontains=q)
    if status:
        qs = qs.filter(status=status)
    return render(request, "portal/clients_list.html", {"clients": qs})


@role_required("Менеджер")
def client_create(request):
    form = ClientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/manager/clients/")
    return render(request, "portal/client_form.html", {"form": form, "title": "Новый клиент"})


@role_required("Менеджер")
def client_edit(request, pk):
    obj = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/manager/clients/")
    return render(request, "portal/client_form.html", {"form": form, "title": "Редактирование клиента"})


@role_required("Менеджер")
def order_list(request):
    qs = Order.objects.select_related("client")
    q = request.GET.get("q")
    status = request.GET.get("status")
    if q:
        qs = qs.filter(order_number__icontains=q)
    if status:
        qs = qs.filter(status=status)
    return render(request, "portal/orders_list.html", {"orders": qs})


@role_required("Менеджер")
def order_create(request):
    form = OrderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.manager = request.user
        obj.save()
        return redirect("/manager/orders/")
    return render(request, "portal/order_form.html", {"form": form, "title": "Новый заказ"})


@role_required("Менеджер")
def order_edit(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/manager/orders/")
    return render(request, "portal/order_form.html", {"form": form, "title": "Редактирование заказа"})


# --------- Кабинет логиста ---------
@roles_required(["Логист"])
def logistic_dashboard(request):
    deliveries = Delivery.objects.select_related("order", "courier").all()
    return render(request, "portal/logistic_dashboard.html", {"deliveries": deliveries})


@roles_required(["Логист"])
def delivery_plan(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    form = DeliveryPlanForm(request.POST or None, instance=delivery)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/logistic/")
    return render(request, "portal/delivery_plan.html", {"form": form, "title": "Планирование доставки", "delivery": delivery})


# --------- Кабинет сборщика ---------
@roles_required(["Сборщик заказов"])
def picker_dashboard(request):
    orders = Order.objects.all()
    form = OrderStatusForm()
    return render(request, "portal/picker_dashboard.html", {"orders": orders, "form": form})


@roles_required(["Сборщик заказов"])
def picker_update_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderStatusForm(request.POST or None, instance=order)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/picker/")
    return render(request, "portal/order_form.html", {"form": form, "title": "Статус заказа"})


# --------- Кабинет администратора системы ---------
@roles_required(["Администратор системы"])
def sysadmin_dashboard(request):
    return render(request, "portal/sysadmin_dashboard.html")
