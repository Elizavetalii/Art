from django.contrib.auth import get_user_model
from crm.models import Role, UserRole

User = get_user_model()
users = [
    ('manager_demo','Менеджер','ManagerDemo123!'),
    ('logistic_demo','Логист','LogisticDemo123!'),
    ('picker_demo','Сборщик заказов','PickerDemo123!'),
    ('admin_demo','Администратор системы','AdminDemo123!'),
]
for username, role_name, pwd in users:
    u, created = User.objects.get_or_create(username=username, defaults={
        'email': f'{username}@example.com',
        'full_name': role_name,
        'is_active': True,
    })
    u.set_password(pwd)
    u.save()
    role, _ = Role.objects.get_or_create(name=role_name)
    UserRole.objects.get_or_create(user=u, role=role)
    print(f"{username} / {pwd} (role {role_name}) created={created}")
