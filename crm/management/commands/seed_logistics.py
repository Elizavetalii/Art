import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from crm.models import (
    Client,
    Order,
    OrderStatus,
    Delivery,
    Route,
    RouteStop,
    Courier,
    CourierStatus,
    User,
    Role,
)


class Command(BaseCommand):
    help = "Создаёт фиктивные данные для логистики."

    def handle(self, *args, **options):
        fake = Faker("ru_RU")

        courier_role, _ = Role.objects.get_or_create(name="Курьер")
        logistic_role, _ = Role.objects.get_or_create(name="Логист")

        logistic_user = (
            User.objects.filter(roles__name="Логист").first()
            or User.objects.filter(is_superuser=True).first()
        )
        if not logistic_user:
            logistic_user = User.objects.create_user(
                username="logistic_seed",
                email="logistic_seed@art.com",
                password="LogisticSeed123!",
                full_name="Логист Сид",
                is_active=True,
            )
            logistic_user.roles.add(logistic_role)

        transports = ["Авто", "Фургон", "Грузовик", "Вело"]
        zones = ["Центр", "Север", "Юг", "Восток", "Запад"]

        couriers = []
        for i in range(10):
            username = f"courier_seed_{i+1}"
            user, _ = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"{username}@art.com",
                    "full_name": f"Курьер {i+1}",
                    "is_active": True,
                },
            )
            user.roles.add(courier_role)
            if not user.has_usable_password():
                user.set_password("CourierSeed123!")
                user.save()
            courier, _ = Courier.objects.get_or_create(
                user=user,
                defaults={
                    "transport_type": random.choice(transports),
                    "experience_years": random.randint(1, 7),
                    "zone": random.choice(zones),
                    "status": random.choice([CourierStatus.FREE, CourierStatus.BUSY, CourierStatus.ON_ROUTE]),
                    "payload_capacity_kg": Decimal(random.randint(50, 1200)),
                    "cargo_volume_m3": Decimal(random.randint(1, 12)),
                    "cargo_length_cm": Decimal(random.randint(120, 400)),
                    "cargo_width_cm": Decimal(random.randint(80, 200)),
                    "cargo_height_cm": Decimal(random.randint(60, 200)),
                    "max_weight": Decimal(random.randint(50, 1200)),
                    "max_volume": Decimal(random.randint(1, 12)),
                    "current_lat": Decimal("55.%03d" % random.randint(600, 900)),
                    "current_lng": Decimal("37.%03d" % random.randint(400, 800)),
                    "current_latitude": Decimal("55.%03d" % random.randint(600, 900)),
                    "current_longitude": Decimal("37.%03d" % random.randint(400, 800)),
                    "location_updated_at": timezone.now(),
                },
            )
            couriers.append(courier)

        clients = list(Client.objects.all())
        if len(clients) < 10:
            for _ in range(10 - len(clients)):
                clients.append(
                    Client.objects.create(
                        name=fake.company(),
                        client_type="store",
                        inn=str(fake.random_number(digits=10)),
                        kpp=str(fake.random_number(digits=9)),
                        default_delivery_address=fake.address(),
                        email=fake.email(),
                        phone=fake.phone_number(),
                        status="active",
                    )
                )

        orders = []
        start_number = 3000
        for idx in range(50):
            order_number = f"LOG-{start_number + idx}"
            client = random.choice(clients)
            order, _ = Order.objects.get_or_create(
                order_number=order_number,
                defaults={
                    "client": client,
                    "manager": None,
                    "status": random.choice(
                        [OrderStatus.REVIEW, OrderStatus.IN_PRODUCTION, OrderStatus.SHIPPED]
                    ),
                    "address": client.default_delivery_address or fake.address(),
                    "total_amount": Decimal(random.randint(10000, 150000)),
                },
            )
            orders.append(order)

        deliveries = []
        for order in orders:
            delivery, _ = Delivery.objects.get_or_create(
                order=order,
                defaults={
                    "courier": random.choice(couriers),
                    "planned_at": timezone.now(),
                    "address": order.address,
                    "status": "Запланировано",
                    "cargo_weight_kg": Decimal(random.randint(5, 800)),
                    "cargo_volume_m3": Decimal(random.randint(1, 8)),
                    "cargo_length_cm": Decimal(random.randint(40, 200)),
                    "cargo_width_cm": Decimal(random.randint(40, 160)),
                    "cargo_height_cm": Decimal(random.randint(30, 160)),
                },
            )
            deliveries.append(delivery)

        routes = []
        for idx in range(5):
            route, _ = Route.objects.get_or_create(
                planned_date=timezone.now().date(),
                logistician=logistic_user,
                defaults={
                    "status": random.choice(["Запланирован", "Выполняется"]),
                    "notes": f"Маршрут {idx + 1}",
                },
            )
            routes.append(route)

        random.shuffle(deliveries)
        stop_deliveries = deliveries[:30]
        per_route = 6
        for route_idx, route in enumerate(routes):
            slice_start = route_idx * per_route
            slice_end = slice_start + per_route
            for seq, delivery in enumerate(stop_deliveries[slice_start:slice_end], start=1):
                RouteStop.objects.get_or_create(
                    route=route,
                    delivery=delivery,
                    defaults={
                        "sequence_index": seq,
                        "planned_time": timezone.now(),
                        "status": random.choice(["Запланирована", "В пути", "Доставлено"]),
                        "latitude": Decimal("55.%03d" % random.randint(600, 900)),
                        "longitude": Decimal("37.%03d" % random.randint(400, 800)),
                    },
                )

        self.stdout.write(self.style.SUCCESS("Логистические демо-данные созданы."))
