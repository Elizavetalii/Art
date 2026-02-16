from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from crm.forms import ClientForm, OrderForm
from crm.models import Client, Order


def is_manager(user):
    return user.is_authenticated and user.roles.filter(name__iexact="Менеджер").exists()


class ManagerLoginView(LoginView):
    template_name = "login_root.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if is_manager(user):
            return "/manager/"
        if user.is_staff:
            return "/admin/"
        return "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        if is_manager(user) or user.is_staff:
            return response
        logout(self.request)
        form.add_error(None, _("У вас нет прав для входа. Обратитесь к администратору."))
        return self.form_invalid(form)


def manager_dashboard_view(request, *args, **kwargs):
    # protected view wrapper
    from django.views.generic import TemplateView

    protected_view = login_required(
        user_passes_test(is_manager)(TemplateView.as_view(template_name="manager_dashboard.html")),
        login_url='/'
    )
    return protected_view(request, *args, **kwargs)


@login_required(login_url='/')
@user_passes_test(is_manager, login_url='/')
def manager_clients_view(request):
    clients = Client.objects.all().select_related('responsible_manager')
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            if not client.responsible_manager:
                client.responsible_manager = request.user
            client.save()
            return redirect('/manager/clients/')
    else:
        form = ClientForm()
    return render(request, 'manager_clients.html', {'clients': clients, 'form': form})


@login_required(login_url='/')
@user_passes_test(is_manager, login_url='/')
def manager_orders_view(request):
    orders = Order.objects.select_related('client', 'manager').all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if not order.manager:
                order.manager = request.user
            order.save()
            return redirect('/manager/orders/')
    else:
        form = OrderForm()
    return render(request, 'manager_orders.html', {'orders': orders, 'form': form})
