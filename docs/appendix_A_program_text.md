ПРИЛОЖЕНИЕ А. ТЕКСТ ПРОГРАММЫ

АННОТАЦИЯ
В данном программном документе приведен текст программы для поддержания работы web-приложения «LumiereSecrete».
В данном программном документе, в разделе «Тест программы», указана информация о информационной системе, области применения программы, модулей программы и код каждого программного модуля.

1. МОДУЛИ ИНФОРМАЦИОННОЙ СИСТЕМЫ
В Таблице 1 представлено описание всех классов и модулей программы, количество строк верстки или кода и размер файла.

Таблица 1 - Модули программы

| № | Модуль | Описание | Строк | Размер (КБ) |
|---:|---|---|---:|---:|
| 1 | `manage.py` | Точка входа Django‑проекта, запуск команд и сервера | 18 | 0.5 |
| 2 | `factory_crm/__init__.py` | Маркер пакета factory_crm | 1 | 0.0 |
| 3 | `factory_crm/asgi.py` | ASGI‑конфигурация для асинхронного запуска | 5 | 0.2 |
| 4 | `factory_crm/settings.py` | Центральные настройки проекта (БД, приложения, безопасность) | 179 | 6.1 |
| 5 | `factory_crm/urls.py` | Маршрутизация URL и привязка обработчиков | 50 | 2.4 |
| 6 | `factory_crm/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 79 | 2.7 |
| 7 | `factory_crm/wsgi.py` | WSGI‑конфигурация для production‑запуска | 5 | 0.2 |
| 8 | `crm/__init__.py` | Маркер пакета crm | 1 | 0.0 |
| 9 | `crm/admin.py` | Регистрация сущностей в админ‑интерфейсе | 91 | 2.7 |
| 10 | `crm/admin_site.py` | Служебный файл проекта | 74 | 2.4 |
| 11 | `crm/api.py` | API‑логика и служебные endpoint‑обработчики | 305 | 9.0 |
| 12 | `crm/apps.py` | Конфигурация приложения Django | 7 | 0.2 |
| 13 | `crm/forms.py` | Формы ввода, валидация и обработка полей | 14 | 0.5 |
| 14 | `crm/management/commands/seed_dishes.py` | Служебный файл проекта | 239 | 9.1 |
| 15 | `crm/management/commands/seed_logistics.py` | Служебный файл проекта | 170 | 6.8 |
| 16 | `crm/models.py` | Описание моделей и структуры данных модуля | 665 | 32.5 |
| 17 | `accounts/__init__.py` | Маркер пакета accounts | 0 | 0.0 |
| 18 | `accounts/admin.py` | Регистрация сущностей в админ‑интерфейсе | 3 | 0.1 |
| 19 | `accounts/apps.py` | Конфигурация приложения Django | 5 | 0.1 |
| 20 | `accounts/context_processors.py` | Передача данных ролей/состояния в шаблоны | 11 | 0.5 |
| 21 | `accounts/management/__init__.py` | Маркер пакета accounts | 1 | 0.0 |
| 22 | `accounts/management/commands/__init__.py` | Маркер пакета accounts | 1 | 0.0 |
| 23 | `accounts/management/commands/seed_demo.py` | Служебный файл проекта | 158 | 5.7 |
| 24 | `accounts/models.py` | Описание моделей и структуры данных модуля | 3 | 0.1 |
| 25 | `accounts/tests.py` | Автоматизированные тесты модуля | 3 | 0.1 |
| 26 | `accounts/urls.py` | Маршрутизация URL и привязка обработчиков | 26 | 1.2 |
| 27 | `accounts/utils.py` | Вспомогательные функции и сервисные утилиты | 28 | 0.9 |
| 28 | `accounts/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 68 | 2.6 |
| 29 | `clients/__init__.py` | Маркер пакета clients | 0 | 0.0 |
| 30 | `clients/admin.py` | Регистрация сущностей в админ‑интерфейсе | 3 | 0.1 |
| 31 | `clients/apps.py` | Конфигурация приложения Django | 5 | 0.1 |
| 32 | `clients/forms.py` | Формы ввода, валидация и обработка полей | 60 | 1.8 |
| 33 | `clients/models.py` | Описание моделей и структуры данных модуля | 3 | 0.1 |
| 34 | `clients/tests.py` | Автоматизированные тесты модуля | 3 | 0.1 |
| 35 | `clients/urls.py` | Маршрутизация URL и привязка обработчиков | 10 | 0.4 |
| 36 | `clients/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 117 | 4.9 |
| 37 | `orders/__init__.py` | Маркер пакета orders | 0 | 0.0 |
| 38 | `orders/admin.py` | Регистрация сущностей в админ‑интерфейсе | 3 | 0.1 |
| 39 | `orders/apps.py` | Конфигурация приложения Django | 5 | 0.1 |
| 40 | `orders/forms.py` | Формы ввода, валидация и обработка полей | 186 | 7.9 |
| 41 | `orders/models.py` | Описание моделей и структуры данных модуля | 3 | 0.1 |
| 42 | `orders/tests.py` | Автоматизированные тесты модуля | 121 | 4.4 |
| 43 | `orders/urls.py` | Маршрутизация URL и привязка обработчиков | 26 | 0.9 |
| 44 | `orders/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 664 | 29.7 |
| 45 | `logistics/__init__.py` | Маркер пакета logistics | 0 | 0.0 |
| 46 | `logistics/admin.py` | Регистрация сущностей в админ‑интерфейсе | 3 | 0.1 |
| 47 | `logistics/apps.py` | Конфигурация приложения Django | 5 | 0.1 |
| 48 | `logistics/forms.py` | Формы ввода, валидация и обработка полей | 249 | 9.7 |
| 49 | `logistics/models.py` | Описание моделей и структуры данных модуля | 3 | 0.1 |
| 50 | `logistics/tests.py` | Автоматизированные тесты модуля | 116 | 4.2 |
| 51 | `logistics/urls.py` | Маршрутизация URL и привязка обработчиков | 40 | 1.7 |
| 52 | `logistics/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 690 | 28.9 |
| 53 | `reports/__init__.py` | Маркер пакета reports | 0 | 0.0 |
| 54 | `reports/admin.py` | Регистрация сущностей в админ‑интерфейсе | 3 | 0.1 |
| 55 | `reports/apps.py` | Конфигурация приложения Django | 5 | 0.1 |
| 56 | `reports/forms.py` | Формы ввода, валидация и обработка полей | 17 | 0.5 |
| 57 | `reports/models.py` | Описание моделей и структуры данных модуля | 32 | 1.3 |
| 58 | `reports/tests.py` | Автоматизированные тесты модуля | 3 | 0.1 |
| 59 | `reports/urls.py` | Маршрутизация URL и привязка обработчиков | 10 | 0.4 |
| 60 | `reports/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 154 | 5.6 |
| 61 | `admin_panel/__init__.py` | Маркер пакета admin_panel | 0 | 0.0 |
| 62 | `admin_panel/admin.py` | Регистрация сущностей в админ‑интерфейсе | 3 | 0.1 |
| 63 | `admin_panel/apps.py` | Конфигурация приложения Django | 5 | 0.1 |
| 64 | `admin_panel/entity_config.py` | Конфигурация универсальных сущностей админ‑панели | 320 | 12.0 |
| 65 | `admin_panel/forms.py` | Формы ввода, валидация и обработка полей | 82 | 2.8 |
| 66 | `admin_panel/models.py` | Описание моделей и структуры данных модуля | 33 | 1.2 |
| 67 | `admin_panel/tests.py` | Автоматизированные тесты модуля | 3 | 0.1 |
| 68 | `admin_panel/urls.py` | Маршрутизация URL и привязка обработчиков | 46 | 1.8 |
| 69 | `admin_panel/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 545 | 22.6 |
| 70 | `dashboard/__init__.py` | Маркер пакета dashboard | 0 | 0.0 |
| 71 | `dashboard/admin.py` | Регистрация сущностей в админ‑интерфейсе | 3 | 0.1 |
| 72 | `dashboard/apps.py` | Конфигурация приложения Django | 5 | 0.1 |
| 73 | `dashboard/models.py` | Описание моделей и структуры данных модуля | 3 | 0.1 |
| 74 | `dashboard/tests.py` | Автоматизированные тесты модуля | 3 | 0.1 |
| 75 | `dashboard/urls.py` | Маршрутизация URL и привязка обработчиков | 9 | 0.4 |
| 76 | `dashboard/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 99 | 3.6 |
| 77 | `portal/__init__.py` | Маркер пакета portal | 1 | 0.1 |
| 78 | `portal/forms.py` | Формы ввода, валидация и обработка полей | 70 | 2.0 |
| 79 | `portal/urls.py` | Маршрутизация URL и привязка обработчиков | 19 | 1.1 |
| 80 | `portal/utils.py` | Вспомогательные функции и сервисные утилиты | 34 | 1.1 |
| 81 | `portal/views.py` | Контроллеры и бизнес‑логика пользовательских сценариев | 155 | 5.9 |
| 82 | `templates/accounts/login.html` | HTML‑шаблон пользовательского интерфейса | 26 | 1.0 |
| 83 | `templates/accounts/login_base.html` | HTML‑шаблон пользовательского интерфейса | 52 | 1.9 |
| 84 | `templates/accounts/password_reset_complete.html` | HTML‑шаблон пользовательского интерфейса | 6 | 0.3 |
| 85 | `templates/accounts/password_reset_confirm.html` | HTML‑шаблон пользовательского интерфейса | 20 | 0.7 |
| 86 | `templates/accounts/password_reset_done.html` | HTML‑шаблон пользовательского интерфейса | 8 | 0.4 |
| 87 | `templates/accounts/password_reset_email.html` | HTML‑шаблон пользовательского интерфейса | 8 | 0.4 |
| 88 | `templates/accounts/password_reset_form.html` | HTML‑шаблон пользовательского интерфейса | 17 | 0.7 |
| 89 | `templates/accounts/password_reset_subject.txt` | Текстовый служебный шаблон | 1 | 0.0 |
| 90 | `templates/admin/base_site.html` | HTML‑шаблон пользовательского интерфейса | 78 | 2.8 |
| 91 | `templates/admin/index.html` | HTML‑шаблон пользовательского интерфейса | 30 | 1.0 |
| 92 | `templates/admin_panel/access.html` | HTML‑шаблон пользовательского интерфейса | 42 | 1.2 |
| 93 | `templates/admin_panel/backup_schedule.html` | HTML‑шаблон пользовательского интерфейса | 31 | 1.0 |
| 94 | `templates/admin_panel/backups.html` | HTML‑шаблон пользовательского интерфейса | 66 | 2.4 |
| 95 | `templates/admin_panel/data_check.html` | HTML‑шаблон пользовательского интерфейса | 50 | 1.7 |
| 96 | `templates/admin_panel/entities/delete.html` | HTML‑шаблон пользовательского интерфейса | 38 | 1.5 |
| 97 | `templates/admin_panel/entities/detail.html` | HTML‑шаблон пользовательского интерфейса | 69 | 2.4 |
| 98 | `templates/admin_panel/entities/form.html` | HTML‑шаблон пользовательского интерфейса | 52 | 2.1 |

2. ТЕКСТ ПРОГРАММНЫХ МОДУЛЕЙ

1. manage.py
```python
#!/usr/bin/env python3
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factory_crm.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it is installed and available on your PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
```

2. factory_crm/__init__.py
```python
# Factory CRM project package
```

3. factory_crm/asgi.py
```python
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factory_crm.settings')
application = get_asgi_application()
```

4. factory_crm/settings.py
```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'insecure-secret-key-change-me')
DEBUG = os.environ.get('DJANGO_DEBUG', 'true').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'drf_spectacular',
    'crm',
    'accounts',
    'clients',
    'orders',
    'logistics',
    'reports',
    'dashboard',
    'admin_panel',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'factory_crm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.role_flags',
            ],
        },
    },
]

WSGI_APPLICATION = 'factory_crm.wsgi.application'
ASGI_APPLICATION = 'factory_crm.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DB_NAME', BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
        'ATOMIC_REQUESTS': True,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY', '')

LOGISTICS_DEPOT_ADDRESS = os.environ.get('LOGISTICS_DEPOT_ADDRESS', 'Химки')
LOGISTICS_DEPOT_LAT = float(os.environ.get('LOGISTICS_DEPOT_LAT', '55.886'))
LOGISTICS_DEPOT_LNG = float(os.environ.get('LOGISTICS_DEPOT_LNG', '37.442'))
LOGISTICS_AVG_SPEED_KMH = int(os.environ.get('LOGISTICS_AVG_SPEED_KMH', '35'))
LOGISTICS_RETURN_TO_DEPOT = os.environ.get('LOGISTICS_RETURN_TO_DEPOT', 'true').lower() == 'true'
LOGISTICS_SERVICE_TIME_MINUTES = int(os.environ.get('LOGISTICS_SERVICE_TIME_MINUTES', '15'))
LOGISTICS_ALLOWED_PROOF_EXT = ['.pdf', '.jpg', '.jpeg', '.png']

ORDER_CUTOFF_TIME = "16:00"
ORDER_MORNING_CUTOFF_TIME = "10:00"
PRODUCTION_WINDOW_DAY_START = "06:00"
PRODUCTION_WINDOW_DAY_END = "18:00"
PRODUCTION_WINDOW_NIGHT_START = "22:00"
PRODUCTION_WINDOW_NIGHT_END = "06:00"
PRODUCTION_MAX_WEIGHT_KG = 500

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'crm.User'

# Email settings (configured via environment; defaults for mail.ru sender)
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.mail.ru')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '465'))
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL', 'true').lower() == 'true'
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'false').lower() == 'true'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'art-culinary@mail.ru')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'Z4rfpjW3dUfJPbzQebIB')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'

THROTTLE_ENABLED = os.environ.get('DJANGO_THROTTLE', 'true').lower() == 'true'
if DEBUG and os.environ.get('DJANGO_THROTTLE') is None:
    THROTTLE_ENABLED = False

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/day',
        'anon': '100/day',
    },
}

if not THROTTLE_ENABLED:
    REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] = []
    REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Art Culinary CRM API',
    'DESCRIPTION': 'REST API для продаж, заказов, логистики и техкарт.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': True,
}

# CORS — dev-режим (ограничьте в проде)
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
```

5. factory_crm/urls.py
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

from crm import api
from orders import views as order_views

router = DefaultRouter()
router.register(r"roles", api.RoleViewSet)
router.register(r"users", api.UserViewSet)
router.register(r"clients", api.ClientViewSet)
router.register(r"client-contacts", api.ClientContactViewSet)
router.register(r"orders", api.OrderViewSet)
router.register(r"order-items", api.OrderItemViewSet)
router.register(r"interactions", api.InteractionViewSet)
router.register(r"stages", api.CooperationStageViewSet)
router.register(r"stage-history", api.ClientStageHistoryViewSet)
router.register(r"ingredients", api.IngredientViewSet)
router.register(r"dishes", api.DishViewSet)
router.register(r"techcards", api.TechCardViewSet)
router.register(r"techcard-components", api.TechCardComponentViewSet)
router.register(r"techcard-variants", api.TechCardVariantViewSet)
router.register(r"couriers", api.CourierViewSet)
router.register(r"deliveries", api.DeliveryViewSet)
router.register(r"routes", api.RouteViewSet)
router.register(r"courier-assignments", api.CourierAssignmentViewSet)
router.register(r"route-stops", api.RouteStopViewSet)

