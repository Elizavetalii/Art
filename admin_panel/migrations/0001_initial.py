from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Backup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file_path", models.CharField(max_length=255, verbose_name="Файл")),
                ("status", models.CharField(choices=[("created", "Создан"), ("restored", "Восстановлен"), ("failed", "Ошибка")], default="created", max_length=20, verbose_name="Статус")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Создан")),
                ("created_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="BackupSchedule",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("frequency", models.CharField(choices=[("daily", "Ежедневно"), ("weekly", "Еженедельно"), ("monthly", "Ежемесячно")], default="weekly", max_length=20, verbose_name="Частота")),
                ("is_active", models.BooleanField(default=True, verbose_name="Активно")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Обновлено")),
            ],
        ),
    ]
