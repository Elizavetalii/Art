def role_flags(request):
    if not hasattr(request, "user") or not request.user.is_authenticated:
        return {}
    roles = set(request.user.roles.values_list("name", flat=True))
    return {
        "is_manager": "Менеджер" in roles,
        "is_logistic": "Логист" in roles,
        "is_picker": "Сборщик заказов" in roles,
        "is_admin": "Администратор системы" in roles,
        "is_courier": "Курьер" in roles,
    }