urlpatterns = [
    path("", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("clients/", include("clients.urls")),
    path("orders/", include("orders.urls")),
    path("logistics/", include("logistics.urls")),
    path("reports/", include("reports.urls")),
    path("admin-panel/", include("admin_panel.urls")),
    path("api/orders/availability/", order_views.order_availability, name="order-availability"),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

6. factory_crm/views.py
```python
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from crm.forms import ClientForm, OrderForm
from crm.models import Client, Order


def is_manager(user):
    return user.is_authenticated and user.roles.filter(name__iexact="Менеджер").exists()


class ManagerLoginView(LoginView):
    template_name = "login_root.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if is_manager(user):
            return "/manager/"
        if user.is_staff:
            return "/admin/"
        return "/"

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.request.user
        if is_manager(user) or user.is_staff:
            return response
        logout(self.request)
        form.add_error(None, _("У вас нет прав для входа. Обратитесь к администратору."))
        return self.form_invalid(form)


def manager_dashboard_view(request, *args, **kwargs):
    # protected view wrapper
    from django.views.generic import TemplateView

    protected_view = login_required(
        user_passes_test(is_manager)(TemplateView.as_view(template_name="manager_dashboard.html")),
        login_url='/'
    )
    return protected_view(request, *args, **kwargs)


@login_required(login_url='/')
@user_passes_test(is_manager, login_url='/')
def manager_clients_view(request):
    clients = Client.objects.all().select_related('responsible_manager')
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            if not client.responsible_manager:
                client.responsible_manager = request.user
            client.save()
            return redirect('/manager/clients/')
    else:
        form = ClientForm()
    return render(request, 'manager_clients.html', {'clients': clients, 'form': form})


@login_required(login_url='/')
@user_passes_test(is_manager, login_url='/')
def manager_orders_view(request):
    orders = Order.objects.select_related('client', 'manager').all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if not order.manager:
                order.manager = request.user
            order.save()
            return redirect('/manager/orders/')
    else:
        form = OrderForm()
    return render(request, 'manager_orders.html', {'orders': orders, 'form': form})
```

7. factory_crm/wsgi.py
```python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factory_crm.settings')
application = get_wsgi_application()
```

8. crm/__init__.py
```python
# CRM app package
```

9. crm/admin.py
```python
from django.contrib import admin
from . import models
from .admin_site import admin_site


class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "is_active")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("is_active",)


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "client_type", "status", "responsible_manager")
    search_fields = ("name", "inn", "kpp", "email", "phone")
    list_filter = ("status", "client_type")


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "client", "status", "total_amount", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("order_number", "client__name")
    inlines = [OrderItemInline]


class LogisticianProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "region", "city", "timezone", "preferred_route_type", "map_show_traffic")
    search_fields = ("user__full_name", "region", "city")


class CourierAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "status",
        "transport_type",
        "payload_capacity_kg",
        "cargo_volume_m3",
        "max_weight",
        "max_volume",
        "zone",
    )
    list_filter = ("status", "transport_type", "zone")
    search_fields = ("user__full_name", "user__phone", "zone")


_registry = [
    (models.Role, RoleAdmin),
    (models.User, UserAdmin),
    (models.UserRole, None),
    (models.Client, ClientAdmin),
    (models.ClientContact, None),
    (models.CooperationStage, None),
    (models.ClientStageHistory, None),
    (models.Interaction, None),
    (models.Dish, None),
    (models.TechCard, None),
    (models.TechCardVariant, None),
    (models.TechCardComponent, None),
    (models.Ingredient, None),
    (models.Equipment, None),
    (models.DishEquipmentRequirement, None),
    (models.ClientAllowedTechCard, None),
    (models.IngredientStock, None),
    (models.ProductionReservation, None),
    (models.IngredientReservation, None),
    (models.EquipmentReservation, None),
    (models.Order, OrderAdmin),
    (models.OrderItem, None),
    (models.Delivery, None),
    (models.Route, None),
    (models.RouteStop, None),
    (models.LogisticianProfile, LogisticianProfileAdmin),
    (models.Courier, CourierAdmin),
    (models.CourierAssignment, None),
    (models.AuditLog, None),
]

# Регистрируем модели в кастомном админ-сайте
for model, admin_class in _registry:
    if admin_class:
        admin_site.register(model, admin_class)
    else:
        admin_site.register(model)
```

10. crm/admin_site.py
```python
from collections import defaultdict

from django.contrib import admin

from . import models


class FactoryAdminSite(admin.AdminSite):
    site_header = "Art Culinary CRM"
    site_title = "Администрирование"
    index_title = "Панель управления"
    enable_nav_sidebar = True

    # Человеческие категории для меню
    CATEGORY_MAP = {
        "Продажи": [
            models.Client,
            models.ClientContact,
            models.CooperationStage,
            models.ClientStageHistory,
            models.Interaction,
        ],
        "Заказы": [
            models.Order,
            models.OrderItem,
        ],
        "Каталог и техкарты": [
            models.Dish,
            models.TechCard,
            models.TechCardVariant,
            models.TechCardComponent,
            models.Ingredient,
        ],
        "Логистика": [
            models.Delivery,
            models.Route,
            models.RouteStop,
            models.Courier,
            models.CourierAssignment,
        ],
        "Система": [
            models.Role,
            models.User,
            models.UserRole,
        ],
    }

    def index(self, request, extra_context=None):
        app_list = self.get_app_list(request)
        categorized = defaultdict(list)

        # Преобразуем стандартный app_list в наш порядок по CATEGORY_MAP
        model_index = {m._meta.model_name: m for models_ in self.CATEGORY_MAP.values() for m in models_}

        for app in app_list:
            for model in app.get("models", []):
                model_cls = model_index.get(model["object_name"].lower())
                if not model_cls:
                    continue
                for cat, model_list in self.CATEGORY_MAP.items():
                    if model_cls in model_list:
                        categorized[cat].append(model)
                        break

        # сохраняем порядок категорий как в словаре
        ordered_categories = [(cat, categorized.get(cat, [])) for cat in self.CATEGORY_MAP.keys()]

        context = {"categorized_list": ordered_categories, "title": self.index_title}
        if extra_context:
            context.update(extra_context)
        return super().index(request, extra_context=context)


admin_site = FactoryAdminSite(name="factory_admin")
```

11. crm/api.py
```python
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models


# ---------- Serializers ----------
from rest_framework import serializers  # noqa: E402


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = ['id', 'username', 'full_name', 'email', 'phone', 'roles', 'is_active', 'is_staff']


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientContact
        fields = ['id', 'client', 'full_name', 'position', 'phone', 'email', 'is_primary']


class ClientSerializer(serializers.ModelSerializer):
    contacts = ClientContactSerializer(many=True, read_only=True)

    class Meta:
        model = models.Client
        fields = ['id', 'name', 'client_type', 'inn', 'kpp', 'default_delivery_address', 'email', 'phone', 'status', 'current_stage', 'responsible_manager', 'created_at', 'contacts']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = ['id', 'name', 'is_active']


class TechCardComponentSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(source='ingredient', queryset=models.Ingredient.objects.all(), write_only=True)

    class Meta:
        model = models.TechCardComponent
        fields = ['id', 'tech_card', 'ingredient', 'ingredient_id', 'quantity', 'note']


class TechCardVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TechCardVariant
        fields = ['id', 'tech_card', 'quantity', 'note']


class TechCardSerializer(serializers.ModelSerializer):
    components = TechCardComponentSerializer(many=True, read_only=True)
    variants = TechCardVariantSerializer(many=True, read_only=True)

    class Meta:
        model = models.TechCard
        fields = ['id', 'dish', 'version_label', 'description', 'photo_url', 'is_active', 'approved_by', 'components', 'variants']


class DishSerializer(serializers.ModelSerializer):
    tech_cards = TechCardSerializer(many=True, read_only=True)

    class Meta:
        model = models.Dish
        fields = ['id', 'name', 'unit', 'is_active', 'tech_cards']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItem
        fields = ['id', 'order', 'dish', 'ingredient', 'custom_tech_card', 'quantity', 'unit_price', 'line_total', 'supply_type']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = models.Order
        fields = ['id', 'order_number', 'client', 'manager', 'address', 'status', 'comments', 'total_amount', 'is_archived', 'created_at', 'updated_at', 'items']


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Interaction
        fields = ['id', 'client', 'manager', 'interaction_type', 'note', 'happened_at']


class CooperationStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CooperationStage
        fields = ['id', 'name', 'order', 'is_active']


class ClientStageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientStageHistory
        fields = ['id', 'client', 'stage', 'changed_by', 'changed_at', 'comment']


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Courier
        fields = [
            'id',
            'user',
            'transport_type',
            'payload_capacity_kg',
            'cargo_volume_m3',
            'cargo_length_cm',
            'cargo_width_cm',
            'cargo_height_cm',
            'current_lat',
            'current_lng',
            'max_weight',
            'max_volume',
            'current_latitude',
            'current_longitude',
            'location_updated_at',
            'experience_years',
            'status',
            'zone',
        ]


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Delivery
        fields = [
            'id',
            'order',
            'courier',
            'route',
            'status',
            'planned_at',
            'departure_time',
            'delivered_at',
            'address',
            'cargo_weight_kg',
            'cargo_volume_m3',
            'cargo_length_cm',
            'cargo_width_cm',
            'cargo_height_cm',
            'note',
            'is_sent',
        ]


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Route
        fields = ['id', 'logistician', 'planned_date', 'status', 'notes']


class CourierAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourierAssignment
        fields = ['id', 'courier', 'route', 'assigned_at']


class RouteStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RouteStop
        fields = [
            'id',
            'route',
            'delivery',
            'sequence_index',
            'planned_time',
            'actual_time',
            'note',
            'status',
            'latitude',
            'longitude',
            'delivery_date',
            'service_time_minutes',
            'failure_reason',
            'proof_of_delivery',
            'proof_uploaded_at',
            'proof_uploaded_by',
        ]


# ---------- ViewSets ----------

class BaseAuthViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


class RoleViewSet(BaseAuthViewSet):
    queryset = models.Role.objects.all()
    serializer_class = RoleSerializer


class UserViewSet(BaseAuthViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(BaseAuthViewSet):
    queryset = models.Client.objects.all()
    serializer_class = ClientSerializer
    search_fields = ['name', 'inn', 'kpp', 'email', 'phone']
    filterset_fields = ['client_type', 'status', 'responsible_manager']
    ordering_fields = ['name', 'status']


class ClientContactViewSet(BaseAuthViewSet):
    queryset = models.ClientContact.objects.all()
    serializer_class = ClientContactSerializer


class InteractionViewSet(BaseAuthViewSet):
    queryset = models.Interaction.objects.all()
    serializer_class = InteractionSerializer
    filterset_fields = ['client', 'manager', 'interaction_type']
    ordering_fields = ['happened_at']


class CooperationStageViewSet(BaseAuthViewSet):
    queryset = models.CooperationStage.objects.all()
    serializer_class = CooperationStageSerializer


class ClientStageHistoryViewSet(BaseAuthViewSet):
    queryset = models.ClientStageHistory.objects.all()
    serializer_class = ClientStageHistorySerializer


class IngredientViewSet(BaseAuthViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = IngredientSerializer


class DishViewSet(BaseAuthViewSet):
    queryset = models.Dish.objects.all()
    serializer_class = DishSerializer


class TechCardViewSet(BaseAuthViewSet):
    queryset = models.TechCard.objects.all()
    serializer_class = TechCardSerializer


class TechCardComponentViewSet(BaseAuthViewSet):
    queryset = models.TechCardComponent.objects.all()
    serializer_class = TechCardComponentSerializer


class TechCardVariantViewSet(BaseAuthViewSet):
    queryset = models.TechCardVariant.objects.all()
    serializer_class = TechCardVariantSerializer


class OrderViewSet(BaseAuthViewSet):
    queryset = models.Order.objects.select_related('client', 'manager').prefetch_related('items').all()
    serializer_class = OrderSerializer
    filterset_fields = ['status', 'client', 'manager']
    search_fields = ['order_number', 'client__name']
    ordering_fields = ['created_at', 'status', 'total_amount']

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        order = self.get_object()
        data = OrderItemSerializer(order.items.all(), many=True).data
        return Response(data)


class OrderItemViewSet(BaseAuthViewSet):
    queryset = models.OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class CourierViewSet(BaseAuthViewSet):
    queryset = models.Courier.objects.all()
    serializer_class = CourierSerializer


class DeliveryViewSet(BaseAuthViewSet):
    queryset = models.Delivery.objects.all()
    serializer_class = DeliverySerializer


class RouteViewSet(BaseAuthViewSet):
    queryset = models.Route.objects.all()
    serializer_class = RouteSerializer


class CourierAssignmentViewSet(BaseAuthViewSet):
    queryset = models.CourierAssignment.objects.all()
    serializer_class = CourierAssignmentSerializer


class RouteStopViewSet(BaseAuthViewSet):
    queryset = models.RouteStop.objects.all()
    serializer_class = RouteStopSerializer
```

12. crm/apps.py
```python
from django.apps import AppConfig


class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'
    verbose_name = 'CRM'
```

13. crm/forms.py
```python
from django import forms


class BootstrapFormMixin:
    def _init_bootstrap(self):
        for field in self.fields.values():
            widget = field.widget
            if isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault("class", "form-check-input")
                continue
            if isinstance(widget, (forms.Select, forms.SelectMultiple)):
                widget.attrs.setdefault("class", "form-select")
                continue
            widget.attrs.setdefault("class", "form-control")
```

14. crm/management/commands/seed_dishes.py
```python
from decimal import Decimal

from django.core.management.base import BaseCommand

from crm.models import Dish, Ingredient, TechCard, TechCardComponent, TechCardVariant, User


class Command(BaseCommand):
    help = "Создаёт 10 блюд с техкартами и составом."

    def handle(self, *args, **options):
        seed_user = User.objects.filter(is_superuser=True).first() or User.objects.first()

        dishes = [
            {
                "name": "Салат Цезарь",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.25",
                "min_batch_qty": "5",
                "batch_multiple_qty": "1",
                "daily_capacity": "120",
                "default_price": "450.00",
                "ingredients": [
                    ("Курица", "0.08"),
                    ("Салат ромэн", "0.06"),
                    ("Пармезан", "0.02"),
                    ("Соус цезарь", "0.03"),
                    ("Гренки", "0.04"),
                ],
            },
            {
                "name": "Паста Болоньезе",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.35",
                "min_batch_qty": "6",
                "batch_multiple_qty": "1",
                "daily_capacity": "140",
                "default_price": "520.00",
                "ingredients": [
                    ("Паста", "0.18"),
                    ("Фарш говяжий", "0.10"),
                    ("Томатный соус", "0.05"),
                    ("Лук", "0.01"),
                    ("Пармезан", "0.01"),
                ],
            },
            {
                "name": "Ризотто с грибами",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.32",
                "min_batch_qty": "5",
                "batch_multiple_qty": "1",
                "daily_capacity": "110",
                "default_price": "480.00",
                "ingredients": [
                    ("Рис арборио", "0.12"),
                    ("Шампиньоны", "0.09"),
                    ("Бульон", "0.08"),
                    ("Сливки", "0.02"),
                    ("Пармезан", "0.01"),
                ],
            },
            {
                "name": "Суп Том Ям",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.40",
                "min_batch_qty": "8",
                "batch_multiple_qty": "1",
                "daily_capacity": "90",
                "default_price": "560.00",
                "ingredients": [
                    ("Креветки", "0.08"),
                    ("Кокосовое молоко", "0.12"),
                    ("Паста Том Ям", "0.03"),
                    ("Грибы", "0.05"),
                    ("Лемонграсс", "0.02"),
                ],
            },
            {
                "name": "Суп тыквенный",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.35",
                "min_batch_qty": "10",
                "batch_multiple_qty": "2",
                "daily_capacity": "200",
                "default_price": "320.00",
                "ingredients": [
                    ("Тыква", "0.20"),
                    ("Сливки", "0.05"),
                    ("Лук", "0.03"),
                    ("Масло сливочное", "0.01"),
                    ("Соль", "0.01"),
                ],
            },
            {
                "name": "Стейк из лосося",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.28",
                "min_batch_qty": "4",
                "batch_multiple_qty": "1",
                "daily_capacity": "60",
                "default_price": "890.00",
                "ingredients": [
                    ("Лосось", "0.20"),
                    ("Лимон", "0.02"),
                    ("Оливковое масло", "0.02"),
                    ("Соль", "0.01"),
                    ("Перец", "0.01"),
                ],
            },
            {
                "name": "Котлета по-киевски",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.30",
                "min_batch_qty": "6",
                "batch_multiple_qty": "2",
                "daily_capacity": "130",
                "default_price": "640.00",
                "ingredients": [
                    ("Куриное филе", "0.20"),
                    ("Масло сливочное", "0.03"),
                    ("Панировка", "0.04"),
                    ("Яйцо", "0.02"),
                    ("Зелень", "0.01"),
                ],
            },
            {
                "name": "Оливье",
                "unit": "кг",
                "base_uom": "kg",
                "quantity_scale": "3",
                "unit_weight_kg": "1.00",
                "min_batch_qty": "3",
                "batch_multiple_qty": "1",
                "daily_capacity": "150",
                "default_price": "900.00",
                "ingredients": [
                    ("Картофель", "0.25"),
                    ("Морковь", "0.10"),
                    ("Горошек", "0.10"),
                    ("Колбаса", "0.20"),
                    ("Майонез", "0.15"),
                ],
            },
            {
                "name": "Плов с курицей",
                "unit": "кг",
                "base_uom": "kg",
                "quantity_scale": "3",
                "unit_weight_kg": "1.00",
                "min_batch_qty": "5",
                "batch_multiple_qty": "1",
                "daily_capacity": "160",
                "default_price": "820.00",
                "ingredients": [
                    ("Рис", "0.50"),
                    ("Курица", "0.30"),
                    ("Морковь", "0.10"),
                    ("Лук", "0.05"),
                    ("Специи", "0.05"),
                ],
            },
            {
                "name": "Блины с творогом",
                "unit": "порция",
                "base_uom": "pcs",
                "quantity_scale": "0",
                "unit_weight_kg": "0.22",
                "min_batch_qty": "10",
                "batch_multiple_qty": "5",
                "daily_capacity": "220",
                "default_price": "260.00",
                "ingredients": [
                    ("Мука", "0.08"),
                    ("Молоко", "0.06"),
                    ("Творог", "0.05"),
                    ("Сахар", "0.02"),
                    ("Яйцо", "0.01"),
                ],
            },
        ]

        for data in dishes:
            dish, _ = Dish.objects.update_or_create(
                name=data["name"],
                defaults={
                "unit": data["unit"],
                "base_uom": data["base_uom"],
                "quantity_scale": int(data["quantity_scale"]),
                "is_active": True,
                "created_by": seed_user,
                "unit_weight_kg": Decimal(data["unit_weight_kg"]),
                "min_batch_qty": Decimal(data["min_batch_qty"]),
                "batch_multiple_qty": Decimal(data["batch_multiple_qty"]),
                "daily_capacity": Decimal(data["daily_capacity"]),
                "default_price": Decimal(data["default_price"]),
            },
        )

            tech_card, _ = TechCard.objects.update_or_create(
                dish=dish,
                version_label="1.0",
                defaults={
                    "description": f"Техкарта для блюда «{dish.name}».",
                    "photo_url": "",
                    "is_active": True,
                    "approved_by": seed_user,
                },
            )

            TechCardVariant.objects.update_or_create(
                tech_card=tech_card,
                quantity=Decimal("1.000"),
                defaults={"note": "Стандартная порция"},
            )

            for ingredient_name, qty in data["ingredients"]:
                ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
                TechCardComponent.objects.update_or_create(
                    tech_card=tech_card,
                    ingredient=ingredient,
                    defaults={"quantity": Decimal(qty), "note": ""},
                )

        self.stdout.write(self.style.SUCCESS("Блюда и техкарты успешно добавлены."))
```

15. crm/management/commands/seed_logistics.py
```python
import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from crm.models import (
    Client,
    Order,
    OrderStatus,
    Delivery,
    Route,
    RouteStop,
    Courier,
    CourierStatus,
    User,
    Role,
)


class Command(BaseCommand):
    help = "Создаёт фиктивные данные для логистики."

    def handle(self, *args, **options):
        fake = Faker("ru_RU")

        courier_role, _ = Role.objects.get_or_create(name="Курьер")
        logistic_role, _ = Role.objects.get_or_create(name="Логист")

        logistic_user = (
            User.objects.filter(roles__name="Логист").first()
            or User.objects.filter(is_superuser=True).first()
        )
        if not logistic_user:
            logistic_user = User.objects.create_user(
                username="logistic_seed",
                email="logistic_seed@art.com",
                password="LogisticSeed123!",
                full_name="Логист Сид",
                is_active=True,
            )
            logistic_user.roles.add(logistic_role)

        transports = ["Авто", "Фургон", "Грузовик", "Вело"]
        zones = ["Центр", "Север", "Юг", "Восток", "Запад"]

        couriers = []
        for i in range(10):
            username = f"courier_seed_{i+1}"
            user, _ = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"{username}@art.com",
                    "full_name": f"Курьер {i+1}",
                    "is_active": True,
                },
            )
            user.roles.add(courier_role)
            if not user.has_usable_password():
                user.set_password("CourierSeed123!")
                user.save()
            courier, _ = Courier.objects.get_or_create(
                user=user,
                defaults={
                    "transport_type": random.choice(transports),
                    "experience_years": random.randint(1, 7),
                    "zone": random.choice(zones),
                    "status": random.choice([CourierStatus.FREE, CourierStatus.BUSY, CourierStatus.ON_ROUTE]),
                    "payload_capacity_kg": Decimal(random.randint(50, 1200)),
                    "cargo_volume_m3": Decimal(random.randint(1, 12)),
                    "cargo_length_cm": Decimal(random.randint(120, 400)),
                    "cargo_width_cm": Decimal(random.randint(80, 200)),
                    "cargo_height_cm": Decimal(random.randint(60, 200)),
                    "max_weight": Decimal(random.randint(50, 1200)),
                    "max_volume": Decimal(random.randint(1, 12)),
                    "current_lat": Decimal("55.%03d" % random.randint(600, 900)),
                    "current_lng": Decimal("37.%03d" % random.randint(400, 800)),
                    "current_latitude": Decimal("55.%03d" % random.randint(600, 900)),
                    "current_longitude": Decimal("37.%03d" % random.randint(400, 800)),
                    "location_updated_at": timezone.now(),
                },
            )
            couriers.append(courier)

        clients = list(Client.objects.all())
        if len(clients) < 10:
            for _ in range(10 - len(clients)):
                clients.append(
                    Client.objects.create(
                        name=fake.company(),
                        client_type="store",
                        inn=str(fake.random_number(digits=10)),
                        kpp=str(fake.random_number(digits=9)),
                        default_delivery_address=fake.address(),
                        email=fake.email(),
                        phone=fake.phone_number(),
                        status="active",
                    )
                )

        orders = []
        start_number = 3000
        for idx in range(50):
            order_number = f"LOG-{start_number + idx}"
            client = random.choice(clients)
            order, _ = Order.objects.get_or_create(
                order_number=order_number,
                defaults={
                    "client": client,
                    "manager": None,
                    "status": random.choice(
                        [OrderStatus.REVIEW, OrderStatus.IN_PRODUCTION, OrderStatus.SHIPPED]
                    ),
                    "address": client.default_delivery_address or fake.address(),
                    "total_amount": Decimal(random.randint(10000, 150000)),
                },
            )
            orders.append(order)

        deliveries = []
        for order in orders:
            delivery, _ = Delivery.objects.get_or_create(
                order=order,
                defaults={
                    "courier": random.choice(couriers),
                    "planned_at": timezone.now(),
                    "address": order.address,
                    "status": "Запланировано",
                    "cargo_weight_kg": Decimal(random.randint(5, 800)),
                    "cargo_volume_m3": Decimal(random.randint(1, 8)),
                    "cargo_length_cm": Decimal(random.randint(40, 200)),
                    "cargo_width_cm": Decimal(random.randint(40, 160)),
                    "cargo_height_cm": Decimal(random.randint(30, 160)),
                },
            )
            deliveries.append(delivery)

        routes = []
        for idx in range(5):
            route, _ = Route.objects.get_or_create(
                planned_date=timezone.now().date(),
                logistician=logistic_user,
                defaults={
                    "status": random.choice(["Запланирован", "Выполняется"]),
                    "notes": f"Маршрут {idx + 1}",
                },
            )
            routes.append(route)

        random.shuffle(deliveries)
        stop_deliveries = deliveries[:30]
        per_route = 6
        for route_idx, route in enumerate(routes):
            slice_start = route_idx * per_route
            slice_end = slice_start + per_route
            for seq, delivery in enumerate(stop_deliveries[slice_start:slice_end], start=1):
                RouteStop.objects.get_or_create(
                    route=route,
                    delivery=delivery,
                    defaults={
                        "sequence_index": seq,
                        "planned_time": timezone.now(),
                        "status": random.choice(["Запланирована", "В пути", "Доставлено"]),
                        "latitude": Decimal("55.%03d" % random.randint(600, 900)),
                        "longitude": Decimal("37.%03d" % random.randint(400, 800)),
                    },
                )

        self.stdout.write(self.style.SUCCESS("Логистические демо-данные созданы."))
```

16. crm/models.py
```python
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Role(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    full_name = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=32, blank=True)
    roles = models.ManyToManyField(Role, through='UserRole', related_name='users', blank=True)

    REQUIRED_FIELDS = ['full_name', 'email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name or self.username


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'role')
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'

    def __str__(self):
        return f"{self.user} → {self.role}"


class LogisticianRouteType(models.TextChoices):
    FASTEST = "fastest", "Самый быстрый"
    SAFEST = "safest", "Самый безопасный"
    SHORTEST = "shortest", "Самый короткий"


class LogisticianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="logistic_profile")
    region = models.CharField("Регион", max_length=128, blank=True)
    city = models.CharField("Город", max_length=128, blank=True)
    transport_types = models.JSONField("Доступные типы транспорта", default=list, blank=True)
    timezone = models.CharField("Часовой пояс", max_length=64, default="UTC")
    map_show_traffic = models.BooleanField("Показывать пробки", default=True)
    preferred_route_type = models.CharField(
        "Предпочтительный тип маршрута",
        max_length=16,
        choices=LogisticianRouteType.choices,
        default=LogisticianRouteType.FASTEST,
    )

    class Meta:
        verbose_name = "Профиль логиста"
        verbose_name_plural = "Профили логистов"

    def __str__(self):
        return f"Профиль логиста {self.user.full_name}"


class ClientType(models.TextChoices):
    STORE = 'store', 'Магазин'
    CAFE = 'cafe', 'Кафе'
    RESTAURANT = 'restaurant', 'Ресторан'
    DISTRIBUTOR = 'distributor', 'Дистрибьютор'
    OTHER = 'other', 'Другое'


class ClientStatus(models.TextChoices):
    PROSPECT = 'prospect', 'Переговоры'
    ACTIVE = 'active', 'Активен'
    PAUSED = 'paused', 'Приостановлен'
    LOST = 'lost', 'Закрыт'


class Client(models.Model):
    name = models.CharField('Название', max_length=255)
    client_type = models.CharField('Тип', max_length=32, choices=ClientType.choices, default=ClientType.STORE)
    inn = models.CharField('ИНН', max_length=20, blank=True)
    kpp = models.CharField('КПП', max_length=20, blank=True)
    default_delivery_address = models.CharField('Адрес доставки по умолчанию', max_length=255, blank=True)
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Телефон', max_length=32, blank=True)
    status = models.CharField('Статус', max_length=20, choices=ClientStatus.choices, default=ClientStatus.PROSPECT)
    current_stage = models.ForeignKey(
        "CooperationStage",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients",
        verbose_name="Текущий этап",
    )
    responsible_manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='clients')
    created_at = models.DateTimeField('Создан', auto_now_add=True, null=True, blank=True)
    daily_max_weight_kg = models.DecimalField('Макс. вес в день (кг)', max_digits=10, decimal_places=2, null=True, blank=True)
    daily_min_qty = models.DecimalField('Мин. объём заказа', max_digits=10, decimal_places=2, null=True, blank=True)
    guaranteed_volume_kg = models.DecimalField('Гарантированный объём (кг)', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class ClientContact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contacts')
    full_name = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=128, blank=True)
    phone = models.CharField('Телефон', max_length=32, blank=True)
    email = models.EmailField('Email', blank=True)
    is_primary = models.BooleanField('Основной', default=False)

    class Meta:
        verbose_name = 'Контакт клиента'
        verbose_name_plural = 'Контакты клиента'

    def __str__(self):
        return f"{self.full_name} ({self.client})"


class CooperationStage(models.Model):
    name = models.CharField('Название этапа', max_length=128)
    order = models.PositiveSmallIntegerField('Порядок', default=1)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Этап сотрудничества'
        verbose_name_plural = 'Этапы сотрудничества'

    def __str__(self):
        return self.name


class ClientStageHistory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='stage_history')
    stage = models.ForeignKey(CooperationStage, on_delete=models.SET_NULL, null=True, related_name='histories')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='changed_stages')
    changed_at = models.DateTimeField(default=timezone.now)
    comment = models.TextField('Комментарий', blank=True)

    class Meta:
        ordering = ['-changed_at']
        verbose_name = 'История этапов клиента'
        verbose_name_plural = 'Истории этапов клиента'

    def __str__(self):
        return f"{self.client} → {self.stage}"


class InteractionType(models.TextChoices):
    CALL = 'call', 'Звонок'
    MEETING = 'meeting', 'Встреча'
    EMAIL = 'email', 'Email'
    MESSAGE = 'message', 'Сообщение'
    OTHER = 'other', 'Другое'


class Interaction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='interactions')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='interactions')
    interaction_type = models.CharField('Тип', max_length=20, choices=InteractionType.choices)
    note = models.TextField('Заметка', blank=True)
    happened_at = models.DateTimeField('Дата/время', default=timezone.now)

    class Meta:
        ordering = ['-happened_at']
        verbose_name = 'Взаимодействие'
        verbose_name_plural = 'Взаимодействия'

    def __str__(self):
        return f"{self.client} – {self.get_interaction_type_display()}"


class Ingredient(models.Model):
    name = models.CharField('Название', max_length=128, unique=True)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Dish(models.Model):
    class BaseUom(models.TextChoices):
        KG = "kg", "кг"
        PCS = "pcs", "шт"

    name = models.CharField('Название', max_length=128)
    unit = models.CharField('Единица измерения', max_length=32, default='шт')
    base_uom = models.CharField('Базовая единица', max_length=8, choices=BaseUom.choices, default=BaseUom.PCS)
    quantity_scale = models.PositiveSmallIntegerField('Знаков после запятой', default=0)
    is_active = models.BooleanField('Активно', default=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_dishes')
    unit_weight_kg = models.DecimalField('Вес единицы (кг)', max_digits=10, decimal_places=3, null=True, blank=True)
    min_batch_qty = models.DecimalField('Мин. партия', max_digits=10, decimal_places=3, null=True, blank=True)
    batch_multiple_qty = models.DecimalField('Кратность партии', max_digits=10, decimal_places=3, null=True, blank=True)
    daily_capacity = models.DecimalField('Суточная мощность', max_digits=12, decimal_places=3, null=True, blank=True)
    default_price = models.DecimalField('Базовая цена', max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Блюдо каталога'
        verbose_name_plural = 'Блюда каталога'

    def __str__(self):
        return self.name


class TechCard(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='tech_cards')
    version_label = models.CharField('Версия/номер', max_length=32)
    description = models.TextField('Описание/технология', blank=True)
    photo_url = models.URLField('Фото', blank=True)
    is_active = models.BooleanField('Активна', default=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_tech_cards')

    class Meta:
        unique_together = ('dish', 'version_label')
        verbose_name = 'Техкарта блюда'
        verbose_name_plural = 'Техкарты блюд'

    def __str__(self):
        return f"{self.dish} v{self.version_label}"


class TechCardVariant(models.Model):
    tech_card = models.ForeignKey(TechCard, on_delete=models.CASCADE, related_name='variants')
    quantity = models.DecimalField('Количество', max_digits=10, decimal_places=3)
    note = models.CharField('Примечание', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Сорт/вариант техкарты'
        verbose_name_plural = 'Сорта/варианты техкарт'

    def __str__(self):
        return f"{self.tech_card} ({self.quantity})"


class TechCardComponent(models.Model):
    tech_card = models.ForeignKey(TechCard, on_delete=models.CASCADE, related_name='components')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='components')
    quantity = models.DecimalField('Количество', max_digits=10, decimal_places=3)
    note = models.CharField('Примечание', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Состав техкарты'
        verbose_name_plural = 'Состав техкарт'

    def __str__(self):
        return f"{self.ingredient} x {self.quantity} ({self.tech_card})"


class OrderStatus(models.TextChoices):
    DRAFT = 'Черновик', 'Черновик'
    REVIEW = 'На проверке', 'На проверке'
    CONFIRMED = 'Подтвержден производством', 'Подтвержден производством'
    IN_PRODUCTION = 'В производстве', 'В производстве'
    READY_TO_SHIP = 'Готов к отгрузке', 'Готов к отгрузке'
    SHIPPED = 'Отгружен', 'Отгружен'
    CANCELLED = 'Отменен', 'Отменен'


class Order(models.Model):
    order_number = models.CharField('Номер заказа', max_length=50, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    address = models.CharField('Адрес доставки', max_length=255, blank=True)
    status = models.CharField('Статус', max_length=64, choices=OrderStatus.choices, default=OrderStatus.DRAFT)
    delivery_date = models.DateField('Дата доставки', null=True, blank=True)
    delivery_time = models.TimeField('Время доставки', null=True, blank=True)
    delivery_type = models.CharField(
        'Тип доставки',
        max_length=32,
        choices=[
            ('Регулярная', 'Регулярная'),
            ('Разовая', 'Разовая'),
            ('Срочная', 'Срочная'),
        ],
        default='Разовая',
    )
    production_date = models.DateField('Дата производства', null=True, blank=True)
    production_shift = models.CharField('Смена', max_length=32, blank=True)
    production_window_start = models.TimeField('Окно производства (с)', null=True, blank=True)
    production_window_end = models.TimeField('Окно производства (до)', null=True, blank=True)
    comments = models.TextField('Комментарии', blank=True)
    total_amount = models.DecimalField('Сумма итого', max_digits=12, decimal_places=2, default=0)
    is_archived = models.BooleanField('В архиве', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def generate_order_number(cls):
        date_part = timezone.now().strftime("%Y%m%d")
        base = f"ORD-{date_part}-"
        last = cls.objects.filter(order_number__startswith=base).order_by("-order_number").first()
        seq = 1
        if last and last.order_number.split("-")[-1].isdigit():
            seq = int(last.order_number.split("-")[-1]) + 1
        return f"{base}{seq:03d}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"Заказ {self.order_number}"

    def recalc_total(self):
        total = self.items.aggregate(total=Sum("line_total"))["total"] or 0
        if self.total_amount != total:
            self.total_amount = total
            self.save(update_fields=["total_amount"])


class ClientAllowedTechCard(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="allowed_tech_cards")
    tech_card = models.ForeignKey(TechCard, on_delete=models.CASCADE, related_name="allowed_for_clients")

    class Meta:
        unique_together = ("client", "tech_card")
        verbose_name = "Разрешённая техкарта клиента"
        verbose_name_plural = "Разрешённые техкарты клиентов"


class Equipment(models.Model):
    name = models.CharField('Оборудование', max_length=128)
    capacity_per_hour = models.DecimalField('Производительность/час', max_digits=10, decimal_places=2, null=True, blank=True)
    available_hours = models.DecimalField('Доступные часы', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.name


class DishEquipmentRequirement(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='equipment_requirements')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='dish_requirements')
    minutes_per_unit = models.DecimalField('Минут на единицу', max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ("dish", "equipment")
        verbose_name = 'Требование оборудования'
        verbose_name_plural = 'Требования оборудования'


class IngredientStock(models.Model):
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='stock')
    quantity = models.DecimalField('Остаток', max_digits=12, decimal_places=3, default=0)

    class Meta:
        verbose_name = 'Остаток ингредиента'
        verbose_name_plural = 'Остатки ингредиентов'


class ProductionReservation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="production_reservations")
    production_date = models.DateField('Дата производства')
    weight_kg = models.DecimalField('Вес (кг)', max_digits=12, decimal_places=3, default=0)

    class Meta:
        verbose_name = 'Резерв мощности производства'
        verbose_name_plural = 'Резервы мощности производства'


class IngredientReservation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="ingredient_reservations")
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="reservations")
    production_date = models.DateField('Дата производства')
    quantity = models.DecimalField('Количество', max_digits=12, decimal_places=3, default=0)

    class Meta:
        verbose_name = 'Резерв ингредиента'
        verbose_name_plural = 'Резервы ингредиентов'


class EquipmentReservation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="equipment_reservations")
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name="reservations")
    production_date = models.DateField('Дата производства')
    hours = models.DecimalField('Часы', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Резерв оборудования'
        verbose_name_plural = 'Резервы оборудования'


class OrderItem(models.Model):
    class ItemStatus(models.TextChoices):
        NOT_STARTED = "not_started", "Не начато"
        IN_PROGRESS = "in_progress", "В сборке"
        DONE = "done", "Собрано"
        OUT_OF_STOCK = "out_of_stock", "Нет в наличии"
        REPLACED = "replaced", "Заменено"

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_items')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_items')
    custom_tech_card = models.ForeignKey(TechCard, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_items')
    quantity = models.DecimalField('Кол-во', max_digits=10, decimal_places=3)
    unit_price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    line_total = models.DecimalField('Сумма', max_digits=12, decimal_places=2, editable=False, default=0)
    supply_type = models.CharField('Тип поставки/заявки', max_length=64, blank=True)
    picked_quantity = models.DecimalField('Собрано фактически', max_digits=10, decimal_places=3, default=0)
    item_status = models.CharField('Статус позиции', max_length=20, choices=ItemStatus.choices, default=ItemStatus.NOT_STARTED)
    item_comment = models.CharField('Комментарий по позиции', max_length=255, blank=True)
    replacement_text = models.CharField('Замена', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'

    def save(self, *args, **kwargs):
        self.line_total = (self.quantity or 0) * (self.unit_price or 0)
        super().save(*args, **kwargs)
        if self.order_id:
            self.order.recalc_total()

    def delete(self, *args, **kwargs):
        order = self.order
        super().delete(*args, **kwargs)
        if order:
            order.recalc_total()

    def display_name(self):
        if self.dish:
            return self.dish.name
        if self.ingredient:
            return self.ingredient.name
        if self.custom_tech_card:
            return str(self.custom_tech_card)
        return "Позиция"

    def __str__(self):
        subject = self.dish or self.ingredient or self.custom_tech_card or 'Позиция'
        return f"{subject} x {self.quantity}"


class PickingSession(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="picking_session")
    picker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="picking_sessions")
    note = models.TextField("Примечание сборщика", blank=True)
    started_at = models.DateTimeField("Начата", null=True, blank=True)
    finished_at = models.DateTimeField("Завершена", null=True, blank=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Сборка заказа"
        verbose_name_plural = "Сборки заказов"

    def __str__(self):
        return f"Сборка {self.order.order_number}"


class CourierStatus(models.TextChoices):
    FREE = 'Свободен', 'Свободен'
    BUSY = 'Занят', 'Занят'
    ON_ROUTE = 'В рейсе', 'В рейсе'


class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='courier_profile')
    transport_type = models.CharField('Тип транспорта', max_length=64, blank=True)
    payload_capacity_kg = models.DecimalField('Грузоподъёмность (кг)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_volume_m3 = models.DecimalField('Объём кузова (м³)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_length_cm = models.DecimalField('Длина кузова (см)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_width_cm = models.DecimalField('Ширина кузова (см)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_height_cm = models.DecimalField('Высота кузова (см)', max_digits=10, decimal_places=2, null=True, blank=True)
    current_lat = models.DecimalField('Текущая широта', max_digits=9, decimal_places=6, null=True, blank=True)
    current_lng = models.DecimalField('Текущая долгота', max_digits=9, decimal_places=6, null=True, blank=True)
    max_weight = models.DecimalField('Макс. вес (кг)', max_digits=10, decimal_places=2, null=True, blank=True)
    max_volume = models.DecimalField('Макс. объём (м³)', max_digits=10, decimal_places=2, null=True, blank=True)
    current_latitude = models.DecimalField('Текущая широта (альт)', max_digits=9, decimal_places=6, null=True, blank=True)
    current_longitude = models.DecimalField('Текущая долгота (альт)', max_digits=9, decimal_places=6, null=True, blank=True)
    location_updated_at = models.DateTimeField('Обновление геолокации', null=True, blank=True)
    experience_years = models.PositiveSmallIntegerField('Опыт (лет)', default=0)
    status = models.CharField('Статус', max_length=20, choices=CourierStatus.choices, default=CourierStatus.FREE)
    zone = models.CharField('Зона', max_length=128, blank=True)

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'

    def __str__(self):
        return f"Курьер {self.user.full_name}"


class Delivery(models.Model):
    class DeliveryStatus(models.TextChoices):
        UNASSIGNED = 'Не назначено', 'Не назначено'
        PLANNED = 'Запланировано', 'Запланировано'
        ON_ROUTE = 'В пути', 'В пути'
        DELIVERED = 'Доставлено', 'Доставлено'
        CANCELLED = 'Отменено', 'Отменено'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='deliveries')
    courier = models.ForeignKey(Courier, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    route = models.ForeignKey("Route", on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
    status = models.CharField('Статус', max_length=20, choices=DeliveryStatus.choices, default=DeliveryStatus.UNASSIGNED)
    planned_at = models.DateTimeField('Плановая дата/время', null=True, blank=True)
    departure_time = models.DateTimeField('Время выезда', null=True, blank=True)
    delivered_at = models.DateTimeField('Доставлено', null=True, blank=True)
    delivery_date = models.DateField('Дата доставки', null=True, blank=True)
    address = models.CharField('Адрес', max_length=255, blank=True)
    note = models.TextField('Примечание', blank=True)
    is_sent = models.BooleanField('Отправлен', default=False)
    cargo_weight_kg = models.DecimalField('Вес груза (кг)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_volume_m3 = models.DecimalField('Объём груза (м³)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_length_cm = models.DecimalField('Длина груза (см)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_width_cm = models.DecimalField('Ширина груза (см)', max_digits=10, decimal_places=2, null=True, blank=True)
    cargo_height_cm = models.DecimalField('Высота груза (см)', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

    def __str__(self):
        return f"Доставка заказа {self.order.order_number}"

    def save(self, *args, **kwargs):
        if self.planned_at and not self.delivery_date:
            self.delivery_date = self.planned_at.date()
        super().save(*args, **kwargs)


class RouteStatus(models.TextChoices):
    DRAFT = 'Черновик', 'Черновик'
    PLANNED = 'Запланирован', 'Запланирован'
    PUBLISHED = 'Опубликован', 'Опубликован'
    IN_PROGRESS = 'Выполняется', 'Выполняется'
    DONE = 'Завершён', 'Завершён'


class Route(models.Model):
    logistician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='routes')
    planned_date = models.DateField('Дата маршрута')
    status = models.CharField('Статус', max_length=20, choices=RouteStatus.choices, default=RouteStatus.DRAFT)
    max_duration_minutes = models.PositiveSmallIntegerField('Макс. длительность (мин)', default=720)
    soft_limit_stops = models.PositiveSmallIntegerField('Мягкий лимит точек', default=30)
    strict_mode = models.BooleanField('Строгий режим лимита точек', default=False)
    notes = models.TextField('Заметки', blank=True)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'

    def __str__(self):
        return f"Маршрут {self.planned_date}"


class CourierAssignment(models.Model):
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name='assignments')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='assignments')
    assigned_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('courier', 'route')
        verbose_name = 'Назначение курьера'
        verbose_name_plural = 'Назначения курьеров'

    def __str__(self):
        return f"{self.courier} на {self.route}"


class RouteStop(models.Model):
    class StopStatus(models.TextChoices):
        DRAFT = "Черновик", "Черновик"
        CONFIRMED = "Подтверждена", "Подтверждена"
        PLANNED = "Запланирована", "Запланирована"
        IN_PROGRESS = "В пути", "В пути"
        DONE = "Доставлено", "Доставлено"
        FAILED = "Не доставлено", "Не доставлено"
        POSTPONED = "Перенесено", "Перенесено"
        CANCELLED = "Отменено", "Отменено"

    class ProofReviewStatus(models.TextChoices):
        PENDING = "Ожидает проверки", "Ожидает проверки"
        APPROVED = "Подтверждено", "Подтверждено"
        REJECTED = "Отклонено", "Отклонено"

    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='stops')
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='route_stops')
    sequence_index = models.PositiveSmallIntegerField('Порядок', default=1)
    planned_time = models.DateTimeField('Плановое время', null=True, blank=True)
    actual_time = models.DateTimeField('Фактическое время', null=True, blank=True)
    service_time_minutes = models.PositiveSmallIntegerField('Время обслуживания (мин)', default=15)
    note = models.CharField('Примечание', max_length=255, blank=True)
    status = models.CharField('Статус', max_length=20, choices=StopStatus.choices, default=StopStatus.DRAFT)
    delivery_date = models.DateField('Дата доставки', null=True, blank=True)
    failure_reason = models.TextField('Причина недоставки', blank=True)
    proof_of_delivery = models.FileField('Документ доставки', upload_to='delivery_proofs/', null=True, blank=True)
    proof_uploaded_at = models.DateTimeField('Время загрузки документа', null=True, blank=True)
    proof_uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='uploaded_delivery_proofs')
    proof_review_status = models.CharField(
        'Статус проверки документа',
        max_length=32,
        choices=ProofReviewStatus.choices,
        default=ProofReviewStatus.PENDING,
    )
    proof_review_comment = models.TextField('Комментарий проверки', blank=True)
    proof_reviewed_at = models.DateTimeField('Время проверки', null=True, blank=True)
    proof_reviewed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_delivery_proofs')
    latitude = models.DecimalField('Широта', max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField('Долгота', max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        ordering = ['sequence_index']
        verbose_name = 'Остановка маршрута'
        verbose_name_plural = 'Остановки маршрута'

    def __str__(self):
        return f"Остановка {self.sequence_index} для {self.route}"

    def save(self, *args, **kwargs):
        if self.route_id and (self.sequence_index is None or self.sequence_index <= 0):
            last = RouteStop.objects.filter(route_id=self.route_id).order_by("-sequence_index").first()
            self.sequence_index = (last.sequence_index + 1) if last else 1
        if self.delivery_id and not self.delivery_date:
            if self.delivery.delivery_date:
                self.delivery_date = self.delivery.delivery_date
            elif self.delivery.planned_at:
                self.delivery_date = self.delivery.planned_at.date()
        super().save(*args, **kwargs)


class AuditLog(models.Model):
    actor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="audit_actions")
    actor_role = models.CharField("Роль", max_length=64, blank=True)
    object_type = models.CharField("Тип объекта", max_length=64)
    object_id = models.PositiveIntegerField("ID объекта")
    field_name = models.CharField("Поле", max_length=64, blank=True)
    old_value = models.TextField("Старое значение", blank=True)
    new_value = models.TextField("Новое значение", blank=True)
    reason = models.TextField("Причина", blank=True)
    created_at = models.DateTimeField("Время", auto_now_add=True)

    class Meta:
        verbose_name = "Аудит"
        verbose_name_plural = "Аудит"

    def __str__(self):
        return f"{self.object_type}#{self.object_id} {self.field_name}"
```

17. accounts/__init__.py
```python
```

18. accounts/admin.py
```python
from django.contrib import admin

# Register your models here.
```

19. accounts/apps.py
```python
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
```

20. accounts/context_processors.py
```python
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
```

21. accounts/management/__init__.py
```python

```

22. accounts/management/commands/__init__.py
```python

```

23. accounts/management/commands/seed_demo.py
```python
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from crm.models import (
    Role,
    UserRole,
    Client,
    CooperationStage,
    ClientStageHistory,
    Interaction,
    Order,
    Delivery,
    Courier,
    OrderStatus,
    InteractionType,
    Route,
    RouteStop,
)
from reports.models import Report


class Command(BaseCommand):
    help = "Создаёт демо-данные для CRM"

    def handle(self, *args, **options):
        User = get_user_model()

        roles = [
            "Менеджер",
            "Логист",
            "Сборщик заказов",
            "Администратор системы",
        ]
        role_map = {}
        for name in roles:
            role, _ = Role.objects.get_or_create(name=name)
            role_map[name] = role

        users_data = [
            ("manager_demo", "Менеджер", "ManagerDemo123!", "manager@art.com"),
            ("logistic_demo", "Логист", "LogisticDemo123!", "logistic@art.com"),
            ("picker_demo", "Сборщик заказов", "PickerDemo123!", "picker@art.com"),
            ("admin_demo", "Администратор системы", "AdminDemo123!", "admin@art.com"),
        ]
        users = {}
        for username, role_name, password, email in users_data:
            user, _ = User.objects.get_or_create(
                username=username,
                defaults={"email": email, "full_name": role_name, "is_active": True},
            )
            user.set_password(password)
            user.save()
            UserRole.objects.get_or_create(user=user, role=role_map[role_name])
            users[role_name] = user

        stages = [
            ("Лид", 1),
            ("Переговоры", 2),
            ("Контракт", 3),
            ("Сделка", 4),
        ]
        stage_objs = []
        for name, order in stages:
            s, _ = CooperationStage.objects.get_or_create(name=name, defaults={"order": order, "is_active": True})
            stage_objs.append(s)

        client_names = [
            "ООО «Север»",
            "Кафе «Линия»",
            "Ресторан «Лист»",
            "Магазин «Вкус»",
            "Дистрибьютор «Трейд»",
        ]
        clients = []
        for i, name in enumerate(client_names, start=1):
            c, _ = Client.objects.get_or_create(
                name=name,
                defaults={
                    "phone": f"+7 (900) 000-00-0{i}",
                    "email": f"client{i}@example.com",
                    "status": "active" if i % 2 == 0 else "prospect",
                    "responsible_manager": users["Менеджер"],
                    "current_stage": stage_objs[min(i - 1, len(stage_objs) - 1)],
                },
            )
            clients.append(c)
            ClientStageHistory.objects.get_or_create(
                client=c,
                stage=c.current_stage,
                defaults={"changed_by": users["Менеджер"], "comment": "Стартовая стадия"},
            )

        for c in clients:
            Interaction.objects.get_or_create(
                client=c,
                manager=users["Менеджер"],
                interaction_type=InteractionType.CALL,
                defaults={"note": "Первичный контакт", "happened_at": timezone.now()},
            )

        orders = []
        for idx, client in enumerate(clients, start=1001):
            order, _ = Order.objects.get_or_create(
                order_number=f"ORD-{idx}",
                defaults={
                    "client": client,
                    "manager": users["Менеджер"],
                    "status": OrderStatus.REVIEW if idx % 2 == 0 else OrderStatus.IN_PRODUCTION,
                    "address": client.default_delivery_address or "Москва, ул. Пример, 1",
                    "total_amount": 15000 + idx,
                },
            )
            orders.append(order)

        courier_user, _ = User.objects.get_or_create(
            username="courier_demo",
            defaults={"email": "courier@art.com", "full_name": "Курьер Демо", "is_active": True},
        )
        courier_user.set_password("CourierDemo123!")
        courier_user.save()
        courier, _ = Courier.objects.get_or_create(
            user=courier_user,
            defaults={"transport_type": "Авто", "experience_years": 3, "zone": "Центр"},
        )

        for order in orders:
            Delivery.objects.get_or_create(
                order=order,
                defaults={
                    "courier": courier,
                    "planned_at": timezone.now(),
                    "address": order.address,
                    "status": "planned",
                },
            )

        route, _ = Route.objects.get_or_create(
            planned_date=timezone.now().date(),
            defaults={"logistician": users["Логист"], "status": "planned"},
        )
        for idx, delivery in enumerate(Delivery.objects.all()[:3], start=1):
            RouteStop.objects.get_or_create(
                route=route,
                delivery=delivery,
                defaults={"sequence_index": idx, "planned_time": timezone.now()},
            )

        Report.objects.get_or_create(
            title="Отчёт по продажам",
            defaults={
                "period_from": timezone.now().date(),
                "period_to": timezone.now().date(),
                "status": "ready",
                "created_by": users["Менеджер"],
            },
        )

        self.stdout.write(self.style.SUCCESS("Демо-данные созданы."))
```

24. accounts/models.py
```python
from django.db import models

# Create your models here.
```

25. accounts/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

26. accounts/urls.py
```python
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, logout_view, dashboard_root

urlpatterns = [
    path("", login_view, name="root-login"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_root, name="dashboard-root"),
    path("password-reset/", auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset_form.html",
        email_template_name="accounts/password_reset_email.html",
        subject_template_name="accounts/password_reset_subject.txt",
        success_url="/password-reset/done/",
    ), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/password_reset_confirm.html",
        success_url="/reset/done/",
    ), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ), name="password_reset_complete"),
]
```

27. accounts/utils.py
```python
from functools import wraps
from django.shortcuts import redirect


def role_required(role_name: str):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("/login/")
            if not request.user.roles.filter(name__iexact=role_name).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator


def roles_required(role_names):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect("/login/")
            if not request.user.roles.filter(name__in=role_names).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
```

28. accounts/views.py
```python
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages


def _role_redirect(user):
    if user.roles.filter(name__iexact="Менеджер").exists():
        return "/dashboard/manager/"
    if user.roles.filter(name__iexact="Логист").exists():
        return "/dashboard/logistic/"
    if user.roles.filter(name__iexact="Сборщик заказов").exists():
        return "/dashboard/picker/"
    if user.roles.filter(name__iexact="Курьер").exists():
        return "/logistics/courier/routes/"
    if user.roles.filter(name__iexact="Администратор системы").exists():
        return "/dashboard/admin/"
    return None


def login_view(request):
    if request.user.is_authenticated:
        target = _role_redirect(request.user)
        if target:
            return redirect(target)
        logout(request)
        messages.error(request, "У вашего аккаунта нет роли. Войдите под другой учётной записью.")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        user = None
        if "@" in username:
            User = get_user_model()
            candidate = User.objects.filter(email__iexact=username).first()
            if candidate:
                user = authenticate(request, username=candidate.username, password=password)
        else:
            user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Неверный логин или пароль.")
        else:
            login(request, user)
            target = _role_redirect(user)
            if target:
                return redirect(target)
            logout(request)
            messages.error(request, "Нет прав доступа. У пользователя не назначена роль.")
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


def dashboard_root(request):
    # редирект на соответствующую роль
    if not request.user.is_authenticated:
        return redirect("/login/")
    target = _role_redirect(request.user)
    if target:
        return redirect(target)
    logout(request)
    messages.error(request, "Нет прав доступа. У пользователя не назначена роль.")
    return redirect("/login/")

# Create your views here.
```

29. clients/__init__.py
```python
```

30. clients/admin.py
```python
from django.contrib import admin

# Register your models here.
```

31. clients/apps.py
```python
from django.apps import AppConfig


class ClientsConfig(AppConfig):
    name = 'clients'
```

32. clients/forms.py
```python
from django import forms
from crm.forms import BootstrapFormMixin
from crm.models import Client, Interaction, ClientStageHistory, CooperationStage


class ClientForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "client_type",
            "inn",
            "kpp",
            "default_delivery_address",
            "email",
            "phone",
            "status",
            "current_stage",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()


class InteractionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ["interaction_type", "note", "happened_at"]
        labels = {
            "interaction_type": "Тип взаимодействия",
            "note": "Заметка",
            "happened_at": "Дата и время",
        }
        widgets = {
            "happened_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        self.fields["happened_at"].input_formats = ["%Y-%m-%dT%H:%M"]


class StageChangeForm(BootstrapFormMixin, forms.ModelForm):
    stage = forms.ModelChoiceField(
        queryset=CooperationStage.objects.none(),
        label="Этап сотрудничества",
        required=True,
    )

    class Meta:
        model = ClientStageHistory
        fields = ["stage", "comment"]
        labels = {"comment": "Комментарий"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["stage"].queryset = CooperationStage.objects.filter(is_active=True)
        self._init_bootstrap()
```

33. clients/models.py
```python
from django.db import models

# Create your models here.
```

34. clients/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

35. clients/urls.py
```python
from django.urls import path
from .views import client_list, client_create, client_edit, client_delete, client_detail

urlpatterns = [
    path("", client_list, name="clients-list"),
    path("create/", client_create, name="clients-create"),
    path("<int:pk>/", client_detail, name="clients-detail"),
    path("<int:pk>/edit/", client_edit, name="clients-edit"),
    path("<int:pk>/delete/", client_delete, name="clients-delete"),
]
```

36. clients/views.py
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from accounts.utils import roles_required
from crm.models import Client, CooperationStage, ClientStageHistory, Interaction, ClientStatus, Order
from .forms import ClientForm, InteractionForm, StageChangeForm


@roles_required(["Менеджер", "Администратор системы"])
def client_list(request):
    qs = Client.objects.select_related("current_stage", "responsible_manager").all()
    q = request.GET.get("q")
    status = request.GET.get("status")
    stage = request.GET.get("stage")
    sort = request.GET.get("sort")
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q))
    if status:
        qs = qs.filter(status=status)
    if stage:
        qs = qs.filter(current_stage_id=stage)
    if sort in ["name", "-name", "created_at", "-created_at"]:
        qs = qs.order_by(sort)
    stages = CooperationStage.objects.filter(is_active=True)
    return render(
        request,
        "clients/list.html",
        {"clients": qs, "stages": stages, "status_choices": ClientStatus.choices},
    )


