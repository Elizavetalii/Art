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
            name="Report",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Название отчёта")),
                ("period_from", models.DateField(verbose_name="Период с")),
                ("period_to", models.DateField(verbose_name="Период по")),
                ("status", models.CharField(choices=[("draft", "Черновик"), ("ready", "Готов"), ("error", "Ошибка"), ("validating", "Проверка")], default="draft", max_length=20, verbose_name="Статус")),
                ("file", models.FileField(blank=True, null=True, upload_to="reports/", verbose_name="Файл отчёта")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Создан")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Обновлён")),
                ("created_by", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
