from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="validation_status",
            field=models.CharField(choices=[("ok", "Без ошибок"), ("warn", "Предупреждение"), ("error", "Ошибка")], default="warn", max_length=20, verbose_name="Проверка"),
        ),
        migrations.AddField(
            model_name="report",
            name="validation_message",
            field=models.TextField(blank=True, verbose_name="Результат проверки"),
        ),
    ]
