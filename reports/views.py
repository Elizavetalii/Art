from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from accounts.utils import roles_required
from .models import Report
from .forms import ReportForm
from crm.models import Order, OrderStatus, Client


@roles_required(["Менеджер", "Администратор системы"])
def reports_list(request):
    qs = Report.objects.all().order_by("-created_at")
    return render(request, "reports/list.html", {"reports": qs})


@roles_required(["Менеджер", "Администратор системы"])
def report_create(request):
    initial = {}
    if request.method == "GET":
        if request.GET.get("from"):
            initial["period_from"] = request.GET.get("from")
        if request.GET.get("to"):
            initial["period_to"] = request.GET.get("to")
    form = ReportForm(request.POST or None, request.FILES or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user
        obj.save()
        return redirect("/reports/")
    return render(request, "reports/form.html", {"form": form, "title": "Создать отчёт"})


@roles_required(["Менеджер", "Администратор системы"])
def report_edit(request, pk):
    obj = get_object_or_404(Report, pk=pk)
    form = ReportForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/reports/")
    return render(request, "reports/form.html", {"form": form, "title": "Редактировать отчёт"})


@roles_required(["Менеджер", "Администратор системы"])
def report_validate(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        if report.period_from and report.period_to and report.period_from > report.period_to:
            report.validation_status = "error"
            report.validation_message = "Дата начала больше даты окончания."
        elif not report.file:
            report.validation_status = "warn"
            report.validation_message = "Файл отчёта не загружен."
        else:
            report.validation_status = "ok"
            report.validation_message = "Проверка пройдена успешно."
        report.save(update_fields=["validation_status", "validation_message"])
    return redirect("/reports/")


@roles_required(["Менеджер", "Администратор системы"])
def analytics_view(request):
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")
    status = request.GET.get("status")
    client_id = request.GET.get("client")
    qs = Order.objects.all()
    if date_from:
        qs = qs.filter(created_at__date__gte=date_from)
    if date_to:
        qs = qs.filter(created_at__date__lte=date_to)
    if status:
        qs = qs.filter(status=status)
    if client_id:
        qs = qs.filter(client_id=client_id)
    total_orders = qs.count()
    revenue = qs.aggregate(total=Sum("total_amount"))["total"] or 0
    avg_check = round((revenue / total_orders), 2) if total_orders else 0
    status_labels = dict(OrderStatus.choices)
    raw_status = list(qs.values("status").annotate(cnt=Count("id")))
    max_cnt = max([row["cnt"] for row in raw_status], default=0) or 1
    by_status = [
        {
            "status": row["status"],
            "label": status_labels.get(row["status"], row["status"]),
            "cnt": row["cnt"],
            "percent": int((row["cnt"] / max_cnt) * 100),
        }
        for row in raw_status
    ]
    by_day = (
        qs.annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(cnt=Count("id"), revenue=Sum("total_amount"))
        .order_by("day")
    )
    by_day = [
        {
            "day": row["day"].strftime("%Y-%m-%d") if row["day"] else "",
            "cnt": row["cnt"],
            "revenue": float(row["revenue"] or 0),
        }
        for row in by_day
    ]
    avg_check_by_day = [
        {
            "day": row["day"],
            "avg_check": round((row["revenue"] / row["cnt"]), 2) if row["cnt"] else 0,
        }
        for row in by_day
    ]
    by_client = (
        qs.values("client__name")
        .annotate(cnt=Count("id"), revenue=Sum("total_amount"))
        .order_by("-revenue")[:10]
    )
    by_client = [
        {
            "client": row["client__name"] or "—",
            "cnt": row["cnt"],
            "revenue": float(row["revenue"] or 0),
        }
        for row in by_client
    ]
    by_client_type = (
        qs.values("client__client_type")
        .annotate(cnt=Count("id"), revenue=Sum("total_amount"))
        .order_by("-cnt")
    )
    by_client_type = [
        {
            "type": row["client__client_type"] or "—",
            "cnt": row["cnt"],
            "revenue": float(row["revenue"] or 0),
        }
        for row in by_client_type
    ]
    clients = Client.objects.all()
    context = {
        "total_orders": total_orders,
        "revenue": revenue,
        "avg_check": avg_check,
        "by_status": list(by_status),
        "by_day": by_day,
        "avg_check_by_day": avg_check_by_day,
        "by_client": by_client,
        "by_client_type": by_client_type,
        "today": timezone.now().date(),
        "clients": clients,
        "statuses": OrderStatus.choices,
    }
    return render(request, "reports/analytics.html", context)

# Create your views here.
