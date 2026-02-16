from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0003_client_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="is_archived",
            field=models.BooleanField(default=False, verbose_name="В архиве"),
        ),
    ]
