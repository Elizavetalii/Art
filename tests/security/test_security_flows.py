from datetime import timedelta
from decimal import Decimal

from django.test import Client as DjangoClient
from django.test import TestCase
from django.utils import timezone

from crm.models import Client, CooperationStage, Dish, Order, OrderItem, OrderStatus, Role, User


class SecurityTests(TestCase):
    """Базовые проверки безопасности: доступ, RBAC, CSRF, API auth."""

    @classmethod
    def setUpTestData(cls):
        cls.role_manager = Role.objects.create(name="Менеджер")
        cls.role_admin = Role.objects.create(name="Администратор системы")

        cls.admin = User.objects.create_user(
            username="sec_admin",
            email="sec_admin@test.local",
            password="Pass12345!",
            full_name="Security Admin",
        )
        cls.admin.roles.add(cls.role_admin)

        cls.manager = User.objects.create_user(
            username="sec_manager",
            email="sec_manager@test.local",
            password="Pass12345!",
            full_name="Security Manager",
        )
        cls.manager.roles.add(cls.role_manager)

        stage = CooperationStage.objects.create(name="Переговоры", order=1, is_active=True)
        cls.client_obj = Client.objects.create(
            name="ООО Security Test",
            client_type="store",
            status="active",
            current_stage=stage,
            responsible_manager=cls.manager,
            default_delivery_address="СПб, Невский 10",
            email="client-security@test.local",
        )
        dish = Dish.objects.create(
            name="Салат",
            unit="кг",
            base_uom=Dish.BaseUom.KG,
            quantity_scale=3,
            default_price=Decimal("100.00"),
            is_active=True,
            created_by=cls.manager,
        )
        cls.order = Order.objects.create(
            order_number=Order.generate_order_number(),
            client=cls.client_obj,
            manager=cls.manager,
            address=cls.client_obj.default_delivery_address,
            status=OrderStatus.REVIEW,
            delivery_date=timezone.localdate() + timedelta(days=1),
            delivery_time=timezone.localtime().time().replace(microsecond=0),
            delivery_type="Разовая",
        )
        OrderItem.objects.create(
            order=cls.order,
            dish=dish,
            quantity=Decimal("2.000"),
            unit_price=Decimal("100.00"),
        )

    def test_admin_panel_requires_admin_role(self):
        self.client.force_login(self.manager)
        response = self.client.get("/admin-panel/", follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/")

    def test_admin_user_toggle_forbidden_for_manager(self):
        self.client.force_login(self.manager)
        before = self.admin.is_active
        response = self.client.post(f"/admin-panel/users/{self.admin.id}/toggle/", follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/")
        self.admin.refresh_from_db()
        self.assertEqual(self.admin.is_active, before)

    def test_api_requires_authentication(self):
        response = self.client.get("/api/clients/")
        self.assertEqual(response.status_code, 401)

    def test_jwt_token_rejects_invalid_credentials(self):
        response = self.client.post(
            "/api/token/",
            data={"username": "sec_admin", "password": "wrong-pass"},
            content_type="application/json",
        )
        self.assertIn(response.status_code, (400, 401))

    def test_csrf_protection_on_login_form(self):
        csrf_client = DjangoClient(enforce_csrf_checks=True)
        response = csrf_client.post(
            "/login/",
            {"username": "sec_manager", "password": "Pass12345!"},
            follow=False,
        )
        self.assertEqual(response.status_code, 403)

    def test_sql_injection_like_query_does_not_break_clients_page(self):
        self.client.force_login(self.manager)
        payload = "' OR 1=1 --"
        response = self.client.get("/clients/", {"q": payload})
        self.assertEqual(response.status_code, 200)

    def test_bulk_delete_requires_role_and_keeps_data_for_anonymous(self):
        order_id = self.order.id
        response = self.client.post("/orders/bulk-delete/", {"order_ids": [str(order_id)]}, follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/login/")
        self.assertTrue(Order.objects.filter(id=order_id).exists())

    def test_password_reset_flow_does_not_error_for_unknown_email(self):
        response = self.client.post(
            "/password-reset/",
            {"email": "unknown-security@test.local"},
            follow=False,
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/password-reset/done/")