@roles_required(["Менеджер", "Администратор системы"])
def client_create(request):
    form = ClientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        if request.user.roles.filter(name__iexact="Менеджер").exists():
            obj.responsible_manager = request.user
        obj.save()
        form.save_m2m()
        messages.success(request, "Клиент создан.")
        return redirect("/clients/")
    return render(request, "clients/form.html", {"form": form, "title": "Новый клиент"})


@roles_required(["Менеджер", "Администратор системы"])
def client_edit(request, pk):
    obj = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Клиент обновлён.")
        return redirect("/clients/")
    return render(request, "clients/form.html", {"form": form, "title": "Редактирование клиента"})


@roles_required(["Менеджер", "Администратор системы"])
def client_delete(request, pk):
    obj = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Клиент удалён.")
        return redirect("/clients/")
    return render(request, "clients/delete.html", {"object": obj})


@roles_required(["Менеджер", "Администратор системы"])
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    interactions = Interaction.objects.filter(client=client).select_related("manager")
    stage_history = ClientStageHistory.objects.filter(client=client).select_related("stage", "changed_by")
    client_orders = Order.objects.filter(client=client).order_by("-created_at")

    interaction_form = InteractionForm(prefix="interaction")
    stage_form = StageChangeForm(prefix="stage", initial={"stage": client.current_stage})

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add_interaction":
            interaction_form = InteractionForm(request.POST, prefix="interaction")
            if interaction_form.is_valid():
                obj = interaction_form.save(commit=False)
                obj.client = client
                obj.manager = request.user
                obj.save()
                messages.success(request, "Взаимодействие добавлено.")
                return redirect(f"/clients/{client.id}/")
        if action == "change_stage":
            stage_form = StageChangeForm(request.POST, prefix="stage")
            if stage_form.is_valid():
                stage = stage_form.cleaned_data["stage"]
                comment = stage_form.cleaned_data.get("comment", "")
                ClientStageHistory.objects.create(
                    client=client,
                    stage=stage,
                    changed_by=request.user,
                    comment=comment,
                )
                client.current_stage = stage
                client.save(update_fields=["current_stage"])
                messages.success(request, "Этап сотрудничества обновлён.")
                return redirect(f"/clients/{client.id}/")

    return render(
        request,
        "clients/detail.html",
        {
            "client": client,
            "interactions": interactions,
            "stage_history": stage_history,
            "client_orders": client_orders,
            "interaction_form": interaction_form,
            "stage_form": stage_form,
        },
    )

# Create your views here.
```

37. orders/__init__.py
```python
```

38. orders/admin.py
```python
from django.contrib import admin

# Register your models here.
```

39. orders/apps.py
```python
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'
```

40. orders/forms.py
```python
from django import forms
from django.utils import timezone
from decimal import Decimal, InvalidOperation
from crm.forms import BootstrapFormMixin
from django.forms import modelformset_factory
from crm.models import Order, OrderItem, PickingSession, Dish


class OrderForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "order_number",
            "client",
            "status",
            "address",
            "delivery_date",
            "delivery_time",
            "delivery_type",
            "comments",
            "total_amount",
        ]
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
            "delivery_time": forms.TimeInput(attrs={"type": "time"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        if "order_number" in self.fields:
            self.fields["order_number"].widget.attrs.setdefault("readonly", True)
            self.fields["order_number"].required = False
            self.fields["order_number"].widget.attrs.pop("required", None)
            if not self.instance.pk and not self.instance.order_number:
                self.fields["order_number"].initial = Order.generate_order_number()
        if "total_amount" in self.fields:
            self.fields["total_amount"].widget.attrs.setdefault("readonly", True)
            self.fields["total_amount"].widget.attrs.setdefault("inputmode", "decimal")
            self.fields["total_amount"].widget.attrs.setdefault("type", "text")
        if "status" in self.fields:
            allowed = ["Черновик", "На проверке"]
            self.fields["status"].choices = [
                (value, label)
                for value, label in self.fields["status"].choices
                if value in allowed
            ]
        if "delivery_date" in self.fields:
            min_date = timezone.localdate()
            # Не ставим min, если редактируем заказ с датой в прошлом, чтобы дата отображалась
            if not self.instance.pk or not self.instance.delivery_date or self.instance.delivery_date >= min_date:
                self.fields["delivery_date"].widget.attrs["min"] = min_date.isoformat()
            else:
                self.fields["delivery_date"].widget.attrs.pop("min", None)
            # Явный формат для value, чтобы input type=date показывал значение
            self.fields["delivery_date"].input_formats = ["%Y-%m-%d"]

    def clean(self):
        cleaned = super().clean()
        total_amount = cleaned.get("total_amount")
        if isinstance(total_amount, str):
            cleaned["total_amount"] = total_amount.replace(",", ".")
        if not cleaned.get("delivery_date"):
            self.add_error("delivery_date", "Укажите дату доставки.")
        else:
            if cleaned["delivery_date"] < timezone.localdate():
                self.add_error("delivery_date", "Дата доставки не может быть в прошедшем времени.")
        if not cleaned.get("delivery_time"):
            self.add_error("delivery_time", "Укажите время доставки.")
        return cleaned


class PickingSessionForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PickingSession
        fields = ["note"]
        labels = {"note": "Примечание сборщика"}
        widgets = {"note": forms.Textarea(attrs={"rows": 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()


class OrderItemPickForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["picked_quantity", "item_status", "item_comment", "replacement_text"]
        labels = {
            "picked_quantity": "Собрано фактически",
            "item_status": "Статус позиции",
            "item_comment": "Комментарий",
            "replacement_text": "Замена",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    def clean(self):
        cleaned = super().clean()
        status = cleaned.get("item_status")
        comment = cleaned.get("item_comment", "")
        replacement = cleaned.get("replacement_text", "")
        if status == OrderItem.ItemStatus.OUT_OF_STOCK and not comment:
            self.add_error("item_comment", "Укажите причину отсутствия.")
        if status == OrderItem.ItemStatus.REPLACED and not replacement:
            self.add_error("replacement_text", "Укажите текст замены.")
        return cleaned


class OrderItemForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
            "dish",
            "quantity",
            "unit_price",
            "supply_type",
            "item_comment",
        ]
        labels = {
            "dish": "Блюдо",
            "quantity": "Количество",
            "unit_price": "Цена",
            "supply_type": "Тип поставки",
            "item_comment": "Комментарий",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        if "dish" in self.fields:
            self.fields["dish"].queryset = Dish.objects.filter(is_active=True).order_by("name")
        if "unit_price" in self.fields:
            self.fields["unit_price"].widget.attrs.setdefault("readonly", True)
            self.fields["unit_price"].widget.attrs.setdefault("inputmode", "decimal")
            self.fields["unit_price"].widget.attrs.setdefault("step", "0.01")
        if "quantity" in self.fields:
            self.fields["quantity"].widget.attrs.setdefault("min", "1")
            self.fields["quantity"].widget.attrs.setdefault("step", "1")

    def clean(self):
        cleaned = super().clean()
        dish = cleaned.get("dish")
        qty = cleaned.get("quantity")
        if not dish:
            self.add_error("dish", "Выберите блюдо.")
        if qty is not None:
            if qty <= 0:
                self.add_error("quantity", "Количество должно быть больше 0.")
            if dish:
                scale = dish.quantity_scale or 0
                quant = Decimal("1").scaleb(-scale)
                try:
                    quantized = Decimal(qty).quantize(quant)
                except (InvalidOperation, TypeError):
                    self.add_error("quantity", "Некорректный формат количества.")
                    return cleaned
                if quantized != Decimal(qty):
                    self.add_error("quantity", f"Количество должно иметь не более {scale} знаков после запятой.")
                if dish.base_uom == Dish.BaseUom.PCS and quantized != quantized.to_integral_value():
                    self.add_error("quantity", "Для штучных блюд количество должно быть целым.")
                if dish.min_batch_qty is not None and quantized < dish.min_batch_qty:
                    self.add_error("quantity", f"Минимальная партия: {dish.min_batch_qty}.")
                if dish.batch_multiple_qty:
                    step = dish.batch_multiple_qty
                    remainder = (quantized % step) if step else Decimal("0")
                    if remainder != 0:
                        self.add_error("quantity", f"Количество должно быть кратно {step}.")
        return cleaned


OrderItemPickFormSet = modelformset_factory(
    OrderItem,
    form=OrderItemPickForm,
    extra=0,
)


OrderItemFormSet = modelformset_factory(
    OrderItem,
    form=OrderItemForm,
    extra=1,
    can_delete=True,
)
```

41. orders/models.py
```python
from django.db import models

# Create your models here.
```

42. orders/tests.py
```python
from datetime import date, timedelta

from django.test import TestCase

from crm.models import Client, Dish, Order, OrderItem, OrderStatus, User
from orders.forms import OrderForm, OrderItemForm
from orders.views import _get_reserved_qty_map


class OrderFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="manager1",
            email="manager1@example.com",
            password="pass12345",
            full_name="Manager One",
        )
        self.client_obj = Client.objects.create(name="Test Client")

    def test_order_number_not_required(self):
        form = OrderForm(
            data={
                "order_number": "",
                "client": self.client_obj.id,
                "status": OrderStatus.DRAFT,
                "address": "Test address",
                "delivery_date": "2026-02-20",
                "delivery_time": "10:00",
                "delivery_type": "Разовая",
                "comments": "",
                "total_amount": "0.00",
            }
        )
        self.assertTrue(form.is_valid())

    def test_delivery_date_time_required(self):
        form = OrderForm(
            data={
                "order_number": "",
                "client": self.client_obj.id,
                "status": OrderStatus.DRAFT,
                "address": "Test address",
                "delivery_date": "",
                "delivery_time": "",
                "delivery_type": "Разовая",
                "comments": "",
                "total_amount": "0.00",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("delivery_date", form.errors)
        self.assertIn("delivery_time", form.errors)

    def test_delivery_date_cannot_be_in_past(self):
        past_day = date.today() - timedelta(days=1)
        form = OrderForm(
            data={
                "order_number": "",
                "client": self.client_obj.id,
                "status": OrderStatus.DRAFT,
                "address": "Test address",
                "delivery_date": past_day.isoformat(),
                "delivery_time": "10:00",
                "delivery_type": "Разовая",
                "comments": "",
                "total_amount": "0.00",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("delivery_date", form.errors)


class OrderItemFormTests(TestCase):
    def setUp(self):
        self.dish = Dish.objects.create(name="Тест блюдо", unit="шт", daily_capacity=100, default_price=10)

    def test_quantity_must_be_integer(self):
        form = OrderItemForm(data={"dish": self.dish.id, "quantity": 0, "unit_price": "10.00"})
        self.assertFalse(form.is_valid())
        form = OrderItemForm(data={"dish": self.dish.id, "quantity": 1.5, "unit_price": "10.00"})
        self.assertFalse(form.is_valid())
        form = OrderItemForm(data={"dish": self.dish.id, "quantity": 2, "unit_price": "10.00"})
        self.assertTrue(form.is_valid())


class ReservedQtyTests(TestCase):
    def setUp(self):
        self.client_obj = Client.objects.create(name="Test Client")
        self.dish = Dish.objects.create(name="Котлета", unit="шт", daily_capacity=100, default_price=50)

    def test_reserved_qty_excludes_statuses_and_order(self):
        day = date(2026, 2, 20)
        order1 = Order.objects.create(
            order_number="ORD-001",
            client=self.client_obj,
            status=OrderStatus.CONFIRMED,
            delivery_date=day,
        )
        OrderItem.objects.create(order=order1, dish=self.dish, quantity=5, unit_price=50)

        order2 = Order.objects.create(
            order_number="ORD-002",
            client=self.client_obj,
            status=OrderStatus.CANCELLED,
            delivery_date=day,
        )
        OrderItem.objects.create(order=order2, dish=self.dish, quantity=7, unit_price=50)

        order3 = Order.objects.create(
            order_number="ORD-003",
            client=self.client_obj,
            status=OrderStatus.IN_PRODUCTION,
            delivery_date=day,
        )
        OrderItem.objects.create(order=order3, dish=self.dish, quantity=9, unit_price=50)

        reserved = _get_reserved_qty_map(day)
        self.assertEqual(reserved.get(self.dish.id), 14)

        reserved_excluding = _get_reserved_qty_map(day, exclude_order_id=order3.id)
        self.assertEqual(reserved_excluding.get(self.dish.id), 5)
```

43. orders/urls.py
```python
from django.urls import path
from .views import (
    order_list,
    order_create,
    order_edit,
    order_delete,
    order_archive,
    order_status_update,
    picker_orders,
    picker_order_detail,
    order_archive_toggle,
    order_bulk_delete,
)

urlpatterns = [
    path("", order_list, name="orders-list"),
    path("create/", order_create, name="orders-create"),
    path("archive/", order_archive, name="orders-archive"),
    path("bulk-delete/", order_bulk_delete, name="orders-bulk-delete"),
    path("picker/", picker_orders, name="orders-picker"),
    path("picker/<int:pk>/", picker_order_detail, name="orders-picker-detail"),
    path("<int:pk>/status/", order_status_update, name="orders-status"),
    path("<int:pk>/archive-toggle/", order_archive_toggle, name="orders-archive-toggle"),
    path("<int:pk>/edit/", order_edit, name="orders-edit"),
    path("<int:pk>/delete/", order_delete, name="orders-delete"),
]
```

44. orders/views.py
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.utils import roles_required, role_required
from django.utils import timezone
from django.conf import settings
from django.db.models import Sum
from django.db import transaction
from django.http import JsonResponse, HttpResponseBadRequest
from crm.models import (
    Order,
    OrderStatus,
    Client,
    Delivery,
    OrderItem,
    PickingSession,
    Dish,
    TechCard,
    TechCardComponent,
    ClientAllowedTechCard,
    ProductionReservation,
    IngredientReservation,
    EquipmentReservation,
    IngredientStock,
    DishEquipmentRequirement,
    Ingredient,
)
from .forms import OrderForm, PickingSessionForm, OrderItemPickFormSet, OrderItemFormSet


def _apply_production_fields(order):
    if not order.delivery_date or not order.delivery_time:
        return
    morning_cutoff = timezone.datetime.strptime(
        getattr(settings, "ORDER_MORNING_CUTOFF_TIME", "10:00"), "%H:%M"
    ).time()
    if order.delivery_time <= morning_cutoff:
        order.production_date = order.delivery_date - timezone.timedelta(days=1)
        order.production_shift = "Ночная"
        order.production_window_start = timezone.datetime.strptime(
            getattr(settings, "PRODUCTION_WINDOW_NIGHT_START", "22:00"), "%H:%M"
        ).time()
        order.production_window_end = timezone.datetime.strptime(
            getattr(settings, "PRODUCTION_WINDOW_NIGHT_END", "06:00"), "%H:%M"
        ).time()
    else:
        order.production_date = order.delivery_date
        order.production_shift = "Дневная"
        order.production_window_start = timezone.datetime.strptime(
            getattr(settings, "PRODUCTION_WINDOW_DAY_START", "06:00"), "%H:%M"
        ).time()
        order.production_window_end = timezone.datetime.strptime(
            getattr(settings, "PRODUCTION_WINDOW_DAY_END", "18:00"), "%H:%M"
        ).time()


def _order_item_weight(item):
    if not item.dish:
        return item.quantity or 0
    if item.dish.base_uom == Dish.BaseUom.KG:
        return item.quantity or 0
    if item.dish.base_uom == Dish.BaseUom.PCS:
        if item.dish.unit_weight_kg:
            return (item.quantity or 0) * item.dish.unit_weight_kg
        return 0
    return item.quantity or 0


def _attach_tech_card(order, item):
    if not item.dish:
        return
    allowed = ClientAllowedTechCard.objects.filter(client=order.client, tech_card__dish=item.dish, tech_card__is_active=True)
    if allowed.exists():
        item.custom_tech_card = allowed.first().tech_card
        return
    active = TechCard.objects.filter(dish=item.dish, is_active=True).order_by("-id")
    if active.count() == 1:
        item.custom_tech_card = active.first()
        return
    raise ValueError("Для блюда нет активной техкарты или их несколько без разрешения клиента.")


def _ensure_order_number(order):
    if order.pk and order.order_number:
        return
    order.order_number = Order.generate_order_number()


RESERVED_STATUSES = {
    OrderStatus.CONFIRMED,
    OrderStatus.IN_PRODUCTION,
    OrderStatus.READY_TO_SHIP,
    OrderStatus.SHIPPED,
}


def _get_reserved_qty_map(production_date, exclude_order_id=None):
    if not production_date:
        return {}
    qs = OrderItem.objects.filter(
        order__delivery_date=production_date,
        order__status__in=RESERVED_STATUSES,
        dish__isnull=False,
    )
    if exclude_order_id:
        qs = qs.exclude(order_id=exclude_order_id)
    data = qs.values("dish_id").annotate(total=Sum("quantity"))
    return {row["dish_id"]: row["total"] for row in data}


def _validate_dish_capacity(order, items):
    reserved_map = _get_reserved_qty_map(order.delivery_date, exclude_order_id=order.id)
    requested_map = {}
    for item in items:
        if not item.dish_id:
            continue
        requested_map[item.dish_id] = requested_map.get(item.dish_id, 0) + (item.quantity or 0)

    errors = []
    for dish_id, requested_qty in requested_map.items():
        dish = Dish.objects.filter(pk=dish_id).only("id", "name", "daily_capacity").first()
        if not dish or dish.daily_capacity is None:
            continue
        reserved_qty = reserved_map.get(dish_id, 0) or 0
        available_qty = max(dish.daily_capacity - reserved_qty, 0)
        if requested_qty > available_qty:
            errors.append(
                f"Недостаточная мощность для «{dish.name}»: доступно {available_qty}, запрошено {requested_qty}."
            )
    return errors


def _validate_order_capacity(order, items):
    errors = []
    warnings = []
    info = {}

    if order.delivery_date:
        cutoff = timezone.datetime.strptime(getattr(settings, "ORDER_CUTOFF_TIME", "16:00"), "%H:%M").time()
        if order.delivery_date == timezone.now().date() and timezone.now().time() > cutoff:
            errors.append("Заказ после допустимого времени. Перенесите дату доставки.")

    total_weight = sum([_order_item_weight(i) for i in items])
    info["order_weight"] = total_weight
    if order.client.daily_max_weight_kg and order.delivery_date:
        existing = Order.objects.filter(client=order.client, delivery_date=order.delivery_date).exclude(pk=order.pk)
        existing_weight = sum([sum([_order_item_weight(i) for i in o.items.all()]) for o in existing])
        info["client_daily_limit"] = order.client.daily_max_weight_kg
        info["client_reserved"] = existing_weight
        if existing_weight + total_weight > order.client.daily_max_weight_kg:
            errors.append("Превышен лимит клиента по весу на день.")
    if order.client.daily_min_qty and total_weight < order.client.daily_min_qty:
        warnings.append("Минимальный объём клиента не достигнут.")

    max_capacity = getattr(settings, "PRODUCTION_MAX_WEIGHT_KG", None)
    if max_capacity is not None and order.production_date:
        reserved = ProductionReservation.objects.filter(production_date=order.production_date).exclude(order=order).aggregate(
            total=Sum("weight_kg")
        )["total"] or 0
        info["production_capacity"] = max_capacity
        info["production_reserved"] = reserved
        if reserved + total_weight > max_capacity:
            excess = (reserved + total_weight) - max_capacity
            errors.append(
                f"Превышена производственная мощность на {order.production_date}. "
                f"Доступно: {max_capacity} кг, ваш заказ: {total_weight} кг, превышение: {excess} кг."
            )
    elif max_capacity is not None:
        info["production_capacity"] = max_capacity
        info["production_reserved"] = 0

    equipment_requirements = {}
    for item in items:
        if not item.dish:
            continue
        for req in DishEquipmentRequirement.objects.filter(dish=item.dish).select_related("equipment"):
            minutes = (req.minutes_per_unit or 0) * (item.quantity or 0)
            equipment_requirements[req.equipment_id] = equipment_requirements.get(req.equipment_id, 0) + minutes

    for eq_id, minutes in equipment_requirements.items():
        eq = DishEquipmentRequirement.objects.filter(equipment_id=eq_id).select_related("equipment").first().equipment
        available_hours = float(eq.available_hours or 0)
        reserved_hours = EquipmentReservation.objects.filter(equipment=eq, production_date=order.production_date).exclude(
            order=order
        ).aggregate(total=Sum("hours"))["total"] or 0
        required_hours = minutes / 60
        if available_hours and reserved_hours + required_hours > available_hours:
            errors.append(f"Превышен лимит оборудования: {eq.name}")

    ingredients_need = {}
    for item in items:
        if not item.custom_tech_card and item.dish:
            active = TechCard.objects.filter(dish=item.dish, is_active=True).order_by("-id").first()
            if active:
                item.custom_tech_card = active
        if not item.custom_tech_card:
            continue
        for comp in TechCardComponent.objects.filter(tech_card=item.custom_tech_card):
            qty = (comp.quantity or 0) * (item.quantity or 0)
            ingredients_need[comp.ingredient_id] = ingredients_need.get(comp.ingredient_id, 0) + qty

    ingredient_warnings = []
    ingredients_map = Ingredient.objects.in_bulk(list(ingredients_need.keys()))
    for ingredient_id, qty in ingredients_need.items():
        stock = IngredientStock.objects.filter(ingredient_id=ingredient_id).first()
        available = stock.quantity if stock else 0
        reserved = IngredientReservation.objects.filter(ingredient_id=ingredient_id, production_date=order.production_date).exclude(
            order=order
        ).aggregate(total=Sum("quantity"))["total"] or 0
        missing = qty - (available - reserved)
        if missing > 0:
            ingredient = ingredients_map.get(ingredient_id)
            ingredient_warnings.append(
                {
                    "id": ingredient_id,
                    "name": ingredient.name if ingredient else f"ID {ingredient_id}",
                    "required": float(qty),
                    "available": float(available),
                    "reserved": float(reserved),
                    "missing": float(missing),
                }
            )
    if ingredient_warnings:
        errors.append("Недостаточно ингредиентов для заказа. Проверьте список ниже.")
        info["ingredient_warnings"] = ingredient_warnings

    for item in items:
        if not item.dish:
            continue
        if item.dish.min_batch_qty and (item.quantity or 0) < item.dish.min_batch_qty:
            errors.append(f"Минимальная партия для {item.dish.name} — {item.dish.min_batch_qty}")
        if item.dish.batch_multiple_qty and (item.quantity or 0) % item.dish.batch_multiple_qty != 0:
            errors.append(f"Количество для {item.dish.name} должно быть кратно {item.dish.batch_multiple_qty}")

    return errors, warnings, info


def _reserve_resources(order):
    ProductionReservation.objects.filter(order=order).delete()
    IngredientReservation.objects.filter(order=order).delete()
    EquipmentReservation.objects.filter(order=order).delete()

    items = list(order.items.select_related("dish"))
    total_weight = sum([_order_item_weight(i) for i in items])
    if order.production_date:
        ProductionReservation.objects.create(order=order, production_date=order.production_date, weight_kg=total_weight)

    ingredients_need = {}
    for item in items:
        if item.custom_tech_card:
            for comp in TechCardComponent.objects.filter(tech_card=item.custom_tech_card):
                qty = (comp.quantity or 0) * (item.quantity or 0)
                ingredients_need[comp.ingredient_id] = ingredients_need.get(comp.ingredient_id, 0) + qty
    for ingredient_id, qty in ingredients_need.items():
        IngredientReservation.objects.create(
            order=order,
            ingredient_id=ingredient_id,
            production_date=order.production_date,
            quantity=qty,
        )

    equipment_requirements = {}
    for item in items:
        if not item.dish:
            continue
        for req in DishEquipmentRequirement.objects.filter(dish=item.dish).select_related("equipment"):
            minutes = (req.minutes_per_unit or 0) * (item.quantity or 0)
            equipment_requirements[req.equipment_id] = equipment_requirements.get(req.equipment_id, 0) + minutes
    for eq_id, minutes in equipment_requirements.items():
        EquipmentReservation.objects.create(
            order=order,
            equipment_id=eq_id,
            production_date=order.production_date,
            hours=minutes / 60,
        )


@roles_required(["Менеджер", "Администратор системы"])
def order_list(request):
    qs = Order.objects.select_related("client").filter(is_archived=False)
    q = request.GET.get("q")
    status = request.GET.get("status")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")
    client_id = request.GET.get("client")
    sort = request.GET.get("sort")
    if q:
        qs = qs.filter(order_number__icontains=q)
    if status:
        qs = qs.filter(status=status)
    if client_id:
        qs = qs.filter(client_id=client_id)
    if date_from:
        qs = qs.filter(created_at__date__gte=date_from)
    if date_to:
        qs = qs.filter(created_at__date__lte=date_to)
    if sort in ["created_at", "-created_at", "order_number", "-order_number"]:
        qs = qs.order_by(sort)
    clients = Client.objects.all()
    return render(
        request,
        "orders/list.html",
        {"orders": qs, "statuses": OrderStatus.choices, "clients": clients},
    )


@roles_required(["Менеджер", "Администратор системы"])
def order_create(request):
    form = OrderForm(request.POST or None)
    formset = OrderItemFormSet(request.POST or None, queryset=OrderItem.objects.none())
    dish_prices = {d.id: float(d.default_price) for d in Dish.objects.filter(is_active=True, default_price__isnull=False)}
    if request.method == "POST" and form.is_valid() and formset.is_valid():
        with transaction.atomic():
            obj = form.save(commit=False)
            if request.user.roles.filter(name__iexact="Менеджер").exists():
                obj.manager = request.user
            action = request.POST.get("action", "save")
            obj.status = OrderStatus.DRAFT if action == "draft" else OrderStatus.REVIEW
            _apply_production_fields(obj)
            _ensure_order_number(obj)
            obj.save()
            items = [i for i in formset.save(commit=False) if i.dish]
            if not items:
                messages.error(request, "Добавьте хотя бы одну позицию заказа.")
                return render(
                request,
                "orders/form.html",
                {"form": form, "formset": formset, "title": "Новый заказ", "dish_prices": dish_prices},
            )
        errors, warnings, info = _validate_order_capacity(obj, items)
        if errors:
            clients = Client.objects.all()
            for err in errors:
                messages.error(request, err)
            return render(
                request,
                "orders/form.html",
                {"form": form, "formset": formset, "title": "Новый заказ", "warnings": warnings, "info": info, "clients": clients, "dish_prices": dish_prices},
            )
            capacity_errors = _validate_dish_capacity(obj, items)
            if capacity_errors:
                clients = Client.objects.all()
                for err in capacity_errors:
                    messages.error(request, err)
                return render(
                    request,
                    "orders/form.html",
                    {"form": form, "formset": formset, "title": "Новый заказ", "warnings": warnings, "info": info, "clients": clients},
                )
            for item in items:
                item.order = obj
                try:
                    _attach_tech_card(obj, item)
                except ValueError as exc:
                    messages.error(request, str(exc))
                    clients = Client.objects.all()
                return render(
                    request,
                    "orders/form.html",
                    {"form": form, "formset": formset, "title": "Новый заказ", "warnings": warnings, "info": info, "clients": clients, "dish_prices": dish_prices},
                )
            if item.unit_price is None and item.dish and item.dish.default_price is not None:
                item.unit_price = item.dish.default_price
            if item.unit_price is None:
                messages.error(request, f"Цена не задана для блюда «{item.dish}».")
                clients = Client.objects.all()
                return render(
                    request,
                    "orders/form.html",
                    {"form": form, "formset": formset, "title": "Новый заказ", "warnings": warnings, "info": info, "clients": clients, "dish_prices": dish_prices},
                )
                item.save()
            for deleted in formset.deleted_objects:
                deleted.delete()
            _reserve_resources(obj)
            if obj.status in [OrderStatus.CONFIRMED, OrderStatus.READY_TO_SHIP, OrderStatus.SHIPPED] and not obj.deliveries.exists():
                Delivery.objects.create(
                    order=obj,
                    address=obj.address,
                    status=Delivery.DeliveryStatus.UNASSIGNED,
                )
            messages.success(request, "Заказ создан.")
            return redirect("/orders/")
    clients = Client.objects.all()
    return render(
        request,
        "orders/form.html",
        {"form": form, "formset": formset, "title": "Новый заказ", "clients": clients, "dish_prices": dish_prices},
    )


@roles_required(["Менеджер", "Администратор системы"])
def order_edit(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=obj)
    formset = OrderItemFormSet(request.POST or None, queryset=obj.items.all())
    dish_prices = {d.id: float(d.default_price) for d in Dish.objects.filter(is_active=True, default_price__isnull=False)}
    if request.method == "POST" and form.is_valid() and formset.is_valid():
        with transaction.atomic():
            order = form.save()
            action = request.POST.get("action", "save")
            order.status = OrderStatus.DRAFT if action == "draft" else OrderStatus.REVIEW
            _apply_production_fields(order)
            _ensure_order_number(order)
            order.save()
            items = [i for i in formset.save(commit=False) if i.dish]
            if not items:
                messages.error(request, "Добавьте хотя бы одну позицию заказа.")
            return render(
                request,
                "orders/form.html",
                {"form": form, "formset": formset, "title": "Редактирование заказа", "dish_prices": dish_prices},
            )
        errors, warnings, info = _validate_order_capacity(order, items)
        if errors:
            clients = Client.objects.all()
            for err in errors:
                messages.error(request, err)
            return render(
                request,
                "orders/form.html",
                {"form": form, "formset": formset, "title": "Редактирование заказа", "warnings": warnings, "info": info, "clients": clients, "dish_prices": dish_prices},
            )
            capacity_errors = _validate_dish_capacity(order, items)
            if capacity_errors:
                clients = Client.objects.all()
                for err in capacity_errors:
                    messages.error(request, err)
                return render(
                    request,
                    "orders/form.html",
                    {"form": form, "formset": formset, "title": "Редактирование заказа", "warnings": warnings, "info": info, "clients": clients},
                )
            for item in items:
                item.order = order
                try:
                    _attach_tech_card(order, item)
                except ValueError as exc:
                    messages.error(request, str(exc))
                    clients = Client.objects.all()
                return render(
                    request,
                    "orders/form.html",
                    {"form": form, "formset": formset, "title": "Редактирование заказа", "warnings": warnings, "info": info, "clients": clients, "dish_prices": dish_prices},
                )
            if item.unit_price is None and item.dish and item.dish.default_price is not None:
                item.unit_price = item.dish.default_price
            if item.unit_price is None:
                messages.error(request, f"Цена не задана для блюда «{item.dish}».")
                clients = Client.objects.all()
                return render(
                    request,
                    "orders/form.html",
                    {"form": form, "formset": formset, "title": "Редактирование заказа", "warnings": warnings, "info": info, "clients": clients, "dish_prices": dish_prices},
                )
                item.save()
            for deleted in formset.deleted_objects:
                deleted.delete()
            _reserve_resources(order)
            if order.status in [OrderStatus.CONFIRMED, OrderStatus.READY_TO_SHIP, OrderStatus.SHIPPED] and not order.deliveries.exists():
                Delivery.objects.create(
                    order=order,
                    address=order.address,
                    status=Delivery.DeliveryStatus.UNASSIGNED,
                )
            messages.success(request, "Заказ обновлён.")
            return redirect("/orders/")
    clients = Client.objects.all()
    return render(
        request,
        "orders/form.html",
        {"form": form, "formset": formset, "title": "Редактирование заказа", "clients": clients, "dish_prices": dish_prices},
    )


@roles_required(["Менеджер", "Администратор системы"])
def order_availability(request):
    delivery_date = request.GET.get("delivery_date")
    client_id = request.GET.get("client_id")
    order_id = request.GET.get("order_id")
    if not delivery_date:
        return HttpResponseBadRequest("delivery_date обязателен")
    max_capacity = getattr(settings, "PRODUCTION_MAX_WEIGHT_KG", None)
    reserved_map = _get_reserved_qty_map(delivery_date, exclude_order_id=order_id)
    reserved_capacity = ProductionReservation.objects.filter(production_date=delivery_date).aggregate(
        total=Sum("weight_kg")
    )["total"] or 0
    dishes = []
    for dish in Dish.objects.filter(is_active=True).order_by("name"):
        daily_capacity = float(dish.daily_capacity) if dish.daily_capacity is not None else None
        reserved_qty = float(reserved_map.get(dish.id, 0) or 0)
        available_qty = None
        if daily_capacity is not None:
            available_qty = max(daily_capacity - reserved_qty, 0)
        weight_per_unit = float(dish.unit_weight_kg) if dish.unit_weight_kg is not None else None
        max_by_capacity = None
        if max_capacity is not None:
            if dish.base_uom == Dish.BaseUom.KG:
                max_by_capacity = max_capacity - reserved_capacity
            elif dish.base_uom == Dish.BaseUom.PCS and weight_per_unit:
                max_by_capacity = (max_capacity - reserved_capacity) / weight_per_unit
        dishes.append(
            {
                "dish_id": dish.id,
                "dish_name": dish.name,
                "unit": dish.unit,
                "base_uom": dish.base_uom,
                "quantity_scale": dish.quantity_scale,
                "weight_per_unit_kg": weight_per_unit,
                "daily_capacity": daily_capacity,
                "reserved_qty": round(reserved_qty, 3),
                "available_qty": round(available_qty, 3) if available_qty is not None else None,
                "max_by_capacity": round(max_by_capacity, 3) if max_by_capacity is not None else None,
                "min_batch": float(dish.min_batch_qty) if dish.min_batch_qty else None,
                "step": float(dish.batch_multiple_qty) if dish.batch_multiple_qty else None,
                "price": float(dish.default_price) if dish.default_price is not None else None,
            }
        )
    return JsonResponse(
        {
            "production_date": delivery_date,
            "capacity_total": max_capacity if max_capacity is not None else 0,
            "capacity_reserved": reserved_capacity,
            "capacity_available": max_capacity - reserved_capacity if max_capacity is not None else 0,
            "dishes": dishes,
        }
    )


@roles_required(["Менеджер", "Администратор системы"])
def order_delete(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Заказ удалён.")
        return redirect("/orders/")
    return render(request, "orders/delete.html", {"object": obj})

@roles_required(["Менеджер", "Администратор системы"])
def order_archive(request):
    qs = Order.objects.select_related("client").filter(is_archived=True)
    return render(request, "orders/archive.html", {"orders": qs, "statuses": OrderStatus.choices})


@roles_required(["Менеджер", "Администратор системы"])
def order_bulk_delete(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST обязателен")
    ids = request.POST.getlist("order_ids")
    if not ids:
        messages.error(request, "Выберите заказы для удаления.")
        return redirect("/orders/")
    qs = Order.objects.filter(id__in=ids)
    count = qs.count()
    qs.delete()
    messages.success(request, f"Удалено заказов: {count}.")
    return redirect("/orders/")


@roles_required(["Менеджер", "Сборщик заказов"])
def order_status_update(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        status = request.POST.get("status")
        if status in dict(OrderStatus.choices):
            obj.status = status
            obj.save(update_fields=["status"])
            if status in [OrderStatus.CONFIRMED, OrderStatus.READY_TO_SHIP, OrderStatus.SHIPPED] and not obj.deliveries.exists():
                Delivery.objects.create(
                    order=obj,
                    address=obj.address,
                    status=Delivery.DeliveryStatus.UNASSIGNED,
                )
                messages.success(request, "Доставка создана автоматически.")
            messages.success(request, "Статус заказа обновлён.")
    return redirect(request.META.get("HTTP_REFERER", "/orders/"))


@roles_required(["Менеджер", "Администратор системы"])
def order_archive_toggle(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        obj.is_archived = not obj.is_archived
        obj.save(update_fields=["is_archived"])
        messages.success(request, "Статус архива обновлён.")
    return redirect(request.META.get("HTTP_REFERER", "/orders/"))


@role_required("Сборщик заказов")
def picker_orders(request):
    qs = Order.objects.select_related("client").filter(is_archived=False)
    status = request.GET.get("status")
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")
    if status:
        qs = qs.filter(status=status)
    else:
        qs = qs.exclude(status__in=[OrderStatus.SHIPPED, OrderStatus.CANCELLED])
    if date_from:
        qs = qs.filter(created_at__date__gte=date_from)
    if date_to:
        qs = qs.filter(created_at__date__lte=date_to)
    return render(
        request,
        "orders/picker_list.html",
        {"orders": qs, "statuses": OrderStatus.choices},
    )


@role_required("Сборщик заказов")
def picker_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    items_qs = order.items.all()
    session, _ = PickingSession.objects.get_or_create(order=order, defaults={"picker": request.user})
    if not session.started_at:
        session.started_at = timezone.now()
        session.picker = request.user
        session.save(update_fields=["started_at", "picker"])

    formset = OrderItemPickFormSet(request.POST or None, queryset=items_qs)
    session_form = PickingSessionForm(request.POST or None, instance=session, prefix="session")

    if request.method == "POST":
        action = request.POST.get("action", "save")
        if formset.is_valid() and session_form.is_valid():
            formset.save()
            session_form.save()

            if action == "finish":
                final_statuses = {
                    OrderItem.ItemStatus.DONE,
                    OrderItem.ItemStatus.OUT_OF_STOCK,
                    OrderItem.ItemStatus.REPLACED,
                }
                if items_qs.exclude(item_status__in=final_statuses).exists():
                    messages.error(request, "Не все позиции имеют итоговый статус.")
                else:
                    order.status = OrderStatus.SHIPPED
                    order.save(update_fields=["status"])
                    session.finished_at = timezone.now()
                    session.save(update_fields=["finished_at"])
                    if not order.deliveries.exists():
                        Delivery.objects.create(
                            order=order,
                            address=order.address,
                            status=Delivery.DeliveryStatus.UNASSIGNED,
                        )
                    messages.success(request, "Сборка завершена. Заказ передан в доставку.")
            else:
                messages.success(request, "Изменения сохранены.")
        else:
            messages.error(request, "Проверьте данные: есть ошибки в позициях.")

    return render(
        request,
        "orders/picker_detail.html",
        {
            "order": order,
            "formset": formset,
            "session_form": session_form,
            "session": session,
        },
    )

# Create your views here.
```

45. logistics/__init__.py
```python
```

46. logistics/admin.py
```python
from django.contrib import admin

# Register your models here.
```

47. logistics/apps.py
```python
from django.apps import AppConfig


class LogisticsConfig(AppConfig):
    name = 'logistics'
```

48. logistics/forms.py
```python
from django import forms
from django.conf import settings
from crm.forms import BootstrapFormMixin
from crm.models import Delivery, Route, RouteStop, CourierAssignment, LogisticianProfile, Courier


class DeliveryForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Delivery
        fields = [
            "courier",
            "route",
            "status",
            "planned_at",
            "departure_time",
            "delivered_at",
            "address",
            "cargo_weight_kg",
            "cargo_volume_m3",
            "cargo_length_cm",
            "cargo_width_cm",
            "cargo_height_cm",
            "note",
        ]
        labels = {
            "courier": "Курьер",
            "route": "Маршрут",
            "status": "Статус доставки",
            "planned_at": "Плановая дата/время",
            "departure_time": "Время выезда",
            "delivered_at": "Время доставки",
            "address": "Адрес",
            "cargo_weight_kg": "Вес груза (кг)",
            "cargo_volume_m3": "Объём груза (м³)",
            "cargo_length_cm": "Длина груза (см)",
            "cargo_width_cm": "Ширина груза (см)",
            "cargo_height_cm": "Высота груза (см)",
            "note": "Примечание",
        }
        widgets = {
            "planned_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
            "departure_time": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
            "delivered_at": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        if "status" in self.fields:
            allowed = ["Не назначено", "Запланировано"]
            self.fields["status"].choices = [
                (value, label)
                for value, label in self.fields["status"].choices
                if value in allowed
            ]
        for name in ("planned_at", "departure_time", "delivered_at"):
            if name in self.fields:
                self.fields[name].input_formats = ["%Y-%m-%dT%H:%M"]

    def clean(self):
        cleaned = super().clean()
        status = cleaned.get("status")
        courier = cleaned.get("courier")
        route = cleaned.get("route")
        planned_at = cleaned.get("planned_at")
        departure_time = cleaned.get("departure_time")
        delivered_at = cleaned.get("delivered_at")
        note = cleaned.get("note")

        if status in ["Запланировано", "В пути", "Доставлено"] and not courier:
            self.add_error("courier", "Нужно назначить курьера.")
        if status in ["Запланировано", "В пути", "Доставлено"] and not planned_at:
            self.add_error("planned_at", "Нужно указать плановую дату/время.")
        if status in ["В пути", "Доставлено"] and not route:
            self.add_error("route", "Для статуса «В пути/Доставлено» нужен маршрут.")
        if status == "В пути" and not departure_time:
            self.add_error("departure_time", "Нужно указать время выезда.")
        if status == "Доставлено" and not delivered_at:
            self.add_error("delivered_at", "Нужно указать время доставки.")
        if status == "Доставлено" and route and route.status != "Завершён":
            self.add_error("status", "Нельзя отметить «Доставлено», пока маршрут не завершён.")
        if status == "Отменено" and not note:
            self.add_error("note", "Укажите причину отмены.")
        return cleaned


class RouteForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Route
        fields = ["planned_date", "status", "max_duration_minutes", "soft_limit_stops", "strict_mode", "notes"]
        labels = {
            "planned_date": "Дата маршрута",
            "status": "Статус",
            "max_duration_minutes": "Макс. длительность (мин)",
            "soft_limit_stops": "Мягкий лимит точек",
            "strict_mode": "Строгий режим лимита",
            "notes": "Заметки",
        }
        widgets = {
            "planned_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()


class RouteStopForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = RouteStop
        fields = ["delivery", "planned_time", "note", "status", "service_time_minutes"]
        labels = {
            "delivery": "Доставка",
            "planned_time": "Плановое время",
            "note": "Примечание",
            "status": "Статус",
            "service_time_minutes": "Время обслуживания (мин)",
        }
        widgets = {
            "planned_time": forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        if "planned_time" in self.fields:
            self.fields["planned_time"].input_formats = ["%Y-%m-%dT%H:%M"]
        if "service_time_minutes" in self.fields and not self.instance.pk:
            self.fields["service_time_minutes"].initial = getattr(settings, "LOGISTICS_SERVICE_TIME_MINUTES", 15)
        if "status" in self.fields:
            allowed = ["Черновик", "Подтверждена", "Запланирована"]
            self.fields["status"].choices = [
                (value, label)
                for value, label in self.fields["status"].choices
                if value in allowed
            ]


class CourierStopStatusForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = RouteStop
        fields = ["status", "failure_reason", "note"]
        labels = {
            "status": "Статус",
            "failure_reason": "Причина",
            "note": "Комментарий",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        if "status" in self.fields:
            allowed = ["В пути", "Не доставлено"]
            self.fields["status"].choices = [
                (value, label)
                for value, label in self.fields["status"].choices
                if value in allowed
            ]


class ProofUploadForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = RouteStop
        fields = ["proof_of_delivery"]
        labels = {"proof_of_delivery": "Документ доставки"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()


class CourierAssignmentForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = CourierAssignment
        fields = ["courier"]
        labels = {"courier": "Курьер"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()


class LogisticianProfileForm(BootstrapFormMixin, forms.ModelForm):
    transport_types = forms.MultipleChoiceField(
        label="Доступные типы транспорта",
        required=False,
        choices=[
            ("bike", "Вело"),
            ("car", "Легковой"),
            ("van", "Фургон"),
            ("truck", "Грузовик"),
        ],
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = LogisticianProfile
        fields = [
            "region",
            "city",
            "transport_types",
            "timezone",
            "map_show_traffic",
            "preferred_route_type",
        ]
        labels = {
            "region": "Регион",
            "city": "Город",
            "timezone": "Часовой пояс",
            "map_show_traffic": "Пробки на карте",
            "preferred_route_type": "Тип маршрута",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        self.fields["transport_types"].initial = self.instance.transport_types or []

    def clean_transport_types(self):
        return self.cleaned_data.get("transport_types") or []


class CourierProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Courier
        fields = [
            "transport_type",
            "payload_capacity_kg",
            "cargo_volume_m3",
            "cargo_length_cm",
            "cargo_width_cm",
            "cargo_height_cm",
            "zone",
            "experience_years",
        ]
        labels = {
            "transport_type": "Тип транспорта",
            "payload_capacity_kg": "Грузоподъёмность (кг)",
            "cargo_volume_m3": "Объём кузова (м³)",
            "cargo_length_cm": "Длина кузова (см)",
            "cargo_width_cm": "Ширина кузова (см)",
            "cargo_height_cm": "Высота кузова (см)",
            "zone": "Зона",
            "experience_years": "Опыт (лет)",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
```

49. logistics/models.py
```python
from django.db import models

# Create your models here.
```

50. logistics/tests.py
```python
from django.test import TestCase
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

from crm.models import (
    Role,
    User,
    Client,
    Order,
    Delivery,
    Route,
    RouteStop,
    Courier,
    CourierAssignment,
    RouteStatus,
)


class LogisticsRulesTests(TestCase):
    def setUp(self):
        self.logist_role = Role.objects.create(name="Логист")
        self.courier_role = Role.objects.create(name="Курьер")
        self.logist = User.objects.create_user(
            username="logist",
            password="Pass123!",
            email="logist@test.com",
            full_name="Логист",
        )
        self.logist.roles.add(self.logist_role)
        self.courier_user = User.objects.create_user(
            username="courier",
            password="Pass123!",
            email="courier@test.com",
            full_name="Курьер",
        )
        self.courier_user.roles.add(self.courier_role)
        self.courier = Courier.objects.create(user=self.courier_user, status="Свободен")

        self.client_obj = Client.objects.create(name="Test", client_type="store")
        self.order = Order.objects.create(
            order_number="ORD-1",
            client=self.client_obj,
            status="confirmed",
            address="Москва",
            total_amount=1000,
        )

    def test_cannot_add_stop_with_different_date(self):
        route = Route.objects.create(planned_date=timezone.now().date(), logistician=self.logist)
        delivery = Delivery.objects.create(
            order=self.order,
            status="Запланировано",
            planned_at=timezone.now() + timezone.timedelta(days=1),
        )
        self.client.force_login(self.logist)
        response = self.client.post(
            f"/logistics/routes/{route.id}/",
            {"action": "add_stop", "stop-delivery": delivery.id, "stop-status": "Запланирована"},
        )
        self.assertEqual(response.status_code, 400)

    def test_publish_blocked_by_duration(self):
        route = Route.objects.create(
            planned_date=timezone.now().date(),
            logistician=self.logist,
            max_duration_minutes=10,
        )
        CourierAssignment.objects.create(route=route, courier=self.courier)
        delivery = Delivery.objects.create(
            order=self.order,
            status="Запланировано",
            planned_at=timezone.now(),
            cargo_weight_kg=10,
            cargo_volume_m3=1,
        )
        RouteStop.objects.create(
            route=route,
            delivery=delivery,
            sequence_index=1,
            service_time_minutes=30,
            status="Запланирована",
            latitude=55.8,
            longitude=37.6,
        )
        self.client.force_login(self.logist)
        response = self.client.post(f"/logistics/routes/{route.id}/", {"action": "publish_route"})
        self.assertEqual(response.status_code, 400)

    def test_courier_cannot_deliver_without_proof(self):
        route = Route.objects.create(
            planned_date=timezone.now().date(),
            logistician=self.logist,
            status=RouteStatus.PUBLISHED,
        )
        CourierAssignment.objects.create(route=route, courier=self.courier)
        delivery = Delivery.objects.create(
            order=self.order,
            status="Запланировано",
            planned_at=timezone.now(),
        )
        stop = RouteStop.objects.create(
            route=route,
            delivery=delivery,
            sequence_index=1,
            status="Запланирована",
        )
        self.client.force_login(self.courier_user)
        response = self.client.post(f"/logistics/courier/stops/{stop.id}/proof/", {"status": "Доставлено"})
        self.assertEqual(response.status_code, 400)

        file = SimpleUploadedFile("proof.pdf", b"test", content_type="application/pdf")
        response = self.client.post(
            f"/logistics/courier/stops/{stop.id}/proof/",
            {"proof_of_delivery": file, "status": "Доставлено"},
        )
        self.assertEqual(response.status_code, 302)
```

51. logistics/urls.py
```python
from django.urls import path
from .views import (
    deliveries_list,
    delivery_edit,
    delivery_by_order,
    delivery_card,
    couriers_list,
    routes_list,
    route_create,
    route_edit,
    route_detail,
    logistic_profile,
    courier_profile,
    courier_routes,
    courier_route_detail,
    courier_stop_update,
    courier_upload_proof,
    proof_review_list,
    proof_review_update,
)

urlpatterns = [
    path("", deliveries_list, name="logistics-list"),
    path("delivery/<int:pk>/", delivery_card, name="logistics-delivery-card"),
    path("delivery/<int:pk>/edit/", delivery_edit, name="logistics-edit"),
    path("orders/<int:order_id>/delivery/", delivery_by_order, name="logistics-delivery-by-order"),
    path("couriers/", couriers_list, name="logistics-couriers"),
    path("routes/", routes_list, name="logistics-routes"),
    path("routes/create/", route_create, name="logistics-route-create"),
    path("routes/<int:pk>/edit/", route_edit, name="logistics-route-edit"),
    path("routes/<int:pk>/", route_detail, name="logistics-route-detail"),
    path("profile/", logistic_profile, name="logistics-profile"),
    path("courier/profile/", courier_profile, name="courier-profile"),
    path("courier/routes/", courier_routes, name="courier-routes"),
    path("courier/routes/<int:pk>/", courier_route_detail, name="courier-route-detail"),
    path("courier/stops/<int:pk>/update/", courier_stop_update, name="courier-stop-update"),
    path("courier/stops/<int:pk>/proof/", courier_upload_proof, name="courier-stop-proof"),
    path("manager/proofs/", proof_review_list, name="manager-proof-list"),
    path("manager/proofs/<int:pk>/", proof_review_update, name="manager-proof-update"),
]
```

52. logistics/views.py
```python
from urllib.parse import quote
import math

from django.conf import settings
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from accounts.utils import role_required
from crm.models import (
    Delivery,
    Route,
    RouteStatus,
    Courier,
    CourierStatus,
    RouteStop,
    CourierAssignment,
    Order,
    OrderStatus,
    Client,
    LogisticianProfile,
    AuditLog,
)
from .forms import (
    DeliveryForm,
    RouteForm,
    RouteStopForm,
    CourierAssignmentForm,
    LogisticianProfileForm,
    CourierStopStatusForm,
    ProofUploadForm,
    CourierProfileForm,
)


def _build_google_maps_dir_url(addresses):
    if len(addresses) < 2:
        return ""
    origin = quote(addresses[0])
    destination = quote(addresses[-1])
    waypoints = "|".join(quote(a) for a in addresses[1:-1])
    url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}"
    if waypoints:
        url += f"&waypoints={waypoints}"
    return url


def _actor_role(user):
    if not user or not user.is_authenticated:
        return ""
    roles = list(user.roles.values_list("name", flat=True))
    return roles[0] if roles else ""


def _log_action(actor, obj, field_name="", old_value="", new_value="", reason=""):
    AuditLog.objects.create(
        actor=actor if actor and actor.is_authenticated else None,
        actor_role=_actor_role(actor),
        object_type=obj.__class__.__name__,
        object_id=obj.id,
        field_name=field_name,
        old_value=str(old_value or ""),
        new_value=str(new_value or ""),
        reason=reason or "",
    )


def _get_or_create_courier_profile(user):
    courier, created = Courier.objects.get_or_create(user=user)
    return courier, created


def _haversine_km(lat1, lon1, lat2, lon2):
    r = 6371.0
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    d_phi = math.radians(lat2 - lat1)
    d_lambda = math.radians(lon2 - lon1)
    a = math.sin(d_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(d_lambda / 2) ** 2
    return 2 * r * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def _route_metrics(route):
    stops = RouteStop.objects.filter(route=route).select_related("delivery")
    total_weight = sum([(s.delivery.cargo_weight_kg or 0) for s in stops])
    total_volume = sum([(s.delivery.cargo_volume_m3 or 0) for s in stops])
    total_stops = stops.count()
    service_minutes = sum([(s.service_time_minutes or 0) for s in stops])

    points = []
    for s in stops.order_by("sequence_index"):
        if s.latitude is not None and s.longitude is not None:
            points.append((float(s.latitude), float(s.longitude)))

    depot_lat = getattr(settings, "LOGISTICS_DEPOT_LAT", None)
    depot_lng = getattr(settings, "LOGISTICS_DEPOT_LNG", None)
    if depot_lat is not None and depot_lng is not None:
        points_with_depot = [(float(depot_lat), float(depot_lng))] + points
    else:
        points_with_depot = points

    distance_km = 0
    for idx in range(1, len(points_with_depot)):
        lat1, lon1 = points_with_depot[idx - 1]
        lat2, lon2 = points_with_depot[idx]
        distance_km += _haversine_km(lat1, lon1, lat2, lon2)

    if getattr(settings, "LOGISTICS_RETURN_TO_DEPOT", False) and depot_lat is not None and depot_lng is not None and points:
        lat1, lon1 = points[-1]
        distance_km += _haversine_km(lat1, lon1, float(depot_lat), float(depot_lng))

    avg_speed = getattr(settings, "LOGISTICS_AVG_SPEED_KMH", 35)
    travel_minutes = (distance_km / avg_speed) * 60 if avg_speed else 0
    duration_minutes = int(travel_minutes + service_minutes)

    return {
        "total_weight": total_weight,
        "total_volume": total_volume,
        "total_stops": total_stops,
        "distance_km": round(distance_km, 1),
        "duration_minutes": duration_minutes,
        "service_minutes": service_minutes,
        "travel_minutes": int(travel_minutes),
    }


def _route_validation(route):
    metrics = _route_metrics(route)
    errors = []
    warnings = []

    if metrics["duration_minutes"] > route.max_duration_minutes:
        errors.append(
            f"Превышение лимита времени: {metrics['duration_minutes']} мин > {route.max_duration_minutes} мин"
        )

    courier = None
    assignment = CourierAssignment.objects.filter(route=route).select_related("courier").first()
    if assignment:
        courier = assignment.courier
    capacity_weight = (courier.max_weight if courier else None) or (courier.payload_capacity_kg if courier else None)
    capacity_volume = (courier.max_volume if courier else None) or (courier.cargo_volume_m3 if courier else None)
    if capacity_weight and metrics["total_weight"] > capacity_weight:
        errors.append("Превышение лимита веса")
    if capacity_volume and metrics["total_volume"] > capacity_volume:
        errors.append("Превышение лимита объёма")

    if metrics["total_stops"] > route.soft_limit_stops:
        message = f"Превышен мягкий лимит точек: {metrics['total_stops']} > {route.soft_limit_stops}"
        if route.strict_mode:
            errors.append(message)
        else:
            warnings.append(message)

    return metrics, errors, warnings

def _courier_is_suitable(delivery, courier):
    if courier.status != CourierStatus.FREE:
        return False
    capacity_weight = courier.max_weight or courier.payload_capacity_kg
    capacity_volume = courier.max_volume or courier.cargo_volume_m3
    if delivery.cargo_weight_kg and not capacity_weight:
        return False
    if delivery.cargo_weight_kg and capacity_weight and delivery.cargo_weight_kg > capacity_weight:
        return False
    if delivery.cargo_volume_m3 and not capacity_volume:
        return False
    if delivery.cargo_volume_m3 and capacity_volume and delivery.cargo_volume_m3 > capacity_volume:
        return False
    for delivery_dim, courier_dim in [
        (delivery.cargo_length_cm, courier.cargo_length_cm),
        (delivery.cargo_width_cm, courier.cargo_width_cm),
        (delivery.cargo_height_cm, courier.cargo_height_cm),
    ]:
        if delivery_dim and not courier_dim:
            return False
        if delivery_dim and courier_dim and delivery_dim > courier_dim:
            return False
    return True


def _normalize_route_stop_sequence(route):
    stops = RouteStop.objects.filter(route=route).order_by("sequence_index", "id")
    for idx, stop in enumerate(stops, start=1):
        if stop.sequence_index != idx:
            RouteStop.objects.filter(pk=stop.pk).update(sequence_index=idx)


@role_required("Логист")
def deliveries_list(request):
    deliveries = Delivery.objects.select_related("order", "courier", "route").all()
    status = request.GET.get("status")
    date = request.GET.get("date")
    courier_id = request.GET.get("courier")
    route_id = request.GET.get("route")
    client_id = request.GET.get("client")
    sort = request.GET.get("sort")
    if status:
        deliveries = deliveries.filter(status=status)
    else:
        deliveries = deliveries.exclude(status__in=[Delivery.DeliveryStatus.DELIVERED, Delivery.DeliveryStatus.CANCELLED])
    if date:
        deliveries = deliveries.filter(planned_at__date=date)
    if courier_id:
        deliveries = deliveries.filter(courier_id=courier_id)
    if route_id:
        deliveries = deliveries.filter(route_id=route_id)
    if client_id:
        deliveries = deliveries.filter(order__client_id=client_id)
    if sort in ["planned_at", "-planned_at", "status", "-status"]:
        deliveries = deliveries.order_by(sort)
    if sort in ["client", "-client"]:
        deliveries = deliveries.order_by(f"{'-' if sort.startswith('-') else ''}order__client__name")
    orders_without_delivery = Order.objects.filter(
        is_archived=False,
        status__in=[
            OrderStatus.CONFIRMED,
            OrderStatus.IN_PRODUCTION,
            OrderStatus.READY_TO_SHIP,
            OrderStatus.SHIPPED,
        ],
        deliveries__isnull=True,
    ).select_related("client")
    couriers = Courier.objects.select_related("user").all()
    routes = Route.objects.all()
    clients = Client.objects.all()

    if request.GET.get("export") == "1":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename=deliveries.csv"
        response.write("Номер заказа;Клиент;Адрес;План;Курьер;Маршрут;Статус\n")
        for d in deliveries:
            response.write(
                f"{d.order.order_number};{d.order.client.name};{d.address or ''};"
                f"{d.planned_at or ''};{d.courier.user.full_name if d.courier else ''};"
                f"{d.route.planned_date if d.route else ''};{d.get_status_display()}\n"
            )
        return response
    return render(
        request,
        "logistics/list.html",
        {
            "deliveries": deliveries,
            "status_choices": Delivery.DeliveryStatus.choices,
            "orders_without_delivery": orders_without_delivery,
            "couriers": couriers,
            "routes": routes,
            "clients": clients,
        },
    )


@role_required("Логист")
def delivery_edit(request, pk):
    obj = get_object_or_404(Delivery, pk=pk)
    form = DeliveryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Доставка обновлена.")
        return redirect(f"/logistics/delivery/{obj.id}/")
    return render(request, "logistics/delivery_card.html", {"form": form, "delivery": obj, "title": "Карточка доставки"})


@role_required("Логист")
def delivery_by_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    delivery, _ = Delivery.objects.get_or_create(
        order=order,
        defaults={"address": order.address, "status": Delivery.DeliveryStatus.UNASSIGNED},
    )
    return redirect(f"/logistics/delivery/{delivery.id}/")


@role_required("Логист")
def delivery_card(request, pk):
    obj = get_object_or_404(Delivery, pk=pk)
    form = DeliveryForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        delivery = form.save()
        if delivery.status == Delivery.DeliveryStatus.DELIVERED and not delivery.delivered_at:
            delivery.delivered_at = delivery.delivered_at or delivery.planned_at
            delivery.save(update_fields=["delivered_at"])
        messages.success(request, "Доставка обновлена.")
        return redirect(f"/logistics/delivery/{obj.id}/")
    couriers = Courier.objects.select_related("user").all()
    suitable_couriers = [c for c in couriers if _courier_is_suitable(obj, c)]
    profile, _ = LogisticianProfile.objects.get_or_create(user=request.user)
    destination = obj.address or obj.order.address
    origin = getattr(settings, "LOGISTICS_DEPOT_ADDRESS", "Химки")
    delivery_map_payload = {
        "origin": origin,
        "destination": destination,
    }
    return render(
        request,
        "logistics/delivery_card.html",
        {
            "form": form,
            "delivery": obj,
            "title": "Карточка доставки",
            "suitable_couriers": suitable_couriers,
            "delivery_map_payload": delivery_map_payload,
            "map_prefs": profile,
        },
    )

@role_required("Логист")
def couriers_list(request):
    couriers = Courier.objects.select_related("user").all()
    status = request.GET.get("status")
    transport = request.GET.get("transport")
    zone = request.GET.get("zone")
    min_payload = request.GET.get("min_payload")
    min_volume = request.GET.get("min_volume")
    sort = request.GET.get("sort")

    if status:
        couriers = couriers.filter(status=status)
    if transport:
        couriers = couriers.filter(transport_type__iexact=transport)
    if zone:
        couriers = couriers.filter(zone__icontains=zone)
    if min_payload:
        couriers = couriers.filter(payload_capacity_kg__gte=min_payload)
    if min_volume:
        couriers = couriers.filter(cargo_volume_m3__gte=min_volume)

    sort_map = {
        "name": "user__full_name",
        "-name": "-user__full_name",
        "status": "status",
        "-status": "-status",
        "payload": "payload_capacity_kg",
        "-payload": "-payload_capacity_kg",
        "updated": "location_updated_at",
        "-updated": "-location_updated_at",
    }
    if sort in sort_map:
        couriers = couriers.order_by(sort_map[sort])

    transport_types = (
        Courier.objects.exclude(transport_type="")
        .values_list("transport_type", flat=True)
        .distinct()
        .order_by("transport_type")
    )
    return render(
        request,
        "logistics/couriers.html",
        {
            "couriers": couriers,
            "status_choices": CourierStatus.choices,
            "transport_types": transport_types,
        },
    )


@role_required("Логист")
def routes_list(request):
    routes = Route.objects.select_related("logistician").all()
    return render(request, "logistics/routes.html", {"routes": routes})


@role_required("Логист")
def route_create(request):
    form = RouteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.logistician = request.user
        obj.save()
        messages.success(request, "Маршрут создан.")
        return redirect("/logistics/routes/")
    return render(request, "logistics/route_form.html", {"form": form, "title": "Новый маршрут"})


@role_required("Логист")
def route_edit(request, pk):
    route = get_object_or_404(Route, pk=pk)
    form = RouteForm(request.POST or None, instance=route)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Маршрут обновлён.")
        return redirect("/logistics/routes/")
    return render(request, "logistics/route_form.html", {"form": form, "title": "Редактирование маршрута"})


@role_required("Логист")
def route_detail(request, pk):
    route = get_object_or_404(Route, pk=pk)
    stops = RouteStop.objects.filter(route=route).select_related("delivery", "delivery__order")
    assignments = CourierAssignment.objects.filter(route=route).select_related("courier", "courier__user")

    stop_form = RouteStopForm(prefix="stop")
    stop_form.fields["delivery"].queryset = Delivery.objects.exclude(route_stops__route=route)
    assign_form = CourierAssignmentForm(prefix="assign")
    assign_form.fields["courier"].queryset = Courier.objects.exclude(assignments__route=route)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add_stop":
            stop_form = RouteStopForm(request.POST, prefix="stop")
            stop_form.fields["delivery"].queryset = Delivery.objects.exclude(route_stops__route=route)
            delivery_id = request.POST.get("stop-delivery")
            if delivery_id:
                delivery = get_object_or_404(Delivery, pk=delivery_id)
                delivery_date = delivery.delivery_date or (delivery.planned_at.date() if delivery.planned_at else None)
                if not delivery_date:
                    return HttpResponseBadRequest("У доставки не задана дата.")
                if delivery_date != route.planned_date:
                    return HttpResponseBadRequest("Нельзя добавить точку другой даты доставки.")
            if stop_form.is_valid():
                obj = stop_form.save(commit=False)
                obj.route = route
                last = RouteStop.objects.filter(route=route).order_by("-sequence_index").first()
                obj.sequence_index = (last.sequence_index + 1) if last else 1
                obj.save()
                _normalize_route_stop_sequence(route)
                _log_action(request.user, route, "stops", "", f"Добавлена остановка {obj.id}")
                messages.success(request, "Остановка добавлена.")
                return redirect(f"/logistics/routes/{route.id}/")
        if action == "assign_courier":
            assign_form = CourierAssignmentForm(request.POST, prefix="assign")
            assign_form.fields["courier"].queryset = Courier.objects.exclude(assignments__route=route)
            if assign_form.is_valid():
                obj = assign_form.save(commit=False)
                obj.route = route
                obj.save()
                _log_action(request.user, route, "courier", "", obj.courier_id)
                messages.success(request, "Курьер назначен.")
                return redirect(f"/logistics/routes/{route.id}/")
        if action in ["move_up", "move_down"]:
            stop_id = request.POST.get("stop_id")
            stop = get_object_or_404(RouteStop, pk=stop_id, route=route)
            delta = -1 if action == "move_up" else 1
            target = RouteStop.objects.filter(route=route, sequence_index=stop.sequence_index + delta).first()
            if target:
                RouteStop.objects.filter(pk=stop.pk).update(sequence_index=target.sequence_index)
                RouteStop.objects.filter(pk=target.pk).update(sequence_index=stop.sequence_index)
                _normalize_route_stop_sequence(route)
                _log_action(request.user, route, "sequence", "", "reorder")
                messages.success(request, "Порядок остановок обновлён.")
            return redirect(f"/logistics/routes/{route.id}/")
        if action == "remove_stop":
            stop_id = request.POST.get("stop_id")
            reason = request.POST.get("reason", "")
            stop = get_object_or_404(RouteStop, pk=stop_id, route=route)
            old_status = stop.status
            stop.status = RouteStop.StopStatus.CANCELLED
            stop.save(update_fields=["status"])
            _normalize_route_stop_sequence(route)
            _log_action(request.user, stop, "status", old_status, stop.status, reason or "Удалена из маршрута")
            messages.success(request, "Остановка удалена из маршрута.")
            return redirect(f"/logistics/routes/{route.id}/")
        if action == "publish_route":
            metrics, errors, warnings = _route_validation(route)
            if errors:
                return HttpResponseBadRequest("; ".join(errors))
            old_status = route.status
            route.status = RouteStatus.PUBLISHED
            route.save(update_fields=["status"])
            RouteStop.objects.filter(route=route, status__in=[RouteStop.StopStatus.DRAFT, RouteStop.StopStatus.CONFIRMED]).update(
                status=RouteStop.StopStatus.PLANNED
            )
            _log_action(request.user, route, "status", old_status, route.status, "Публикация маршрута")
            messages.success(request, "Маршрут опубликован.")
            return redirect(f"/logistics/routes/{route.id}/")

    stop_points = []
    for s in stops:
        address = s.delivery.address or s.delivery.order.address
        stop_points.append(
            {
                "id": s.id,
                "sequence": s.sequence_index,
                "status": s.status,
                "address": address,
                "lat": float(s.latitude) if s.latitude is not None else None,
                "lng": float(s.longitude) if s.longitude is not None else None,
            }
        )
    map_payload = {"route_id": route.id, "stops": stop_points}
    profile, _ = LogisticianProfile.objects.get_or_create(user=request.user)
    metrics, errors, warnings = _route_validation(route)
    if not errors and route.status == RouteStatus.DRAFT:
        old_status = route.status
        route.status = RouteStatus.PLANNED
        route.save(update_fields=["status"])
        _log_action(request.user, route, "status", old_status, route.status, "Авто-переход при валидности")

    return render(
        request,
        "logistics/route_detail.html",
        {
            "route": route,
            "stops": stops,
            "assignments": assignments,
            "stop_form": stop_form,
            "assign_form": assign_form,
            "map_payload": map_payload,
            "map_prefs": profile,
            "total_points": metrics["total_stops"],
            "total_weight": metrics["total_weight"],
            "total_volume": metrics["total_volume"],
            "route_distance_km": metrics["distance_km"],
            "route_duration_minutes": metrics["duration_minutes"],
            "route_errors": errors,
            "route_warnings": warnings,
        },
    )

# Create your views here.


@role_required("Логист")
def logistic_profile(request):
    profile, _ = LogisticianProfile.objects.get_or_create(user=request.user)
    form = LogisticianProfileForm(request.POST or None, instance=profile)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Профиль логиста обновлён.")
        return redirect("/logistics/profile/")
    return render(
        request,
        "logistics/profile.html",
        {
            "form": form,
            "profile": profile,
        },
    )


@role_required("Курьер")
def courier_routes(request):
    courier, created = _get_or_create_courier_profile(request.user)
    if created:
        messages.info(request, "Профиль курьера создан автоматически. Заполните данные профиля.")
    date = request.GET.get("date")
    assignments = CourierAssignment.objects.filter(courier=courier).select_related("route")
    routes = [a.route for a in assignments]
    if date:
        routes = [r for r in routes if str(r.planned_date) == date]
    return render(request, "courier/routes.html", {"routes": routes})


@role_required("Курьер")
def courier_route_detail(request, pk):
    courier, _ = _get_or_create_courier_profile(request.user)
    route = get_object_or_404(Route, pk=pk)
    if not CourierAssignment.objects.filter(route=route, courier=courier).exists():
        return HttpResponseBadRequest("Маршрут недоступен.")
    stops = RouteStop.objects.filter(route=route).select_related("delivery", "delivery__order")
    stop_form = CourierStopStatusForm()
    proof_form = ProofUploadForm()
    return render(
        request,
        "courier/route_detail.html",
        {"route": route, "stops": stops, "stop_form": stop_form, "proof_form": proof_form},
    )


@role_required("Курьер")
def courier_stop_update(request, pk):
    courier, _ = _get_or_create_courier_profile(request.user)
    stop = get_object_or_404(RouteStop, pk=pk)
    if not CourierAssignment.objects.filter(route=stop.route, courier=courier).exists():
        return HttpResponseBadRequest("Остановка недоступна.")
    form = CourierStopStatusForm(request.POST, instance=stop)
    if request.method == "POST" and form.is_valid():
        new_status = form.cleaned_data["status"]
        if stop.status not in [RouteStop.StopStatus.IN_PROGRESS, RouteStop.StopStatus.PLANNED]:
            return HttpResponseBadRequest("Нельзя изменить статус этой остановки.")
        if new_status == RouteStop.StopStatus.IN_PROGRESS and stop.route.status not in [
            RouteStatus.PUBLISHED,
            RouteStatus.IN_PROGRESS,
        ]:
            return HttpResponseBadRequest("Маршрут ещё не опубликован.")
        if new_status == RouteStop.StopStatus.DONE:
            if not stop.proof_of_delivery:
                return HttpResponseBadRequest("Документ доставки обязателен.")
        if new_status == RouteStop.StopStatus.FAILED and not form.cleaned_data.get("failure_reason"):
            return HttpResponseBadRequest("Укажите причину недоставки.")
        old_status = stop.status
        stop = form.save(commit=False)
        if new_status in [RouteStop.StopStatus.DONE, RouteStop.StopStatus.FAILED]:
            stop.actual_time = timezone.now()
        stop.save()
        if new_status == RouteStop.StopStatus.IN_PROGRESS and stop.route.status == RouteStatus.PUBLISHED:
            stop.route.status = RouteStatus.IN_PROGRESS
            stop.route.save(update_fields=["status"])
        if new_status in [RouteStop.StopStatus.DONE, RouteStop.StopStatus.FAILED]:
            remaining = RouteStop.objects.filter(
                route=stop.route,
                status__in=[
                    RouteStop.StopStatus.DRAFT,
                    RouteStop.StopStatus.CONFIRMED,
                    RouteStop.StopStatus.PLANNED,
                    RouteStop.StopStatus.IN_PROGRESS,
                ],
            ).exists()
            if not remaining:
                stop.route.status = RouteStatus.DONE
                stop.route.save(update_fields=["status"])
        _log_action(request.user, stop, "status", old_status, new_status)
        messages.success(request, "Статус остановки обновлён.")
    return redirect(f"/courier/routes/{stop.route.id}/")


@role_required("Курьер")
def courier_upload_proof(request, pk):
    courier, _ = _get_or_create_courier_profile(request.user)
    stop = get_object_or_404(RouteStop, pk=pk)
    if not CourierAssignment.objects.filter(route=stop.route, courier=courier).exists():
        return HttpResponseBadRequest("Остановка недоступна.")
    form = ProofUploadForm(request.POST or None, request.FILES or None, instance=stop)
    if request.method == "POST" and form.is_valid():
        uploaded = request.FILES.get("proof_of_delivery")
        if uploaded:
            ext = f".{uploaded.name.split('.')[-1].lower()}" if "." in uploaded.name else ""
            allowed = getattr(settings, "LOGISTICS_ALLOWED_PROOF_EXT", [".pdf", ".jpg", ".jpeg", ".png"])
            if ext not in allowed:
                return HttpResponseBadRequest("Недопустимый формат файла.")
        else:
            return HttpResponseBadRequest("Документ доставки обязателен.")
        stop = form.save(commit=False)
        stop.proof_uploaded_at = timezone.now()
        stop.proof_uploaded_by = request.user
        stop.proof_review_status = RouteStop.ProofReviewStatus.PENDING
        if request.POST.get("status") == RouteStop.StopStatus.DONE:
            stop.status = RouteStop.StopStatus.DONE
            stop.actual_time = timezone.now()
        stop.save(
            update_fields=[
                "proof_of_delivery",
                "proof_uploaded_at",
                "proof_uploaded_by",
                "proof_review_status",
                "status",
                "actual_time",
            ]
        )
        _log_action(request.user, stop, "proof_of_delivery", "", stop.proof_of_delivery.name)
        messages.success(request, "Документ загружен.")
    return redirect(f"/courier/routes/{stop.route.id}/")


@role_required("Менеджер")
def proof_review_list(request):
    stops = RouteStop.objects.filter(proof_of_delivery__isnull=False).select_related("route", "delivery", "delivery__order")
    status = request.GET.get("status")
    if status:
        stops = stops.filter(proof_review_status=status)
    return render(request, "manager/proof_review_list.html", {"stops": stops})


@role_required("Менеджер")
def proof_review_update(request, pk):
    stop = get_object_or_404(RouteStop, pk=pk)
    action = request.POST.get("action")
    comment = request.POST.get("comment", "")
    if action not in ["approve", "reject"]:
        return HttpResponseBadRequest("Некорректное действие.")
    old_status = stop.proof_review_status
    stop.proof_review_status = (
        RouteStop.ProofReviewStatus.APPROVED if action == "approve" else RouteStop.ProofReviewStatus.REJECTED
    )
    stop.proof_review_comment = comment
    stop.proof_reviewed_at = timezone.now()
    stop.proof_reviewed_by = request.user
    stop.save(update_fields=["proof_review_status", "proof_review_comment", "proof_reviewed_at", "proof_reviewed_by"])
    _log_action(request.user, stop, "proof_review_status", old_status, stop.proof_review_status, comment)
    messages.success(request, "Проверка обновлена.")
    return redirect("/logistics/manager/proofs/")


@role_required("Курьер")
def courier_profile(request):
    courier, _ = _get_or_create_courier_profile(request.user)
    form = CourierProfileForm(request.POST or None, instance=courier)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Профиль курьера обновлён.")
        return redirect("/logistics/courier/profile/")
    return render(
        request,
        "courier/profile.html",
        {
            "form": form,
            "courier": courier,
        },
    )
```

53. reports/__init__.py
```python
```

54. reports/admin.py
```python
from django.contrib import admin

# Register your models here.
```

55. reports/apps.py
```python
from django.apps import AppConfig


class ReportsConfig(AppConfig):
    name = 'reports'
```

56. reports/forms.py
```python
from django import forms
from crm.forms import BootstrapFormMixin
from .models import Report


class ReportForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Report
        fields = ["title", "period_from", "period_to", "status", "file"]
        widgets = {
            "period_from": forms.DateInput(attrs={"type": "date"}),
            "period_to": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
```

57. reports/models.py
```python
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
```

58. reports/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

59. reports/urls.py
```python
from django.urls import path
from .views import reports_list, report_create, report_edit, analytics_view, report_validate

urlpatterns = [
    path("", reports_list, name="reports-list"),
    path("analytics/", analytics_view, name="reports-analytics"),
    path("create/", report_create, name="reports-create"),
    path("<int:pk>/edit/", report_edit, name="reports-edit"),
    path("<int:pk>/validate/", report_validate, name="reports-validate"),
]
```

60. reports/views.py
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from accounts.utils import roles_required
from .models import Report
from .forms import ReportForm
from crm.models import Order, OrderStatus, Client


@roles_required(["Менеджер", "Администратор системы"])
def reports_list(request):
    qs = Report.objects.all().order_by("-created_at")
    return render(request, "reports/list.html", {"reports": qs})


@roles_required(["Менеджер", "Администратор системы"])
def report_create(request):
    initial = {}
    if request.method == "GET":
        if request.GET.get("from"):
            initial["period_from"] = request.GET.get("from")
        if request.GET.get("to"):
            initial["period_to"] = request.GET.get("to")
    form = ReportForm(request.POST or None, request.FILES or None, initial=initial)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user
        obj.save()
        return redirect("/reports/")
    return render(request, "reports/form.html", {"form": form, "title": "Создать отчёт"})


@roles_required(["Менеджер", "Администратор системы"])
def report_edit(request, pk):
    obj = get_object_or_404(Report, pk=pk)
    form = ReportForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/reports/")
    return render(request, "reports/form.html", {"form": form, "title": "Редактировать отчёт"})


@roles_required(["Менеджер", "Администратор системы"])
def report_validate(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        if report.period_from and report.period_to and report.period_from > report.period_to:
            report.validation_status = "error"
            report.validation_message = "Дата начала больше даты окончания."
        elif not report.file:
            report.validation_status = "warn"
            report.validation_message = "Файл отчёта не загружен."
        else:
            report.validation_status = "ok"
            report.validation_message = "Проверка пройдена успешно."
        report.save(update_fields=["validation_status", "validation_message"])
    return redirect("/reports/")


@roles_required(["Менеджер", "Администратор системы"])
def analytics_view(request):
    date_from = request.GET.get("from")
    date_to = request.GET.get("to")
    status = request.GET.get("status")
    client_id = request.GET.get("client")
    qs = Order.objects.all()
    if date_from:
        qs = qs.filter(created_at__date__gte=date_from)
    if date_to:
        qs = qs.filter(created_at__date__lte=date_to)
    if status:
        qs = qs.filter(status=status)
    if client_id:
        qs = qs.filter(client_id=client_id)
    total_orders = qs.count()
    revenue = qs.aggregate(total=Sum("total_amount"))["total"] or 0
    avg_check = round((revenue / total_orders), 2) if total_orders else 0
    status_labels = dict(OrderStatus.choices)
    raw_status = list(qs.values("status").annotate(cnt=Count("id")))
    max_cnt = max([row["cnt"] for row in raw_status], default=0) or 1
    by_status = [
        {
            "status": row["status"],
            "label": status_labels.get(row["status"], row["status"]),
            "cnt": row["cnt"],
            "percent": int((row["cnt"] / max_cnt) * 100),
        }
        for row in raw_status
    ]
    by_day = (
        qs.annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(cnt=Count("id"), revenue=Sum("total_amount"))
        .order_by("day")
    )
    by_day = [
        {
            "day": row["day"].strftime("%Y-%m-%d") if row["day"] else "",
            "cnt": row["cnt"],
            "revenue": float(row["revenue"] or 0),
        }
        for row in by_day
    ]
    avg_check_by_day = [
        {
            "day": row["day"],
            "avg_check": round((row["revenue"] / row["cnt"]), 2) if row["cnt"] else 0,
        }
        for row in by_day
    ]
    by_client = (
        qs.values("client__name")
        .annotate(cnt=Count("id"), revenue=Sum("total_amount"))
        .order_by("-revenue")[:10]
    )
    by_client = [
        {
            "client": row["client__name"] or "—",
            "cnt": row["cnt"],
            "revenue": float(row["revenue"] or 0),
        }
        for row in by_client
    ]
    by_client_type = (
        qs.values("client__client_type")
        .annotate(cnt=Count("id"), revenue=Sum("total_amount"))
        .order_by("-cnt")
    )
    by_client_type = [
        {
            "type": row["client__client_type"] or "—",
            "cnt": row["cnt"],
            "revenue": float(row["revenue"] or 0),
        }
        for row in by_client_type
    ]
    clients = Client.objects.all()
    context = {
        "total_orders": total_orders,
        "revenue": revenue,
        "avg_check": avg_check,
        "by_status": list(by_status),
        "by_day": by_day,
        "avg_check_by_day": avg_check_by_day,
        "by_client": by_client,
        "by_client_type": by_client_type,
        "today": timezone.now().date(),
        "clients": clients,
        "statuses": OrderStatus.choices,
    }
    return render(request, "reports/analytics.html", context)

# Create your views here.
```

61. admin_panel/__init__.py
```python
```

62. admin_panel/admin.py
```python
from django.contrib import admin

# Register your models here.
```

63. admin_panel/apps.py
```python
from django.apps import AppConfig


class AdminPanelConfig(AppConfig):
    name = 'admin_panel'
```

64. admin_panel/entity_config.py
```python
from dataclasses import dataclass
from typing import Callable, Iterable

from crm import models as crm
from admin_panel.forms import UserCreateForm, UserUpdateForm
from reports.models import Report
from admin_panel.models import Backup, BackupSchedule


@dataclass
class InlineConfig:
    label: str
    get_queryset: Callable
    fields: list


@dataclass
class EntityConfig:
    slug: str
    label: str
    model: type
    list_display: list  # list of (header, accessor)
    search_fields: list
    filter_fields: list
    date_fields: list
    inlines: list
    create_form_class: type | None = None
    edit_form_class: type | None = None


def _roles_display(obj):
    return ", ".join(obj.roles.values_list("name", flat=True))


ENTITIES = [
    EntityConfig(
        slug="users",
        label="Пользователи",
        model=crm.User,
        list_display=[
            ("Логин", "username"),
            ("ФИО", "full_name"),
            ("Email", "email"),
            ("Активен", "is_active"),
            ("Роли", _roles_display),
        ],
        search_fields=["username", "full_name", "email", "phone"],
        filter_fields=["is_active"],
        date_fields=["date_joined"],
        inlines=[
            InlineConfig("Роли", lambda obj: obj.roles.all(), ["name"]),
        ],
        create_form_class=UserCreateForm,
        edit_form_class=UserUpdateForm,
    ),
    EntityConfig(
        slug="roles",
        label="Роли",
        model=crm.Role,
        list_display=[("Название", "name")],
        search_fields=["name"],
        filter_fields=[],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="user-roles",
        label="Роли пользователей",
        model=crm.UserRole,
        list_display=[("Пользователь", "user"), ("Роль", "role"), ("Назначено", "assigned_at")],
        search_fields=["user__username", "user__full_name", "role__name"],
        filter_fields=["role"],
        date_fields=["assigned_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="clients",
        label="Клиенты",
        model=crm.Client,
        list_display=[
            ("Название", "name"),
            ("Телефон", "phone"),
            ("Email", "email"),
            ("Статус", "status"),
            ("Этап", "current_stage"),
        ],
        search_fields=["name", "phone", "email", "inn", "kpp"],
        filter_fields=["status", "current_stage", "responsible_manager"],
        date_fields=["created_at"],
        inlines=[
            InlineConfig("Контакты", lambda obj: obj.contacts.all(), ["full_name", "phone", "email", "is_primary"]),
            InlineConfig("История этапов", lambda obj: obj.stage_history.all(), ["stage", "changed_by", "changed_at"]),
            InlineConfig("Взаимодействия", lambda obj: obj.interactions.all(), ["interaction_type", "happened_at", "manager"]),
            InlineConfig("Заказы", lambda obj: obj.orders.all(), ["order_number", "status", "total_amount"]),
        ],
    ),
    EntityConfig(
        slug="client-contacts",
        label="Контакты клиентов",
        model=crm.ClientContact,
        list_display=[("Клиент", "client"), ("ФИО", "full_name"), ("Телефон", "phone"), ("Email", "email")],
        search_fields=["full_name", "phone", "email", "client__name"],
        filter_fields=["client", "is_primary"],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="stages",
        label="Этапы сотрудничества",
        model=crm.CooperationStage,
        list_display=[("Название", "name"), ("Порядок", "order"), ("Активен", "is_active")],
        search_fields=["name"],
        filter_fields=["is_active"],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="stage-history",
        label="Истории этапов клиента",
        model=crm.ClientStageHistory,
        list_display=[("Клиент", "client"), ("Этап", "stage"), ("Изменил", "changed_by"), ("Дата", "changed_at")],
        search_fields=["client__name", "stage__name"],
        filter_fields=["client", "stage", "changed_by"],
        date_fields=["changed_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="interactions",
        label="Взаимодействия",
        model=crm.Interaction,
        list_display=[("Клиент", "client"), ("Тип", "interaction_type"), ("Менеджер", "manager"), ("Дата", "happened_at")],
        search_fields=["client__name", "note"],
        filter_fields=["interaction_type", "manager", "client"],
        date_fields=["happened_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="ingredients",
        label="Ингредиенты",
        model=crm.Ingredient,
        list_display=[("Название", "name"), ("Активен", "is_active")],
        search_fields=["name"],
        filter_fields=["is_active"],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="dishes",
        label="Блюда каталога",
        model=crm.Dish,
        list_display=[("Название", "name"), ("Ед.", "unit"), ("Активно", "is_active")],
        search_fields=["name"],
        filter_fields=["is_active", "created_by"],
        date_fields=[],
        inlines=[
            InlineConfig("Техкарты", lambda obj: obj.tech_cards.all(), ["version_label", "is_active"]),
        ],
    ),
    EntityConfig(
        slug="techcards",
        label="Техкарты блюд",
        model=crm.TechCard,
        list_display=[("Блюдо", "dish"), ("Версия", "version_label"), ("Активна", "is_active")],
        search_fields=["dish__name", "version_label"],
        filter_fields=["dish", "is_active", "approved_by"],
        date_fields=[],
        inlines=[
            InlineConfig("Состав", lambda obj: obj.components.all(), ["ingredient", "quantity"]),
            InlineConfig("Варианты", lambda obj: obj.variants.all(), ["quantity", "note"]),
        ],
    ),
    EntityConfig(
        slug="techcard-components",
        label="Состав техкарт",
        model=crm.TechCardComponent,
        list_display=[("Техкарта", "tech_card"), ("Ингредиент", "ingredient"), ("Количество", "quantity")],
        search_fields=["tech_card__dish__name", "ingredient__name"],
        filter_fields=["tech_card", "ingredient"],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="techcard-variants",
        label="Сорта/варианты техкарт",
        model=crm.TechCardVariant,
        list_display=[("Техкарта", "tech_card"), ("Количество", "quantity"), ("Примечание", "note")],
        search_fields=["tech_card__dish__name"],
        filter_fields=["tech_card"],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="orders",
        label="Заказы",
        model=crm.Order,
        list_display=[
            ("Номер", "order_number"),
            ("Клиент", "client"),
            ("Статус", "status"),
            ("Сумма", "total_amount"),
            ("Дата", "created_at"),
        ],
        search_fields=["order_number", "client__name"],
        filter_fields=["status", "client", "manager", "is_archived"],
        date_fields=["created_at"],
        inlines=[
            InlineConfig("Позиции заказа", lambda obj: obj.items.all(), ["display_name", "quantity", "item_status"]),
            InlineConfig("Доставки", lambda obj: obj.deliveries.all(), ["status", "courier", "planned_at"]),
        ],
    ),
    EntityConfig(
        slug="order-items",
        label="Позиции заказов",
        model=crm.OrderItem,
        list_display=[
            ("Заказ", "order"),
            ("Позиция", "display_name"),
            ("Заказано", "quantity"),
            ("Собрано", "picked_quantity"),
            ("Статус", "item_status"),
        ],
        search_fields=["order__order_number", "dish__name", "ingredient__name"],
        filter_fields=["order", "item_status"],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="couriers",
        label="Курьеры",
        model=crm.Courier,
        list_display=[("Курьер", "user"), ("Статус", "status"), ("Зона", "zone")],
        search_fields=["user__full_name", "user__phone"],
        filter_fields=["status"],
        date_fields=[],
        inlines=[],
    ),
    EntityConfig(
        slug="deliveries",
        label="Доставки",
        model=crm.Delivery,
        list_display=[("Заказ", "order"), ("Курьер", "courier"), ("Статус", "status"), ("План", "planned_at")],
        search_fields=["order__order_number", "address"],
        filter_fields=["status", "courier", "route"],
        date_fields=["planned_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="routes",
        label="Маршруты",
        model=crm.Route,
        list_display=[("Дата", "planned_date"), ("Логист", "logistician"), ("Статус", "status")],
        search_fields=["notes"],
        filter_fields=["status", "logistician"],
        date_fields=["planned_date"],
        inlines=[
            InlineConfig("Остановки", lambda obj: obj.stops.all(), ["delivery", "sequence_index"]),
            InlineConfig("Назначения", lambda obj: obj.assignments.all(), ["courier", "assigned_at"]),
        ],
    ),
    EntityConfig(
        slug="courier-assignments",
        label="Назначения курьеров",
        model=crm.CourierAssignment,
        list_display=[("Курьер", "courier"), ("Маршрут", "route"), ("Назначено", "assigned_at")],
        search_fields=["courier__user__full_name", "route__planned_date"],
        filter_fields=["courier", "route"],
        date_fields=["assigned_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="route-stops",
        label="Остановки маршрута",
        model=crm.RouteStop,
        list_display=[("Маршрут", "route"), ("Доставка", "delivery"), ("Порядок", "sequence_index")],
        search_fields=["route__planned_date"],
        filter_fields=["route"],
        date_fields=["planned_time"],
        inlines=[],
    ),
    EntityConfig(
        slug="picking-sessions",
        label="Сборки заказов",
        model=crm.PickingSession,
        list_display=[("Заказ", "order"), ("Сборщик", "picker"), ("Начата", "started_at"), ("Завершена", "finished_at")],
        search_fields=["order__order_number", "picker__full_name"],
        filter_fields=["picker"],
        date_fields=["started_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="reports",
        label="Отчёты",
        model=Report,
        list_display=[("Название", "title"), ("Период с", "period_from"), ("Период по", "period_to"), ("Статус", "status")],
        search_fields=["title"],
        filter_fields=["status", "validation_status", "created_by"],
        date_fields=["created_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="backups",
        label="Резервные копии",
        model=Backup,
        list_display=[("Файл", "file_path"), ("Статус", "status"), ("Создан", "created_at")],
        search_fields=["file_path"],
        filter_fields=["status", "created_by"],
        date_fields=["created_at"],
        inlines=[],
    ),
    EntityConfig(
        slug="backup-schedule",
        label="Расписание бэкапов",
        model=BackupSchedule,
        list_display=[("Частота", "frequency"), ("Активно", "is_active"), ("Обновлено", "updated_at")],
        search_fields=[],
        filter_fields=["is_active", "frequency"],
        date_fields=["updated_at"],
        inlines=[],
    ),
]
```

65. admin_panel/forms.py
```python
from django import forms
from django.contrib.auth import get_user_model
from crm.forms import BootstrapFormMixin
from crm.models import Role
from .models import BackupSchedule


User = get_user_model()


class UserCreateForm(BootstrapFormMixin, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    roles = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), label="Роли")

    class Meta:
        model = User
        fields = ["username", "email", "full_name", "phone", "is_active"]
        labels = {
            "username": "Логин",
            "email": "Электронная почта",
            "full_name": "ФИО",
            "phone": "Телефон",
            "is_active": "Активен",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        self.fields["password"].widget.attrs.setdefault("class", "form-control")
        self.fields["roles"].widget.attrs.setdefault("class", "form-select")


class UserUpdateForm(BootstrapFormMixin, forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(queryset=Role.objects.all(), label="Роли", required=False)

    class Meta:
        model = User
        fields = ["email", "full_name", "phone", "is_active"]
        labels = {
            "email": "Электронная почта",
            "full_name": "ФИО",
            "phone": "Телефон",
            "is_active": "Активен",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
        self.fields["roles"].widget.attrs.setdefault("class", "form-select")


class UserPasswordForm(BootstrapFormMixin, forms.Form):
    password = forms.CharField(label="Новый пароль", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password") != cleaned.get("password_confirm"):
            self.add_error("password_confirm", "Пароли не совпадают.")
        return cleaned


class RoleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Role
        fields = ["name"]
        labels = {"name": "Название роли"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()


class BackupScheduleForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = BackupSchedule
        fields = ["frequency", "is_active"]
        labels = {"frequency": "Частота", "is_active": "Активные задания"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()
```

66. admin_panel/models.py
```python
from django.db import models
from django.conf import settings


class Backup(models.Model):
    STATUS_CHOICES = [
        ("created", "Создан"),
        ("restored", "Восстановлен"),
        ("failed", "Ошибка"),
    ]
    file_path = models.CharField("Файл", max_length=255)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="created")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField("Создан", auto_now_add=True)

    def __str__(self):
        return self.file_path


class BackupSchedule(models.Model):
    FREQUENCY_CHOICES = [
        ("daily", "Ежедневно"),
        ("weekly", "Еженедельно"),
        ("monthly", "Ежемесячно"),
    ]
    frequency = models.CharField("Частота", max_length=20, choices=FREQUENCY_CHOICES, default="weekly")
    is_active = models.BooleanField("Активно", default=True)
    updated_at = models.DateTimeField("Обновлено", auto_now=True)

    def __str__(self):
        return f"{self.get_frequency_display()} ({'активно' if self.is_active else 'выключено'})"

# Create your models here.
```

67. admin_panel/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

68. admin_panel/urls.py
```python
from django.urls import path
from .views import (
    admin_index,
    users_list,
    user_create,
    user_edit,
    user_delete,
    user_toggle_active,
    user_password,
    roles_list,
    role_create,
    backup_list,
    backup_create,
    backup_restore,
    backup_schedule,
    access_matrix,
    data_check,
    entity_list,
    entity_detail,
    entity_create,
    entity_edit,
    entity_delete,
)

urlpatterns = [
    path("", admin_index, name="admin-index"),
    path("users/", users_list, name="admin-users"),
    path("users/create/", user_create, name="admin-user-create"),
    path("users/<int:pk>/edit/", user_edit, name="admin-user-edit"),
    path("users/<int:pk>/delete/", user_delete, name="admin-user-delete"),
    path("users/<int:pk>/toggle/", user_toggle_active, name="admin-user-toggle"),
    path("users/<int:pk>/password/", user_password, name="admin-user-password"),
    path("roles/", roles_list, name="admin-roles"),
    path("roles/create/", role_create, name="admin-role-create"),
    path("backups/", backup_list, name="admin-backups"),
    path("backups/create/", backup_create, name="admin-backup-create"),
    path("backups/<int:pk>/restore/", backup_restore, name="admin-backup-restore"),
    path("backups/schedule/", backup_schedule, name="admin-backup-schedule"),
    path("access/", access_matrix, name="admin-access"),
    path("data-check/", data_check, name="admin-data-check"),
    path("entities/<slug:slug>/", entity_list, name="admin-entity-list"),
    path("entities/<slug:slug>/create/", entity_create, name="admin-entity-create"),
    path("entities/<slug:slug>/<int:pk>/", entity_detail, name="admin-entity-detail"),
    path("entities/<slug:slug>/<int:pk>/edit/", entity_edit, name="admin-entity-edit"),
    path("entities/<slug:slug>/<int:pk>/delete/", entity_delete, name="admin-entity-delete"),
]
```

69. admin_panel/views.py
```python
import os
import shutil
from datetime import datetime
from django.conf import settings
from django.core.paginator import Paginator
from django.db import IntegrityError, connection, transaction
from django.db import models as dj_models
from django.db.models import ProtectedError
from django.db.models import Q
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from accounts.utils import role_required
from crm.models import Role, Client, Order, Delivery
from .models import Backup, BackupSchedule
from .forms import UserCreateForm, UserUpdateForm, UserPasswordForm, RoleForm, BackupScheduleForm
from django.contrib.auth import get_user_model
from django.contrib import messages
from .entity_config import ENTITIES, EntityConfig
from crm.forms import BootstrapFormMixin

User = get_user_model()


def _cleanup_legacy_user_refs(user_id: int) -> None:
    """
    Remove references from legacy tables that might still have FK to crm_user
    but are not represented by installed models (e.g. django_admin_log).
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = {row[0] for row in cursor.fetchall()}
        if "django_admin_log" in tables:
            cursor.execute("DELETE FROM django_admin_log WHERE user_id = %s", [user_id])


@role_required("Администратор системы")
def admin_index(request):
    stats = {
        "users": User.objects.count(),
        "roles": Role.objects.count(),
        "backups": Backup.objects.count(),
    }
    entities = []
    for entity in ENTITIES:
        try:
            count = entity.model.objects.count()
        except Exception:
            count = 0
        entities.append({"slug": entity.slug, "label": entity.label, "count": count})
    return render(request, "admin_panel/index.html", {"stats": stats, "entities": entities})


@role_required("Администратор системы")
def users_list(request):
    qs = User.objects.all()
    return render(request, "admin_panel/users_list.html", {"users": qs})


@role_required("Администратор системы")
def user_create(request):
    form = UserCreateForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        roles = form.cleaned_data.pop("roles")
        password = form.cleaned_data.pop("password")
        user = User.objects.create(**form.cleaned_data)
        user.set_password(password)
        user.save()
        user.roles.set(roles)
        messages.success(request, "Пользователь создан.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_form.html", {"form": form, "title": "Создать пользователя"})


@role_required("Администратор системы")
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserUpdateForm(request.POST or None, instance=user, initial={"roles": user.roles.all()})
    if request.method == "POST" and form.is_valid():
        roles = form.cleaned_data.pop("roles")
        form.save()
        user.roles.set(roles)
        messages.success(request, "Пользователь обновлён.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_form.html", {"form": form, "title": "Редактировать пользователя"})


@role_required("Администратор системы")
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        if request.user.pk == user.pk:
            messages.error(request, "Нельзя удалить текущего авторизованного пользователя.")
            return redirect("/admin-panel/users/")
        try:
            with transaction.atomic():
                _cleanup_legacy_user_refs(user.pk)
                user.delete()
            messages.success(request, "Пользователь удалён.")
        except ProtectedError:
            messages.error(request, "Невозможно удалить пользователя: есть связанные защищённые данные.")
        except IntegrityError:
            messages.error(request, "Невозможно удалить пользователя: найдены связанные записи в базе данных.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_delete.html", {"object": user})


@role_required("Администратор системы")
def user_toggle_active(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.is_active = not user.is_active
        user.save(update_fields=["is_active"])
        messages.success(request, "Статус пользователя обновлён.")
    return redirect("/admin-panel/users/")


@role_required("Администратор системы")
def user_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserPasswordForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user.set_password(form.cleaned_data["password"])
        user.save()
        messages.success(request, "Пароль обновлён.")
        return redirect("/admin-panel/users/")
    return render(request, "admin_panel/user_password.html", {"form": form, "user_obj": user})


@role_required("Администратор системы")
def roles_list(request):
    qs = Role.objects.all()
    return render(request, "admin_panel/roles_list.html", {"roles": qs})


@role_required("Администратор системы")
def role_create(request):
    form = RoleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Роль создана.")
        return redirect("/admin-panel/roles/")
    return render(request, "admin_panel/role_form.html", {"form": form, "title": "Создать роль"})


@role_required("Администратор системы")
def backup_list(request):
    qs = Backup.objects.all().order_by("-created_at")
    schedule = BackupSchedule.objects.first()
    backups = []
    for b in qs:
        try:
            size = os.path.getsize(b.file_path) if os.path.exists(b.file_path) else 0
        except OSError:
            size = 0
        backups.append({"obj": b, "size": size})
    return render(request, "admin_panel/backups.html", {"backups": backups, "schedule": schedule})


@role_required("Администратор системы")
def backup_create(request):
    db_path = settings.DATABASES["default"]["NAME"]
    if not db_path or not os.path.exists(db_path):
        messages.error(request, "Файл базы данных не найден.")
        return redirect("/admin-panel/backups/")
    os.makedirs(settings.MEDIA_ROOT / "backups", exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = settings.MEDIA_ROOT / "backups" / f"backup_{ts}.sqlite3"
    shutil.copy2(db_path, dest)
    Backup.objects.create(file_path=str(dest), created_by=request.user, status="created")
    messages.success(request, "Резервная копия создана.")
    return redirect("/admin-panel/backups/")


@role_required("Администратор системы")
def backup_restore(request, pk):
    backup = get_object_or_404(Backup, pk=pk)
    db_path = settings.DATABASES["default"]["NAME"]
    if request.method == "POST":
        if os.path.exists(backup.file_path) and db_path:
            shutil.copy2(backup.file_path, db_path)
            backup.status = "restored"
            backup.save(update_fields=["status"])
            messages.success(request, "Резервная копия восстановлена.")
        else:
            messages.error(request, "Файл резервной копии не найден.")
    return redirect("/admin-panel/backups/")


@role_required("Администратор системы")
def backup_schedule(request):
    schedule = BackupSchedule.objects.first()
    form = BackupScheduleForm(request.POST or None, instance=schedule)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Настройки резервного копирования сохранены.")
        return redirect("/admin-panel/backups/")
    return render(request, "admin_panel/backup_schedule.html", {"form": form, "title": "Расписание бэкапов"})


@role_required("Администратор системы")
def access_matrix(request):
    roles = Role.objects.all()
    rows = [
        {"name": "Клиенты", "url": "/clients/", "allowed": ["Менеджер", "Администратор системы"]},
        {"name": "Заказы", "url": "/orders/", "allowed": ["Менеджер", "Сборщик заказов", "Администратор системы"]},
        {"name": "Доставки", "url": "/logistics/", "allowed": ["Логист", "Администратор системы"]},
        {"name": "Маршруты", "url": "/logistics/routes/", "allowed": ["Логист", "Администратор системы"]},
        {"name": "Отчёты", "url": "/reports/", "allowed": ["Менеджер", "Администратор системы"]},
        {"name": "Аналитика", "url": "/reports/analytics/", "allowed": ["Менеджер", "Администратор системы"]},
        {"name": "Админ‑панель", "url": "/admin-panel/", "allowed": ["Администратор системы"]},
    ]
    return render(request, "admin_panel/access.html", {"rows": rows, "roles": roles})


@role_required("Администратор системы")
def data_check(request):
    report = {"errors": [], "warnings": []}
    if request.method == "POST":
        if Order.objects.filter(client__isnull=True).exists():
            report["errors"].append("Есть заказы без клиента.")
        if Delivery.objects.filter(order__isnull=True).exists():
            report["errors"].append("Есть доставки без заказа.")
        if Delivery.objects.filter(courier__isnull=True, status__in=["Запланировано", "В пути", "Доставлено"]).exists():
            report["errors"].append("Есть доставки со статусом в работе без курьера.")
        if Client.objects.filter(phone="").exists():
            report["warnings"].append("Есть клиенты без телефона.")
        if Client.objects.filter(email="").exists():
            report["warnings"].append("Есть клиенты без email.")
        if not report["errors"] and not report["warnings"]:
            report["warnings"].append("Критичных проблем не найдено.")
    return render(request, "admin_panel/data_check.html", {"report": report})

def _get_entity(slug: str) -> EntityConfig:
    for entity in ENTITIES:
        if entity.slug == slug:
            return entity
    return None


def _resolve_accessor(obj, accessor):
    if callable(accessor):
        value = accessor(obj)
        if isinstance(value, bool):
            return "Да" if value else "Нет"
        return value
    if isinstance(accessor, str):
        display_method = f"get_{accessor}_display"
        if hasattr(obj, display_method):
            value = getattr(obj, display_method)()
            return value
        value = getattr(obj, accessor, "")
        if callable(value):
            value = value()
        if isinstance(value, bool):
            return "Да" if value else "Нет"
        return value
    return ""


def _field_label(model, accessor):
    if isinstance(accessor, str):
        try:
            field = model._meta.get_field(accessor)
            return field.verbose_name.capitalize()
        except Exception:
            return accessor.replace("_", " ").capitalize()
    if callable(accessor):
        return getattr(accessor, "__name__", "Поле").replace("_", " ").capitalize()
    return "Поле"


def _build_filter_options(model, field_name):
    field = model._meta.get_field(field_name)
    if field.choices:
        return [{"value": choice[0], "label": choice[1]} for choice in field.choices]
    if isinstance(field, dj_models.BooleanField):
        return [{"value": "1", "label": "Да"}, {"value": "0", "label": "Нет"}]
    if field.is_relation:
        qs = field.remote_field.model.objects.all()
        return [{"value": str(obj.pk), "label": str(obj)} for obj in qs]
    return []


def _entity_form_class(model, exclude_fields=None):
    exclude_fields = exclude_fields or []
    for field in model._meta.fields:
        if not field.editable or field.auto_created:
            exclude_fields.append(field.name)
    for field in model._meta.many_to_many:
        if not field.editable:
            exclude_fields.append(field.name)
        if field.remote_field.through and not field.remote_field.through._meta.auto_created:
            exclude_fields.append(field.name)

    meta_class = type(
        "Meta",
        (),
        {
            "model": model,
            "fields": "__all__",
            "exclude": list(set(exclude_fields)),
        },
    )

    class EntityForm(BootstrapFormMixin, forms.ModelForm):
        Meta = meta_class

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._init_bootstrap()
            for field in self.fields.values():
                if isinstance(field.widget, forms.Textarea):
                    field.widget.attrs.setdefault("rows", 3)
                    field.widget.attrs.setdefault("data-size", "full")
                if isinstance(field, forms.DateField) and not isinstance(field, forms.DateTimeField):
                    field.widget.attrs.setdefault("type", "date")
                if isinstance(field, forms.DateTimeField):
                    field.widget.attrs.setdefault("type", "datetime-local")

    return EntityForm


@role_required("Администратор системы")
def entity_list(request, slug):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    model = entity.model
    qs = model.objects.all()

    query = request.GET.get("q", "").strip()
    if query and entity.search_fields:
        q_obj = Q()
        for field in entity.search_fields:
            q_obj |= Q(**{f"{field}__icontains": query})
        qs = qs.filter(q_obj)

    filters = []
    for field_name in entity.filter_fields:
        value = request.GET.get(field_name, "")
        field = model._meta.get_field(field_name)
        if value != "":
            if isinstance(field, dj_models.BooleanField):
                qs = qs.filter(**{field_name: value in ["1", "true", "True"]})
            elif field.is_relation:
                qs = qs.filter(**{field_name: value})
            else:
                qs = qs.filter(**{field_name: value})
        filters.append(
            {
                "name": field_name,
                "label": field.verbose_name.capitalize(),
                "value": value,
                "options": _build_filter_options(model, field_name),
            }
        )

    date_filters = []
    for field_name in entity.date_fields:
        start = request.GET.get(f"{field_name}_from", "")
        end = request.GET.get(f"{field_name}_to", "")
        field = model._meta.get_field(field_name)
        if start:
            key = f"{field_name}__date__gte" if isinstance(field, dj_models.DateTimeField) else f"{field_name}__gte"
            qs = qs.filter(**{key: start})
        if end:
            key = f"{field_name}__date__lte" if isinstance(field, dj_models.DateTimeField) else f"{field_name}__lte"
            qs = qs.filter(**{key: end})
        date_filters.append({"name": field_name, "label": field.verbose_name.capitalize(), "from": start, "to": end})

    allowed_sort = {f.name for f in model._meta.fields}
    sort_field = request.GET.get("sort", "")
    sort_dir = request.GET.get("dir", "desc")
    if sort_field in allowed_sort:
        ordering = f"-{sort_field}" if sort_dir == "desc" else sort_field
        qs = qs.order_by(ordering)

    paginator = Paginator(qs, 20)
    page_obj = paginator.get_page(request.GET.get("page"))
    query_params = request.GET.copy()
    if "page" in query_params:
        query_params.pop("page")
    query_string = query_params.urlencode()
    rows = []
    for obj in page_obj:
        cells = []
        for _, accessor in entity.list_display:
            cells.append(_resolve_accessor(obj, accessor))
        rows.append({"obj": obj, "cells": cells})

    sort_options = [
        {"value": f.name, "label": f.verbose_name.capitalize()}
        for f in model._meta.fields
        if f.name in allowed_sort
    ]

    return render(
        request,
        "admin_panel/entities/list.html",
        {
            "entity": entity,
            "headers": [header for header, _ in entity.list_display],
            "rows": rows,
            "filters": filters,
            "date_filters": date_filters,
            "query": query,
            "page_obj": page_obj,
            "paginator": paginator,
            "sort_options": sort_options,
            "sort_field": sort_field,
            "sort_dir": sort_dir,
            "query_string": query_string,
        },
    )


@role_required("Администратор системы")
def entity_detail(request, slug, pk):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    obj = get_object_or_404(entity.model, pk=pk)
    fields = []
    for field in obj._meta.fields:
        if field.choices:
            value = getattr(obj, f"get_{field.name}_display")()
        else:
            value = getattr(obj, field.name)
        if field.is_relation:
            value = str(value) if value else "—"
        elif isinstance(field, dj_models.BooleanField):
            value = "Да" if value else "Нет"
        fields.append({"label": field.verbose_name.capitalize(), "value": value})

    inline_sections = []
    for inline in entity.inlines:
        qs = inline.get_queryset(obj)
        rows = []
        for row in qs:
            values = [_resolve_accessor(row, f) for f in inline.fields]
            rows.append(values)
        model = getattr(qs, "model", None)
        headers = [_field_label(model, f) for f in inline.fields] if model else [str(f) for f in inline.fields]
        count = qs.count() if hasattr(qs, "count") else len(rows)
        inline_sections.append({"label": inline.label, "headers": headers, "rows": rows, "count": count})

    return render(
        request,
        "admin_panel/entities/detail.html",
        {"entity": entity, "obj": obj, "fields": fields, "inline_sections": inline_sections},
    )


@role_required("Администратор системы")
def entity_create(request, slug):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    form_class = entity.create_form_class or _entity_form_class(entity.model)
    form = form_class(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            obj = form.save(commit=False)
            if hasattr(obj, "created_at") and not getattr(obj, "created_at"):
                obj.created_at = timezone.now()
            if isinstance(form, UserCreateForm):
                roles = form.cleaned_data.pop("roles", [])
                password = form.cleaned_data.pop("password")
                user = User.objects.create(**form.cleaned_data)
                user.set_password(password)
                user.save()
                user.roles.set(roles)
            else:
                obj.save()
                if hasattr(form, "save_m2m"):
                    form.save_m2m()
            messages.success(request, "Сохранено.")
            return redirect(f"/admin-panel/entities/{entity.slug}/")
        messages.error(request, "Ошибка валидации.")
    return render(request, "admin_panel/entities/form.html", {"entity": entity, "form": form, "is_edit": False})


@role_required("Администратор системы")
def entity_edit(request, slug, pk):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    obj = get_object_or_404(entity.model, pk=pk)
    form_class = entity.edit_form_class or _entity_form_class(entity.model)
    if form_class is UserUpdateForm:
        form = form_class(request.POST or None, instance=obj, initial={"roles": obj.roles.all()})
    else:
        form = form_class(request.POST or None, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            if isinstance(form, UserUpdateForm):
                roles = form.cleaned_data.pop("roles", [])
                form.save()
                obj.roles.set(roles)
            else:
                form.save()
            messages.success(request, "Сохранено.")
            return redirect(f"/admin-panel/entities/{entity.slug}/{obj.pk}/")
        messages.error(request, "Ошибка валидации.")
    return render(request, "admin_panel/entities/form.html", {"entity": entity, "form": form, "is_edit": True})


@role_required("Администратор системы")
def entity_delete(request, slug, pk):
    entity = _get_entity(slug)
    if not entity:
        return redirect("/admin-panel/")
    obj = get_object_or_404(entity.model, pk=pk)
    blockers = []
    if isinstance(obj, Client):
        count = obj.orders.count()
        if count:
            blockers.append(f"Есть связанные заказы: {count}. Удаление запрещено.")
    if isinstance(obj, Order):
        items = obj.items.count()
        deliveries = obj.deliveries.count()
        if items:
            blockers.append(f"Есть позиции заказа: {items}.")
        if deliveries:
            blockers.append(f"Есть доставки: {deliveries}.")
        if items or deliveries:
            blockers.append("Рекомендуется архивировать заказ вместо удаления.")

    if request.method == "POST":
        if blockers:
            messages.error(request, "Удаление запрещено из‑за связанных данных.")
            return redirect(f"/admin-panel/entities/{entity.slug}/{obj.pk}/")
        try:
            obj.delete()
            messages.success(request, "Удалено.")
        except Exception:
            messages.error(request, "Ошибка удаления.")
        return redirect(f"/admin-panel/entities/{entity.slug}/")

    return render(
        request,
        "admin_panel/entities/delete.html",
        {"entity": entity, "obj": obj, "blockers": blockers},
    )
```

70. dashboard/__init__.py
```python
```

71. dashboard/admin.py
```python
from django.contrib import admin

# Register your models here.
```

72. dashboard/apps.py
```python
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'
```

73. dashboard/models.py
```python
from django.db import models

# Create your models here.
```

74. dashboard/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

75. dashboard/urls.py
```python
from django.urls import path
from .views import manager_dashboard, logistic_dashboard, picker_dashboard, admin_dashboard

urlpatterns = [
    path("manager/", manager_dashboard, name="manager"),
    path("logistic/", logistic_dashboard, name="logistic"),
    path("picker/", picker_dashboard, name="picker"),
    path("admin/", admin_dashboard, name="admin"),
]
```

76. dashboard/views.py
```python
from urllib.parse import quote

from django.conf import settings
from django.shortcuts import render, redirect
from accounts.utils import role_required
from crm.models import Client, Order, Delivery, Route, RouteStatus, LogisticianProfile, Courier, CourierStatus
from reports.models import Report


@role_required("Менеджер")
def manager_dashboard(request):
    stats = {
        "clients": Client.objects.count(),
        "orders": Order.objects.count(),
        "active_orders": Order.objects.filter(
            status__in=["На проверке", "Подтвержден производством", "В производстве"]
        ).count(),
    }
    recent_clients = Client.objects.order_by("-id")[:5]
    recent_orders = Order.objects.select_related("client").order_by("-created_at")[:5]
    return render(
        request,
        "dashboard/manager.html",
        {"stats": stats, "recent_clients": recent_clients, "recent_orders": recent_orders},
    )


@role_required("Логист")
def logistic_dashboard(request):
    stats = {
        "deliveries": Delivery.objects.count(),
        "pending": Delivery.objects.filter(is_sent=False).count(),
        "couriers_total": Courier.objects.count(),
        "couriers_free": Courier.objects.filter(status=CourierStatus.FREE).count(),
        "active_cargo": Delivery.objects.exclude(
            status__in=[Delivery.DeliveryStatus.DELIVERED, Delivery.DeliveryStatus.CANCELLED]
        ).count(),
    }
    recent_deliveries = Delivery.objects.select_related("order").order_by("-id")[:5]
    active_routes = (
        Route.objects.filter(status__in=[RouteStatus.PLANNED, RouteStatus.PUBLISHED, RouteStatus.IN_PROGRESS])
        .prefetch_related("stops__delivery__order")
        .select_related("logistician")
        .order_by("planned_date")
    )
    routes_payload = []
    for route in active_routes:
        stops = sorted(route.stops.all(), key=lambda s: s.sequence_index)
        stop_points = []
        for s in stops:
            address = s.delivery.address or s.delivery.order.address
            stop_points.append(
                {
                    "address": address,
                    "lat": float(s.latitude) if s.latitude is not None else None,
                    "lng": float(s.longitude) if s.longitude is not None else None,
                }
            )
        routes_payload.append(
            {
                "id": route.id,
                "title": f"Маршрут {route.planned_date}",
                "status": route.get_status_display(),
                "stops": stop_points,
            }
        )
    profile, _ = LogisticianProfile.objects.get_or_create(user=request.user)
    return render(
        request,
        "dashboard/logistic.html",
        {
            "stats": stats,
            "recent_deliveries": recent_deliveries,
            "routes_payload": routes_payload,
            "map_prefs": profile,
        },
    )


@role_required("Сборщик заказов")
def picker_dashboard(request):
    stats = {
        "orders": Order.objects.count(),
        "in_progress": Order.objects.filter(status="В производстве").count(),
    }
    recent_orders = Order.objects.select_related("client").order_by("-created_at")[:5]
    return render(request, "dashboard/picker.html", {"stats": stats, "recent_orders": recent_orders})


@role_required("Администратор системы")
def admin_dashboard(request):
    stats = {
        "clients": Client.objects.count(),
        "orders": Order.objects.count(),
        "reports": Report.objects.count(),
    }
    return render(request, "dashboard/admin.html", {"stats": stats})

# Create your views here.
```

77. portal/__init__.py
```python
# Portal app for custom dashboards and CRUD (no Django admin)
```

78. portal/forms.py
```python
from django import forms
from crm.models import Client, Order, Delivery, Courier


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "client_type",
            "inn",
            "kpp",
            "default_delivery_address",
            "email",
            "phone",
            "status",
        ]
        labels = {
            "name": "Название / ФИО",
            "client_type": "Тип клиента",
            "inn": "ИНН",
            "kpp": "КПП",
            "default_delivery_address": "Адрес доставки",
            "email": "Электронная почта",
            "phone": "Телефон",
            "status": "Статус",
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "order_number",
            "client",
            "status",
            "address",
            "comments",
            "total_amount",
        ]
        labels = {
            "order_number": "Номер заказа",
            "client": "Клиент",
            "status": "Статус",
            "address": "Адрес доставки",
            "comments": "Комментарии",
            "total_amount": "Сумма",
        }


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["status", "comments"]
        labels = {"status": "Статус", "comments": "Комментарий"}


class DeliveryPlanForm(forms.ModelForm):
    courier = forms.ModelChoiceField(queryset=Courier.objects.all(), required=False, label="Курьер")

    class Meta:
        model = Delivery
        fields = ["courier", "departure_time", "delivered_at", "address", "note", "is_sent"]
        labels = {
            "departure_time": "Время выезда",
            "delivered_at": "Доставлено",
            "address": "Адрес",
            "note": "Примечание",
            "is_sent": "Отправлен",
        }
```

79. portal/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="portal-login"),
    path("logout/", views.logout_view, name="portal-logout"),
    path("manager/", views.manager_dashboard, name="portal-manager"),
    path("manager/clients/", views.clients_list, name="portal-clients"),
    path("manager/clients/create/", views.client_create, name="portal-client-create"),
    path("manager/clients/<int:pk>/edit/", views.client_edit, name="portal-client-edit"),
    path("manager/orders/", views.order_list, name="portal-orders"),
    path("manager/orders/create/", views.order_create, name="portal-order-create"),
    path("manager/orders/<int:pk>/edit/", views.order_edit, name="portal-order-edit"),
    path("logistic/", views.logistic_dashboard, name="portal-logistic"),
    path("logistic/delivery/<int:pk>/", views.delivery_plan, name="portal-delivery-plan"),
    path("picker/", views.picker_dashboard, name="portal-picker"),
    path("picker/orders/<int:pk>/status/", views.picker_update_status, name="portal-picker-status"),
    path("admin-panel/", views.sysadmin_dashboard, name="portal-sysadmin"),
]
```

80. portal/utils.py
```python
from django.shortcuts import redirect
from functools import wraps


def role_required(role_name: str):
    """
    Decorator to ensure user has role_name (case-insensitive).
    Expects user model with many-to-many to Role via roles.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect("/login/")
            if not user.roles.filter(name__iexact=role_name).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator


def roles_required(role_names):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                return redirect("/login/")
            if not user.roles.filter(name__in=role_names).exists():
                return redirect("/login/")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
```

81. portal/views.py
```python
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from crm.models import Client, Order, Delivery
from .forms import ClientForm, OrderForm, OrderStatusForm, DeliveryPlanForm
from .utils import role_required, roles_required


@csrf_protect
def login_view(request):
    if request.user.is_authenticated:
        # если уже менеджер, ведём в кабинет
        if request.user.roles.filter(name__iexact="Менеджер").exists():
            return redirect("/manager/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Неверные логин или пароль.")
        else:
            login(request, user)
            # маршрутизация по роли
            if user.roles.filter(name__iexact="Менеджер").exists():
                return redirect("/manager/")
            if user.roles.filter(name__iexact="Логист").exists():
                return redirect("/logistic/")
            if user.roles.filter(name__iexact="Сборщик заказов").exists():
                return redirect("/picker/")
            if user.roles.filter(name__iexact="Администратор системы").exists():
                return redirect("/admin-panel/")
            messages.error(request, "Нет прав для доступа.")
    return render(request, "portal/login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


@role_required("Менеджер")
def manager_dashboard(request):
    stats = {
        "clients": Client.objects.count(),
        "orders": Order.objects.count(),
        "active_orders": Order.objects.filter(status__in=["confirmed", "in_progress"]).count(),
    }
    return render(request, "portal/manager_dashboard.html", {"stats": stats})


@role_required("Менеджер")
def clients_list(request):
    qs = Client.objects.all()
    q = request.GET.get("q")
    status = request.GET.get("status")
    if q:
        qs = qs.filter(name__icontains=q)
    if status:
        qs = qs.filter(status=status)
    return render(request, "portal/clients_list.html", {"clients": qs})


@role_required("Менеджер")
def client_create(request):
    form = ClientForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/manager/clients/")
    return render(request, "portal/client_form.html", {"form": form, "title": "Новый клиент"})


@role_required("Менеджер")
def client_edit(request, pk):
    obj = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/manager/clients/")
    return render(request, "portal/client_form.html", {"form": form, "title": "Редактирование клиента"})


@role_required("Менеджер")
def order_list(request):
    qs = Order.objects.select_related("client")
    q = request.GET.get("q")
    status = request.GET.get("status")
    if q:
        qs = qs.filter(order_number__icontains=q)
    if status:
        qs = qs.filter(status=status)
    return render(request, "portal/orders_list.html", {"orders": qs})


@role_required("Менеджер")
def order_create(request):
    form = OrderForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        obj.manager = request.user
        obj.save()
        return redirect("/manager/orders/")
    return render(request, "portal/order_form.html", {"form": form, "title": "Новый заказ"})


@role_required("Менеджер")
def order_edit(request, pk):
    obj = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=obj)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/manager/orders/")
    return render(request, "portal/order_form.html", {"form": form, "title": "Редактирование заказа"})


# --------- Кабинет логиста ---------
@roles_required(["Логист"])
def logistic_dashboard(request):
    deliveries = Delivery.objects.select_related("order", "courier").all()
    return render(request, "portal/logistic_dashboard.html", {"deliveries": deliveries})


@roles_required(["Логист"])
def delivery_plan(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    form = DeliveryPlanForm(request.POST or None, instance=delivery)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/logistic/")
    return render(request, "portal/delivery_plan.html", {"form": form, "title": "Планирование доставки", "delivery": delivery})


# --------- Кабинет сборщика ---------
@roles_required(["Сборщик заказов"])
def picker_dashboard(request):
    orders = Order.objects.all()
    form = OrderStatusForm()
    return render(request, "portal/picker_dashboard.html", {"orders": orders, "form": form})


@roles_required(["Сборщик заказов"])
def picker_update_status(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderStatusForm(request.POST or None, instance=order)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/picker/")
    return render(request, "portal/order_form.html", {"form": form, "title": "Статус заказа"})


# --------- Кабинет администратора системы ---------
@roles_required(["Администратор системы"])
def sysadmin_dashboard(request):
    return render(request, "portal/sysadmin_dashboard.html")
```

82. templates/accounts/login.html
```html
{% extends "accounts/login_base.html" %}
{% load static %}
{% block content %}
  <h1 class="auth-title">Вход в систему</h1>
  <p class="auth-subtitle">Используйте корпоративные данные для входа</p>
  {% if messages %}
    {% for m in messages %}
      <div class="alert alert-danger py-2">{{ m }}</div>
    {% endfor %}
  {% endif %}
  <form method="post" novalidate>
    {% csrf_token %}
    <div class="mb-3">
      <label class="form-label">Электронная почта</label>
      <input type="text" name="username" class="form-control" placeholder="name@company.ru" required>
    </div>
    <div class="mb-3">
      <label class="form-label">Пароль</label>
      <input type="password" name="password" class="form-control" placeholder="••••••••" required>
    </div>
    <button class="btn btn-primary w-100">Войти</button>
  </form>
  <div class="text-center mt-3">
    <a href="/password-reset/" class="link-muted">Забыли пароль?</a>
  </div>
{% endblock %}
```

83. templates/accounts/login_base.html
```html
{% load static %}
<!doctype html>
<html lang="ru" data-theme="light">
<head>
  <meta charset="utf-8">
  <title>Art Culinary CRM</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/app.css' %}">
  <script>
    (function() {
      const key = "crm_theme";
      const saved = localStorage.getItem(key) || "light";
      document.documentElement.setAttribute("data-theme", saved);
    })();
  </script>
</head>
<body class="auth-body">
  <div class="auth-topbar">
    <div class="auth-logo">Art Culinary CRM</div>
    <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Сменить тему">
      <span id="theme-icon">☾</span>
    </button>
  </div>

  <div class="auth-shell">
    <div class="auth-card">
      {% block content %}{% endblock %}
    </div>
  </div>

  <script>
    const key = "crm_theme";
    const html = document.documentElement;
    const btn = document.getElementById("theme-toggle");
    const icon = document.getElementById("theme-icon");
    const applyTheme = (t) => { html.setAttribute("data-theme", t); localStorage.setItem(key, t); };
    const saved = localStorage.getItem(key) || "light";
    applyTheme(saved);
    const updateIcon = () => { icon.textContent = html.getAttribute("data-theme") === "dark" ? "☀︎" : "☾"; };
    updateIcon();
    btn.addEventListener("click", () => {
      const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
      updateIcon();
    });
  </script>
</body>
</html>
```

84. templates/accounts/password_reset_complete.html
```html
{% extends "accounts/login_base.html" %}
{% block content %}
  <h1 class="auth-title">Пароль обновлён</h1>
  <p class="auth-subtitle">Теперь вы можете войти с новым паролем.</p>
  <a href="/login/" class="btn btn-primary w-100">Перейти ко входу</a>
{% endblock %}
```

85. templates/accounts/password_reset_confirm.html
```html
{% extends "accounts/login_base.html" %}
{% block content %}
  <h1 class="auth-title">Новый пароль</h1>
  <p class="auth-subtitle">Придумайте новый пароль для своего аккаунта</p>
  <form method="post" novalidate>
    {% csrf_token %}
    {{ form.non_field_errors }}
    <div class="mb-3">
      <label class="form-label">Новый пароль</label>
      {{ form.new_password1 }}
      {{ form.new_password1.errors }}
    </div>
    <div class="mb-3">
      <label class="form-label">Повторите пароль</label>
      {{ form.new_password2 }}
      {{ form.new_password2.errors }}
    </div>
    <button class="btn btn-primary w-100">Сохранить пароль</button>
  </form>
{% endblock %}
```

86. templates/accounts/password_reset_done.html
```html
{% extends "accounts/login_base.html" %}
{% block content %}
  <h1 class="auth-title">Письмо отправлено</h1>
  <p class="auth-subtitle">Если аккаунт существует, вы получите ссылку для сброса пароля.</p>
  <div class="text-center mt-3">
    <a href="/login/" class="btn btn-outline-secondary w-100">Вернуться ко входу</a>
  </div>
{% endblock %}
```

87. templates/accounts/password_reset_email.html
```html
{% load i18n %}{% autoescape off %}
Вы запросили сброс пароля для аккаунта {{ user.email }}.

Для установки нового пароля перейдите по ссылке:
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

Если вы не отправляли запрос, просто проигнорируйте это письмо.
{% endautoescape %}
```

88. templates/accounts/password_reset_form.html
```html
{% extends "accounts/login_base.html" %}
{% block content %}
  <h1 class="auth-title">Восстановление пароля</h1>
  <p class="auth-subtitle">Укажите почту, мы отправим ссылку для сброса</p>
  <form method="post" novalidate>
    {% csrf_token %}
    {{ form.email.errors }}
    <div class="mb-3">
      <label class="form-label">Электронная почта</label>
      {{ form.email }}
    </div>
    <button class="btn btn-primary w-100">Отправить письмо</button>
  </form>
  <div class="text-center mt-3">
    <a href="/login/" class="link-muted">Назад к входу</a>
  </div>
{% endblock %}
```

89. templates/accounts/password_reset_subject.txt
```text
Сброс пароля для Art Culinary CRM
```

90. templates/admin/base_site.html
```html
{% extends "admin/base.html" %}
{% load static %}

{% block extrastyle %}
  {{ block.super }}
  {# cache-busting query param to avoid stale CSS in browsers #}
  <link rel="stylesheet" href="{% static 'admin_theme.css' %}?v=20260202">
{% endblock %}

{% block nav-global %}
  <div class="admin-quickbar">
    <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Сменить тему">
      <span class="theme-toggle__icon">☾</span>
    </button>
  </div>
{% endblock %}

{% block extrafooter %}
  {{ block.super }}
  <script>
    (function() {
      const STORAGE_KEY = 'factory_admin_theme';
      const root = document.documentElement;
      const btn = document.getElementById('theme-toggle');

      // Удаляем возможные дубликаты кнопки темы
      document.querySelectorAll('.theme-toggle').forEach(el => {
        if (el.id !== 'theme-toggle') el.remove();
      });

      const setTheme = (theme) => {
        const target = theme === 'light' ? 'light' : 'dark';
        root.classList.remove('light', 'dark');
        root.classList.add(target);
        root.setAttribute('data-theme', target);
        localStorage.setItem(STORAGE_KEY, target);
        if (btn) btn.querySelector('.theme-toggle__icon').textContent = target === 'light' ? '☀︎' : '☾';
      };

      const saved = localStorage.getItem(STORAGE_KEY);
      let current = saved === 'light' ? 'light' : 'dark';
      setTheme(current); // принудительно только dark/light

      if (btn) {
        btn.addEventListener('click', () => {
          current = current === 'dark' ? 'light' : 'dark';
          setTheme(current);
        });
      }

      // Фильтр по пунктам меню — инъекция поля в сайдбар
      const navSidebar = document.getElementById('nav-sidebar');
      if (navSidebar) {
        const filterWrap = document.createElement('div');
        filterWrap.className = 'nav-filter-wrap';
        const filterInput = document.createElement('input');
        filterInput.type = 'search';
        filterInput.id = 'nav-filter';
        filterInput.className = 'nav-filter-input';
        filterInput.placeholder = 'Фильтр меню...';
        filterInput.setAttribute('aria-label', 'Фильтр меню');
        filterWrap.appendChild(filterInput);
        navSidebar.prepend(filterWrap);

        const items = Array.from(navSidebar.querySelectorAll('a'));
        filterInput.addEventListener('input', (e) => {
          const q = e.target.value.toLowerCase();
          items.forEach((link) => {
            const text = link.textContent.toLowerCase();
            const row = link.closest('tr, li, div, dd');
            if (!row) return;
            row.style.display = (!q || text.includes(q)) ? '' : 'none';
          });
        });
      }
    })();
  </script>
{% endblock %}
```

91. templates/admin/index.html
```html
{% extends "admin/index.html" %}

{% block content %}
<div id="content-main" class="dashboard-full">
  <div class="dashboard-grid">
    {% for category, models in categorized_list %}
      {% if models %}
      <div class="dash-card">
        <div class="dash-card__header">
          <h2>{{ category }}</h2>
        </div>
        <div class="dash-card__body">
          {% for model in models %}
            <div class="dash-entry">
              <div class="dash-entry__title">
                <a href="{{ model.admin_url }}">{{ model.name }}</a>
              </div>
              <div class="dash-entry__actions">
                {% if model.add_url %}<a class="pill pill--primary" href="{{ model.add_url }}">Добавить</a>{% endif %}
                <a class="pill pill--ghost" href="{{ model.admin_url }}">Список</a>
              </div>
            </div>
          {% endfor %}
        </div>
      </div>
      {% endif %}
    {% endfor %}
  </div>
</div>
{% endblock %}
```

92. templates/admin_panel/access.html
```html
{% extends "base.html" %}

{% block title %}Роли и доступы{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Роли и доступы{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/">Админ‑панель</a> / Роли и доступы
{% endblock %}

{% block content %}
  <div class="card">
    <h6>Матрица доступа</h6>
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Раздел</th>
            {% for r in roles %}
              <th>{{ r.name }}</th>
            {% endfor %}
          </tr>
        </thead>
        <tbody>
          {% for row in rows %}
            <tr>
              <td><a href="{{ row.url }}" class="text-decoration-none">{{ row.name }}</a></td>
              {% for r in roles %}
                <td>
                  {% if r.name in row.allowed %}
                    ✅
                  {% else %}
                    —
                  {% endif %}
                </td>
              {% endfor %}
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

93. templates/admin_panel/backup_schedule.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/backups/">Резервные копии</a> / Расписание
{% endblock %}

{% block content %}
  <div class="card">
    <form method="post" novalidate>
      {% csrf_token %}
      <div class="row g-3">
        {% for field in form %}
          <div class="col-md-6">
            <label class="form-label">{{ field.label }}</label>
            {{ field }}
            {% if field.errors %}
              <div class="text-danger small mt-1">{{ field.errors|striptags }}</div>
            {% endif %}
          </div>
        {% endfor %}
      </div>
      <div class="d-flex gap-2 mt-4">
        <button class="btn btn-primary">Сохранить</button>
        <a href="/admin-panel/backups/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

94. templates/admin_panel/backups.html
```html
{% extends "base.html" %}

{% block title %}Резервные копии{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Резервные копии{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/">Админ‑панель</a> / Резервные копии
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Резервные копии</h4>
    <div class="d-flex gap-2">
      <a href="/admin-panel/backups/create/" class="btn btn-primary">Создать бэкап</a>
      <a href="/admin-panel/backups/schedule/" class="btn btn-outline-secondary">Расписание</a>
    </div>
  </div>

  {% if schedule %}
    <div class="card mb-3">
      <div class="d-flex justify-content-between align-items-center">
        <div>
          <div class="fw-semibold">Автобэкапы</div>
          <div class="text-muted small">{{ schedule.get_frequency_display }} · {{ schedule.is_active|yesno:"включено,выключено" }}</div>
        </div>
        <a href="/admin-panel/backups/schedule/" class="btn btn-outline-secondary btn-sm">Изменить</a>
      </div>
    </div>
  {% endif %}

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Файл</th>
            <th>Размер</th>
            <th>Статус</th>
            <th>Создан</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for item in backups %}
            {% with b=item.obj %}
            <tr>
              <td>{{ b.file_path }}</td>
              <td>{{ item.size }} байт</td>
              <td>{{ b.get_status_display }}</td>
              <td>{{ b.created_at|date:"d.m.Y H:i" }}</td>
              <td class="text-end">
                <form method="post" action="/admin-panel/backups/{{ b.id }}/restore/" class="d-inline">
                  {% csrf_token %}
                  <button class="btn btn-sm btn-outline-secondary">Восстановить</button>
                </form>
              </td>
            </tr>
            {% endwith %}
          {% empty %}
            <tr><td colspan="5" class="text-muted">Бэкапов нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

95. templates/admin_panel/data_check.html
```html
{% extends "base.html" %}

{% block title %}Проверка данных{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Проверка данных{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/">Админ‑панель</a> / Проверка данных
{% endblock %}

{% block content %}
  <div class="card mb-3">
    <form method="post">
      {% csrf_token %}
      <div class="d-flex align-items-center gap-2">
        <button class="btn btn-primary">Запустить проверки</button>
        <span class="text-muted">Проверка связей и качества данных</span>
      </div>
    </form>
  </div>

  <div class="card">
    <h6>Результаты</h6>
    <div class="row g-3">
      <div class="col-md-6">
        <div class="card">
          <h6>Ошибки</h6>
          <ul class="list-group list-group-flush">
            {% for e in report.errors %}
              <li class="list-group-item">{{ e }}</li>
            {% empty %}
              <li class="list-group-item text-muted">Ошибок нет</li>
            {% endfor %}
          </ul>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card">
          <h6>Предупреждения</h6>
          <ul class="list-group list-group-flush">
            {% for w in report.warnings %}
              <li class="list-group-item">{{ w }}</li>
            {% empty %}
              <li class="list-group-item text-muted">Предупреждений нет</li>
            {% endfor %}
          </ul>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
```

96. templates/admin_panel/entities/delete.html
```html
{% extends "base.html" %}

{% block title %}Удаление{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Админ‑панель: {{ entity.label }}{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/admin/">Кабинет администратора</a> /
  <a href="/admin-panel/">Админ‑панель</a> /
  <a href="/admin-panel/entities/{{ entity.slug }}/">{{ entity.label }}</a> /
  Удаление
{% endblock %}

{% block content %}
  <div class="card">
    <h5 class="mb-2">Удаление записи</h5>
    <p class="text-muted">Вы собираетесь удалить запись: <strong>{{ obj }}</strong></p>

    {% if blockers %}
      <div class="alert alert-warning">
        <div class="fw-semibold mb-1">Удаление недоступно:</div>
        <ul class="mb-0">
          {% for b in blockers %}
            <li>{{ b }}</li>
          {% endfor %}
        </ul>
      </div>
      <a href="/admin-panel/entities/{{ entity.slug }}/{{ obj.pk }}/" class="btn btn-outline-secondary">Назад</a>
    {% else %}
      <form method="post">
        {% csrf_token %}
        <div class="d-flex gap-2">
          <button class="btn btn-danger" type="submit">Удалить</button>
          <a href="/admin-panel/entities/{{ entity.slug }}/{{ obj.pk }}/" class="btn btn-outline-secondary">Отмена</a>
        </div>
      </form>
    {% endif %}
  </div>
{% endblock %}
```

97. templates/admin_panel/entities/detail.html
```html
{% extends "base.html" %}

{% block title %}{{ entity.label }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Админ‑панель: {{ entity.label }}{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/admin/">Кабинет администратора</a> /
  <a href="/admin-panel/">Админ‑панель</a> /
  <a href="/admin-panel/entities/{{ entity.slug }}/">{{ entity.label }}</a> /
  Карточка
{% endblock %}

{% block content %}
  <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
    <div>
      <h4 class="mb-1">{{ entity.label }}</h4>
      <div class="text-muted">Карточка записи</div>
    </div>
    <div class="d-flex gap-2">
      <a href="/admin-panel/entities/{{ entity.slug }}/{{ obj.pk }}/edit/" class="btn btn-outline-secondary">Редактировать</a>
      <a href="/admin-panel/entities/{{ entity.slug }}/{{ obj.pk }}/delete/" class="btn btn-outline-danger">Удалить</a>
    </div>
  </div>

  <div class="card mb-3">
    <h6 class="mb-3">Данные</h6>
    <div class="row">
      {% for field in fields %}
        <div class="col-md-6 mb-3">
          <div class="text-muted small">{{ field.label }}</div>
          <div>{{ field.value }}</div>
        </div>
      {% endfor %}
    </div>
  </div>

  {% for inline in inline_sections %}
    <div class="card mb-3">
      <div class="d-flex justify-content-between align-items-center mb-2">
        <h6 class="mb-0">{{ inline.label }}</h6>
        <span class="text-muted small">Записей: {{ inline.count }}</span>
      </div>
      <div class="table-responsive">
        <table class="table mb-0">
          <thead>
            <tr>
              {% for header in inline.headers %}
                <th>{{ header }}</th>
              {% endfor %}
            </tr>
          </thead>
          <tbody>
            {% for row in inline.rows %}
              <tr>
                {% for cell in row %}
                  <td>{{ cell }}</td>
                {% endfor %}
              </tr>
            {% empty %}
              <tr>
                <td colspan="{{ inline.headers|length }}" class="text-muted">Связанные записи не найдены</td>
              </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>
  {% endfor %}
{% endblock %}
```

98. templates/admin_panel/entities/form.html
```html
{% extends "base.html" %}

{% block title %}{{ entity.label }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Админ‑панель: {{ entity.label }}{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/admin/">Кабинет администратора</a> /
  <a href="/admin-panel/">Админ‑панель</a> /
  <a href="/admin-panel/entities/{{ entity.slug }}/">{{ entity.label }}</a> /
  {% if is_edit %}Редактирование{% else %}Создание{% endif %}
{% endblock %}

{% block content %}
  <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
    <div>
      <h4 class="mb-1">{{ entity.label }}</h4>
      <div class="text-muted">
        {% if is_edit %}Редактирование записи{% else %}Создание записи{% endif %}
      </div>
    </div>
    <a href="/admin-panel/entities/{{ entity.slug }}/" class="btn btn-outline-secondary">Назад</a>
  </div>

  <div class="card">
    <form method="post">
      {% csrf_token %}
      {% if form.non_field_errors %}
        <div class="alert alert-danger">{{ form.non_field_errors }}</div>
      {% endif %}
      <div class="row">
        {% for field in form %}
          {% with size=field.field.widget.attrs.data_size %}
          <div class="{% if size == 'full' %}col-12{% else %}col-md-6{% endif %} mb-3">
            <label class="form-label">{{ field.label }}</label>
            {{ field }}
            {% if field.help_text %}
              <div class="form-text">{{ field.help_text }}</div>
            {% endif %}
            {% for error in field.errors %}
              <div class="invalid-feedback d-block">{{ error }}</div>
            {% endfor %}
          </div>
          {% endwith %}
        {% endfor %}
      </div>
      <div class="d-flex gap-2">
        <button class="btn btn-primary" type="submit">Сохранить</button>
        <a href="/admin-panel/entities/{{ entity.slug }}/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```
