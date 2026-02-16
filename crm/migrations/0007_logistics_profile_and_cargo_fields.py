from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0006_picking_session_and_item_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogisticianProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("region", models.CharField(blank=True, max_length=128, verbose_name="Регион")),
                ("city", models.CharField(blank=True, max_length=128, verbose_name="Город")),
                ("transport_types", models.JSONField(blank=True, default=list, verbose_name="Доступные типы транспорта")),
                ("timezone", models.CharField(default="UTC", max_length=64, verbose_name="Часовой пояс")),
                ("map_show_traffic", models.BooleanField(default=True, verbose_name="Показывать пробки")),
                (
                    "preferred_route_type",
                    models.CharField(
                        choices=[("fast", "Быстрый"), ("safe", "Безопасный"), ("economic", "Экономичный")],
                        default="fast",
                        max_length=16,
                        verbose_name="Предпочтительный тип маршрута",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="logistic_profile", to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name": "Профиль логиста",
                "verbose_name_plural": "Профили логистов",
            },
        ),
        migrations.AddField(
            model_name="courier",
            name="payload_capacity_kg",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Грузоподъёмность (кг)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_volume_m3",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Объём кузова (м³)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_length_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Длина кузова (см)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_width_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Ширина кузова (см)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_height_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Высота кузова (см)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="current_lat",
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name="Текущая широта"),
        ),
        migrations.AddField(
            model_name="courier",
            name="current_lng",
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name="Текущая долгота"),
        ),
        migrations.AddField(
            model_name="courier",
            name="location_updated_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Обновление геолокации"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_weight_kg",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Вес груза (кг)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_volume_m3",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Объём груза (м³)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_length_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Длина груза (см)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_width_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Ширина груза (см)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_height_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Высота груза (см)"),
        ),
    ]
