from decimal import Decimal

from django.core.management.base import BaseCommand

from crm.models import Dish, Ingredient, TechCard, TechCardComponent, TechCardVariant, User


class Command(BaseCommand):
    help = "Создаёт 10 блюд с техкартами и составом."

    def handle(self, *args, **options):
        seed_user = User.objects.filter(is_superuser=True).first() or User.objects.first()

        dishes = [
            {
                "name": "Салат Цезарь",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.25",
                "min_batch_qty": "5",
                "batch_multiple_qty": "1",
                "daily_capacity": "120",
                "default_price": "450.00",
                "ingredients": [
                    ("Курица", "0.08"),
                    ("Салат ромэн", "0.06"),
                    ("Пармезан", "0.02"),
                    ("Соус цезарь", "0.03"),
                    ("Гренки", "0.04"),
                ],
            },
            {
                "name": "Паста Болоньезе",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.35",
                "min_batch_qty": "6",
                "batch_multiple_qty": "1",
                "daily_capacity": "140",
                "default_price": "520.00",
                "ingredients": [
                    ("Паста", "0.18"),
                    ("Фарш говяжий", "0.10"),
                    ("Томатный соус", "0.05"),
                    ("Лук", "0.01"),
                    ("Пармезан", "0.01"),
                ],
            },
            {
                "name": "Ризотто с грибами",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.32",
                "min_batch_qty": "5",
                "batch_multiple_qty": "1",
                "daily_capacity": "110",
                "default_price": "480.00",
                "ingredients": [
                    ("Рис арборио", "0.12"),
                    ("Шампиньоны", "0.09"),
                    ("Бульон", "0.08"),
                    ("Сливки", "0.02"),
                    ("Пармезан", "0.01"),
                ],
            },
            {
                "name": "Суп Том Ям",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.40",
                "min_batch_qty": "8",
                "batch_multiple_qty": "1",
                "daily_capacity": "90",
                "default_price": "560.00",
                "ingredients": [
                    ("Креветки", "0.08"),
                    ("Кокосовое молоко", "0.12"),
                    ("Паста Том Ям", "0.03"),
                    ("Грибы", "0.05"),
                    ("Лемонграсс", "0.02"),
                ],
            },
            {
                "name": "Суп тыквенный",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.35",
                "min_batch_qty": "10",
                "batch_multiple_qty": "2",
                "daily_capacity": "200",
                "default_price": "320.00",
                "ingredients": [
                    ("Тыква", "0.20"),
                    ("Сливки", "0.05"),
                    ("Лук", "0.03"),
                    ("Масло сливочное", "0.01"),
                    ("Соль", "0.01"),
                ],
            },
            {
                "name": "Стейк из лосося",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.28",
                "min_batch_qty": "4",
                "batch_multiple_qty": "1",
                "daily_capacity": "60",
                "default_price": "890.00",
                "ingredients": [
                    ("Лосось", "0.20"),
                    ("Лимон", "0.02"),
                    ("Оливковое масло", "0.02"),
                    ("Соль", "0.01"),
                    ("Перец", "0.01"),
                ],
            },
            {
                "name": "Котлета по-киевски",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.30",
                "min_batch_qty": "6",
                "batch_multiple_qty": "2",
                "daily_capacity": "130",
                "default_price": "640.00",
                "ingredients": [
                    ("Куриное филе", "0.20"),
                    ("Масло сливочное", "0.03"),
                    ("Панировка", "0.04"),
                    ("Яйцо", "0.02"),
                    ("Зелень", "0.01"),
                ],
            },
            {
                "name": "Оливье",
                "unit": "кг",
                "base_uom": "kg",
                "quantity_scale": "3",
                "unit_weight_kg": "1.00",
                "min_batch_qty": "3",
                "batch_multiple_qty": "1",
                "daily_capacity": "150",
                "default_price": "900.00",
                "ingredients": [
                    ("Картофель", "0.25"),
                    ("Морковь", "0.10"),
                    ("Горошек", "0.10"),
                    ("Колбаса", "0.20"),
                    ("Майонез", "0.15"),
                ],
            },
            {
                "name": "Плов с курицей",
                "unit": "кг",
                "base_uom": "kg",
                "quantity_scale": "3",
                "unit_weight_kg": "1.00",
                "min_batch_qty": "5",
                "batch_multiple_qty": "1",
                "daily_capacity": "160",
                "default_price": "820.00",
                "ingredients": [
                    ("Рис", "0.50"),
                    ("Курица", "0.30"),
                    ("Морковь", "0.10"),
                    ("Лук", "0.05"),
                    ("Специи", "0.05"),
                ],
            },
            {
                "name": "Блины с творогом",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.22",
                "min_batch_qty": "10",
                "batch_multiple_qty": "5",
                "daily_capacity": "220",
                "default_price": "260.00",
                "ingredients": [
                    ("Мука", "0.08"),
                    ("Молоко", "0.06"),
                    ("Творог", "0.05"),
                    ("Сахар", "0.02"),
                    ("Яйцо", "0.01"),
                ],
            },
        ]

        for data in dishes:
            dish, _ = Dish.objects.update_or_create(
                name=data["name"],
                defaults={
                "unit": data["unit"],
                "base_uom": data["base_uom"],
                "quantity_scale": int(data["quantity_scale"]),
                "is_active": True,
                "created_by": seed_user,
                "unit_weight_kg": Decimal(data["unit_weight_kg"]),
                "min_batch_qty": Decimal(data["min_batch_qty"]),
                "batch_multiple_qty": Decimal(data["batch_multiple_qty"]),
                "daily_capacity": Decimal(data["daily_capacity"]),
                "default_price": Decimal(data["default_price"]),
            },
        )

            tech_card, _ = TechCard.objects.update_or_create(
                dish=dish,
                version_label="1.0",
                defaults={
                    "description": f"Техкарта для блюда «{dish.name}».",
                    "photo_url": "",
                    "is_active": True,
                    "approved_by": seed_user,
                },
            )

            TechCardVariant.objects.update_or_create(
                tech_card=tech_card,
                quantity=Decimal("1.000"),
                defaults={"note": "Стандартная порция"},
            )

            for ingredient_name, qty in data["ingredients"]:
                ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
                TechCardComponent.objects.update_or_create(
                    tech_card=tech_card,
                    ingredient=ingredient,
                    defaults={"quantity": Decimal(qty), "note": ""},
                )

        self.stdout.write(self.style.SUCCESS("Блюда и техкарты успешно добавлены."))
