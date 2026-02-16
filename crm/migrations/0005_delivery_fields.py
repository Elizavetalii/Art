from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0004_order_archived"),
    ]

    operations = [
        migrations.AddField(
            model_name="courier",
            name="zone",
            field=models.CharField(blank=True, max_length=128, verbose_name="Зона"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="planned_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Плановая дата/время"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="route",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="deliveries",
                to="crm.route",
            ),
        ),
        migrations.AddField(
            model_name="delivery",
            name="status",
            field=models.CharField(
                choices=[
                    ("unassigned", "Не назначено"),
                    ("planned", "Запланировано"),
                    ("on_route", "В пути"),
                    ("delivered", "Доставлено"),
                    ("cancelled", "Отмена"),
                ],
                default="unassigned",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
    ]
