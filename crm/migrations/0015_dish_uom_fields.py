from django.db import migrations, models


def set_dish_uom(apps, schema_editor):
    Dish = apps.get_model("crm", "Dish")
    for dish in Dish.objects.all():
        unit = (dish.unit or "").lower()
        if "кг" in unit or "kg" in unit:
            dish.base_uom = "kg"
            dish.quantity_scale = 3
        else:
            dish.base_uom = "pcs"
            dish.quantity_scale = 0
        dish.save(update_fields=["base_uom", "quantity_scale"])


class Migration(migrations.Migration):
    dependencies = [
        ("crm", "0014_dish_default_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="base_uom",
            field=models.CharField(choices=[("kg", "кг"), ("pcs", "шт")], default="pcs", max_length=8, verbose_name="Базовая единица"),
        ),
        migrations.AddField(
            model_name="dish",
            name="quantity_scale",
            field=models.PositiveSmallIntegerField(default=0, verbose_name="Знаков после запятой"),
        ),
        migrations.RunPython(set_dish_uom, migrations.RunPython.noop),
    ]
