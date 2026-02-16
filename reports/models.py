from django.db import models
from django.conf import settings


class Report(models.Model):
    STATUS_CHOICES = [
        ("draft", "Черновик"),
        ("ready", "Готов"),
        ("error", "Ошибка"),
        ("validating", "Проверка"),
    ]
    VALIDATION_CHOICES = [
        ("ok", "Без ошибок"),
        ("warn", "Предупреждение"),
        ("error", "Ошибка"),
    ]

    title = models.CharField("Название отчёта", max_length=200)
    period_from = models.DateField("Период с")
    period_to = models.DateField("Период по")
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="draft")
    validation_status = models.CharField("Проверка", max_length=20, choices=VALIDATION_CHOICES, default="warn")
    validation_message = models.TextField("Результат проверки", blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField("Файл отчёта", upload_to="reports/", null=True, blank=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)
    updated_at = models.DateTimeField("Обновлён", auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
