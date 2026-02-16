from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0002_client_current_stage"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Создан", null=True),
        ),
    ]
