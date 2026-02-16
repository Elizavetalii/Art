from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from crm.models import (
    Role,
    UserRole,
    Client,
    CooperationStage,
    ClientStageHistory,
    Interaction,
    Order,
    Delivery,
    Courier,
    OrderStatus,
    InteractionType,
    Route,
    RouteStop,
)
from reports.models import Report


class Command(BaseCommand):
    help = "Создаёт демо-данные для CRM"

    def handle(self, *args, **options):
        User = get_user_model()

        roles = [
            "Менеджер",
            "Логист",
            "Сборщик заказов",
            "Администратор системы",
        ]
        role_map = {}
        for name in roles:
            role, _ = Role.objects.get_or_create(name=name)
            role_map[name] = role

        users_data = [
            ("manager_demo", "Менеджер", "ManagerDemo123!", "manager@art.com"),
            ("logistic_demo", "Логист", "LogisticDemo123!", "logistic@art.com"),
            ("picker_demo", "Сборщик заказов", "PickerDemo123!", "picker@art.com"),
            ("admin_demo", "Администратор системы", "AdminDemo123!", "admin@art.com"),
        ]
        users = {}
        for username, role_name, password, email in users_data:
            user, _ = User.objects.get_or_create(
                username=username,
                defaults={"email": email, "full_name": role_name, "is_active": True},
            )
            user.set_password(password)
            user.save()
            UserRole.objects.get_or_create(user=user, role=role_map[role_name])
            users[role_name] = user

        stages = [
            ("Лид", 1),
            ("Переговоры", 2),
            ("Контракт", 3),
            ("Сделка", 4),
        ]
        stage_objs = []
        for name, order in stages:
            s, _ = CooperationStage.objects.get_or_create(name=name, defaults={"order": order, "is_active": True})
            stage_objs.append(s)

        client_names = [
            "ООО «Север»",
            "Кафе «Линия»",
            "Ресторан «Лист»",
            "Магазин «Вкус»",
            "Дистрибьютор «Трейд»",
        ]
        clients = []
        for i, name in enumerate(client_names, start=1):
            c, _ = Client.objects.get_or_create(
                name=name,
                defaults={
                    "phone": f"+7 (900) 000-00-0{i}",
                    "email": f"client{i}@example.com",
                    "status": "active" if i % 2 == 0 else "prospect",
                    "responsible_manager": users["Менеджер"],
                    "current_stage": stage_objs[min(i - 1, len(stage_objs) - 1)],
                },
            )
            clients.append(c)
            ClientStageHistory.objects.get_or_create(
                client=c,
                stage=c.current_stage,
                defaults={"changed_by": users["Менеджер"], "comment": "Стартовая стадия"},
            )

        for c in clients:
            Interaction.objects.get_or_create(
                client=c,
                manager=users["Менеджер"],
                interaction_type=InteractionType.CALL,
                defaults={"note": "Первичный контакт", "happened_at": timezone.now()},
            )

        orders = []
        for idx, client in enumerate(clients, start=1001):
            order, _ = Order.objects.get_or_create(
                order_number=f"ORD-{idx}",
                defaults={
                    "client": client,
                    "manager": users["Менеджер"],
                    "status": OrderStatus.REVIEW if idx % 2 == 0 else OrderStatus.IN_PRODUCTION,
                    "address": client.default_delivery_address or "Москва, ул. Пример, 1",
                    "total_amount": 15000 + idx,
                },
            )
            orders.append(order)

        courier_user, _ = User.objects.get_or_create(
            username="courier_demo",
            defaults={"email": "courier@art.com", "full_name": "Курьер Демо", "is_active": True},
        )
        courier_user.set_password("CourierDemo123!")
        courier_user.save()
        courier, _ = Courier.objects.get_or_create(
            user=courier_user,
            defaults={"transport_type": "Авто", "experience_years": 3, "zone": "Центр"},
        )

        for order in orders:
            Delivery.objects.get_or_create(
                order=order,
                defaults={
                    "courier": courier,
                    "planned_at": timezone.now(),
                    "address": order.address,
                    "status": "planned",
                },
            )

        route, _ = Route.objects.get_or_create(
            planned_date=timezone.now().date(),
            defaults={"logistician": users["Логист"], "status": "planned"},
        )
        for idx, delivery in enumerate(Delivery.objects.all()[:3], start=1):
            RouteStop.objects.get_or_create(
                route=route,
                delivery=delivery,
                defaults={"sequence_index": idx, "planned_time": timezone.now()},
            )

        Report.objects.get_or_create(
            title="Отчёт по продажам",
            defaults={
                "period_from": timezone.now().date(),
                "period_to": timezone.now().date(),
                "status": "ready",
                "created_by": users["Менеджер"],
            },
        )

        self.stdout.write(self.style.SUCCESS("Демо-данные созданы."))
