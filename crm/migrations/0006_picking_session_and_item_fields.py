from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0005_delivery_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="picked_quantity",
            field=models.DecimalField(default=0, decimal_places=3, max_digits=10, verbose_name="Собрано фактически"),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="item_status",
            field=models.CharField(
                choices=[
                    ("not_started", "Не начато"),
                    ("in_progress", "В сборке"),
                    ("done", "Собрано"),
                    ("out_of_stock", "Нет в наличии"),
                    ("replaced", "Заменено"),
                ],
                default="not_started",
                max_length=20,
                verbose_name="Статус позиции",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="item_comment",
            field=models.CharField(blank=True, max_length=255, verbose_name="Комментарий по позиции"),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="replacement_text",
            field=models.CharField(blank=True, max_length=255, verbose_name="Замена"),
        ),
        migrations.CreateModel(
            name="PickingSession",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("note", models.TextField(blank=True, verbose_name="Примечание сборщика")),
                ("started_at", models.DateTimeField(blank=True, null=True, verbose_name="Начата")),
                ("finished_at", models.DateTimeField(blank=True, null=True, verbose_name="Завершена")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Обновлено")),
                ("order", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="picking_session", to="crm.order")),
                ("picker", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="picking_sessions", to="crm.user")),
            ],
            options={
                "verbose_name": "Сборка заказа",
                "verbose_name_plural": "Сборки заказов",
            },
        ),
    ]
