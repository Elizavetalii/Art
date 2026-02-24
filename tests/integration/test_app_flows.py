from datetime import timedelta
from decimal import Decimal

from django.test import TestCase
from django.utils import timezone

from crm.models import (
    Client,
    CooperationStage,
    Courier,
    CourierAssignment,
    Delivery,
    Dish,
    Ingredient,
    IngredientStock,
    InteractionType,
    Order,
    OrderItem,
    OrderStatus,
    Role,
    Route,
    RouteStatus,
    RouteStop,
    TechCard,
    TechCardComponent,
    User,
)


class AppIntegrationTests(TestCase):
    """Сквозные интеграционные проверки для основных модулей Art Culinary CRM."""

    @classmethod
    def setUpTestData(cls):
        cls.role_manager = Role.objects.create(name="Менеджер")
        cls.role_logist = Role.objects.create(name="Логист")
        cls.role_admin = Role.objects.create(name="Администратор системы")
        cls.role_picker = Role.objects.create(name="Сборщик заказов")
        cls.role_courier = Role.objects.create(name="Курьер")

        cls.manager = User.objects.create_user(
            username="manager",
            email="manager@test.local",
            password="Pass12345!",
            full_name="Manager Test",
        )
        cls.manager.roles.add(cls.role_manager)

        cls.logist = User.objects.create_user(
            username="logist",
            email="logist@test.local",
            password="Pass12345!",
            full_name="Logist Test",
        )
        cls.logist.roles.add(cls.role_logist)

        cls.admin = User.objects.create_user(
            username="admin",
            email="admin@test.local",
            password="Pass12345!",
            full_name="Admin Test",
        )
        cls.admin.roles.add(cls.role_admin)

        cls.picker = User.objects.create_user(
            username="picker",
            email="picker@test.local",
            password="Pass12345!",
            full_name="Picker Test",
        )
        cls.picker.roles.add(cls.role_picker)

        cls.courier_user = User.objects.create_user(
            username="courier",
            email="courier@test.local",
            password="Pass12345!",
            full_name="Courier Test",
        )
        cls.courier_user.roles.add(cls.role_courier)

        cls.stage = CooperationStage.objects.create(name="Переговоры", order=1, is_active=True)
        cls.client_obj = Client.objects.create(
            name="ООО Тест Клиент",
            client_type="store",
            status="active",
            current_stage=cls.stage,
            responsible_manager=cls.manager,
            default_delivery_address="Санкт-Петербург, Невский 1",
            email="client@test.local",
            phone="+79990000000",
        )

        cls.ingredient = Ingredient.objects.create(name="Картофель", is_active=True)
        IngredientStock.objects.create(ingredient=cls.ingredient, quantity=Decimal("500.000"))
        cls.dish = Dish.objects.create(
            name="Оливье",
            unit="кг",
            base_uom=Dish.BaseUom.KG,
            quantity_scale=3,
            default_price=Decimal("900.00"),
            is_active=True,
            created_by=cls.manager,
        )
        tech = TechCard.objects.create(
            dish=cls.dish,
            version_label="v1",
            is_active=True,
            approved_by=cls.manager,
        )
        TechCardComponent.objects.create(
            tech_card=tech,
            ingredient=cls.ingredient,
            quantity=Decimal("1.000"),
        )

    def _make_order(self, qty=Decimal("10.000")):
        order = Order.objects.create(
            order_number=Order.generate_order_number(),
            client=self.client_obj,
            manager=self.manager,
            address=self.client_obj.default_delivery_address,
            status=OrderStatus.REVIEW,
            delivery_date=timezone.localdate() + timedelta(days=1),
            delivery_time=timezone.localtime().time().replace(microsecond=0),
            delivery_type="Разовая",
        )
        OrderItem.objects.create(
            order=order,
            dish=self.dish,
            quantity=qty,
            unit_price=Decimal("900.00"),
        )
        order.refresh_from_db()
        return order

    def test_login_redirect_by_role(self):
        response = self.client.post(
            "/login/",
            {"username": "manager", "password": "Pass12345!"},
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/dashboard/manager/")

    def test_manager_clients_pages_and_create(self):
        self.client.force_login(self.manager)
        self.assertEqual(self.client.get("/clients/").status_code, 200)
        create_resp = self.client.post(
            "/clients/create/",
            {
                "name": "ООО Новый клиент",
                "client_type": "store",
                "inn": "123",
                "kpp": "456",
                "default_delivery_address": "СПб",
                "email": "new-client@test.local",
                "phone": "+79991112233",
                "status": "prospect",
                "current_stage": str(self.stage.id),
            },
            follow=False,
        )
        self.assertEqual(create_resp.status_code, 302)
        self.assertTrue(Client.objects.filter(email="new-client@test.local").exists())

    def test_client_detail_interaction_and_stage_history(self):
        self.client.force_login(self.manager)
        detail_url = f"/clients/{self.client_obj.id}/"
        response = self.client.post(
            detail_url,
            {
                "action": "add_interaction",
                "interaction-interaction_type": InteractionType.CALL,
                "interaction-note": "Созвон",
                "interaction-happened_at": timezone.localtime().strftime("%Y-%m-%dT%H:%M"),
            },
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        response2 = self.client.post(
            detail_url,
            {
                "action": "change_stage",
                "stage-stage": str(self.stage.id),
                "stage-comment": "Оставили на текущем этапе",
            },
            follow=False,
        )
        self.assertEqual(response2.status_code, 302)
        self.client_obj.refresh_from_db()
        self.assertEqual(self.client_obj.current_stage_id, self.stage.id)

    def test_order_status_flow_creates_delivery(self):
        self.client.force_login(self.manager)
        order = self._make_order()
        response = self.client.post(
            f"/orders/{order.id}/status/",
            {"status": OrderStatus.SHIPPED},
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        order.refresh_from_db()
        self.assertEqual(order.status, OrderStatus.SHIPPED)
        self.assertTrue(Delivery.objects.filter(order=order).exists())

    def test_order_archive_toggle_and_bulk_delete(self):
        self.client.force_login(self.manager)
        order1 = self._make_order()
        order2 = self._make_order()
        response = self.client.post(f"/orders/{order1.id}/archive-toggle/", follow=False)
        self.assertEqual(response.status_code, 302)
        order1.refresh_from_db()
        self.assertTrue(order1.is_archived)

        bulk = self.client.post(
            "/orders/bulk-delete/",
            {"order_ids": [str(order1.id), str(order2.id)]},
            follow=False,
        )
        self.assertEqual(bulk.status_code, 302)
        self.assertFalse(Order.objects.filter(id__in=[order1.id, order2.id]).exists())

    def test_order_item_recalculates_order_total(self):
        order = self._make_order(qty=Decimal("5.000"))
        self.assertEqual(order.total_amount, Decimal("4500.00"))
        item = order.items.first()
        item.quantity = Decimal("7.000")
        item.save()
        order.refresh_from_db()
        self.assertEqual(order.total_amount, Decimal("6300.00"))

    def test_logistics_routes_and_assignments_model_integration(self):
        order = self._make_order()
        delivery = Delivery.objects.create(
            order=order,
            address=order.address,
            status=Delivery.DeliveryStatus.PLANNED,
        )
        route = Route.objects.create(
            logistician=self.logist,
            planned_date=timezone.localdate() + timedelta(days=1),
            status=RouteStatus.PLANNED,
        )
        courier = Courier.objects.create(
            user=self.courier_user,
            transport_type="car",
            experience_years=2,
            status="Свободен",
            zone="СПб",
        )
        CourierAssignment.objects.create(courier=courier, route=route)
        RouteStop.objects.create(
            route=route,
            delivery=delivery,
            sequence_index=1,
            status=RouteStop.StopStatus.PLANNED,
        )
        delivery.route = route
        delivery.courier = courier
        delivery.save()

        self.assertEqual(route.assignments.count(), 1)
        self.assertEqual(route.stops.count(), 1)
        self.assertEqual(delivery.route_id, route.id)

    def test_logistics_pages_access_by_roles(self):
        self.client.force_login(self.logist)
        self.assertEqual(self.client.get("/logistics/").status_code, 200)
        self.assertEqual(self.client.get("/logistics/routes/").status_code, 200)
        self.assertEqual(self.client.get("/logistics/couriers/").status_code, 200)

        self.client.force_login(self.courier_user)
        self.assertEqual(self.client.get("/logistics/courier/profile/").status_code, 200)
        self.assertEqual(self.client.get("/logistics/courier/routes/").status_code, 200)

    def test_reports_pages(self):
        self.client.force_login(self.manager)
        self.assertEqual(self.client.get("/reports/").status_code, 200)
        self.assertEqual(self.client.get("/reports/analytics/").status_code, 200)

    def test_admin_panel_pages(self):
        self.client.force_login(self.admin)
        self.assertEqual(self.client.get("/admin-panel/").status_code, 200)
        self.assertEqual(self.client.get("/admin-panel/users/").status_code, 200)
        self.assertEqual(self.client.get("/admin-panel/roles/").status_code, 200)
        self.assertEqual(self.client.get("/admin-panel/access/").status_code, 200)
        self.assertEqual(self.client.get("/admin-panel/data-check/").status_code, 200)

    def test_api_endpoints_require_auth(self):
        self.assertEqual(self.client.get("/api/clients/").status_code, 401)
        self.client.force_login(self.manager)
        authed = self.client.get("/api/clients/")
        self.assertEqual(authed.status_code, 200)
