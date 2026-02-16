from django.db import migrations, models


def migrate_courier_status(apps, schema_editor):
    Courier = apps.get_model("crm", "Courier")
    status_map = {
        "active": "free",
        "on_route": "busy",
        "inactive": "offline",
    }
    for old, new in status_map.items():
        Courier.objects.filter(status=old).update(status=new)


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0007_logistics_profile_and_cargo_fields"),
    ]

    operations = [
        migrations.RunPython(migrate_courier_status, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="courier",
            name="status",
            field=models.CharField(
                choices=[("free", "Свободен"), ("busy", "Занят"), ("offline", "Оффлайн")],
                default="free",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="logisticianprofile",
            name="preferred_route_type",
            field=models.CharField(
                choices=[("fastest", "Самый быстрый"), ("safest", "Самый безопасный"), ("shortest", "Самый короткий")],
                default="fastest",
                max_length=16,
                verbose_name="Предпочтительный тип маршрута",
            ),
        ),
    ]
