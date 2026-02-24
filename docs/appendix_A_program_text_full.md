ПРИЛОЖЕНИЕ А. ТЕКСТ ПРОГРАММЫ (ПОЛНАЯ СБОРКА)

АННОТАЦИЯ
В данном документе собран почти весь исходный код web-приложения «Art Culinary CRM».
Включены серверные модули, шаблоны и статические исходники (без служебных артефактов окружения).

1. СПИСОК ФАЙЛОВ

| № | Файл |
|---:|---|
| 1 | `.github/workflows/pipeline.yaml` |
| 2 | `.gitlab-ci.yml` |
| 3 | `README.md` |
| 4 | `accounts/__init__.py` |
| 5 | `accounts/admin.py` |
| 6 | `accounts/apps.py` |
| 7 | `accounts/context_processors.py` |
| 8 | `accounts/management/__init__.py` |
| 9 | `accounts/management/commands/__init__.py` |
| 10 | `accounts/management/commands/seed_demo.py` |
| 11 | `accounts/migrations/__init__.py` |
| 12 | `accounts/models.py` |
| 13 | `accounts/tests.py` |
| 14 | `accounts/urls.py` |
| 15 | `accounts/utils.py` |
| 16 | `accounts/views.py` |
| 17 | `admin_panel/__init__.py` |
| 18 | `admin_panel/admin.py` |
| 19 | `admin_panel/apps.py` |
| 20 | `admin_panel/entity_config.py` |
| 21 | `admin_panel/forms.py` |
| 22 | `admin_panel/migrations/0001_initial.py` |
| 23 | `admin_panel/migrations/__init__.py` |
| 24 | `admin_panel/models.py` |
| 25 | `admin_panel/tests.py` |
| 26 | `admin_panel/urls.py` |
| 27 | `admin_panel/views.py` |
| 28 | `clients/__init__.py` |
| 29 | `clients/admin.py` |
| 30 | `clients/apps.py` |
| 31 | `clients/forms.py` |
| 32 | `clients/migrations/__init__.py` |
| 33 | `clients/models.py` |
| 34 | `clients/tests.py` |
| 35 | `clients/urls.py` |
| 36 | `clients/views.py` |
| 37 | `create_demo_users.py` |
| 38 | `crm/__init__.py` |
| 39 | `crm/admin.py` |
| 40 | `crm/admin_site.py` |
| 41 | `crm/api.py` |
| 42 | `crm/apps.py` |
| 43 | `crm/forms.py` |
| 44 | `crm/management/commands/seed_dishes.py` |
| 45 | `crm/management/commands/seed_logistics.py` |
| 46 | `crm/migrations/0001_initial.py` |
| 47 | `crm/migrations/0002_client_current_stage.py` |
| 48 | `crm/migrations/0003_client_created_at.py` |
| 49 | `crm/migrations/0004_order_archived.py` |
| 50 | `crm/migrations/0005_delivery_fields.py` |
| 51 | `crm/migrations/0006_picking_session_and_item_fields.py` |
| 52 | `crm/migrations/0007_logistics_profile_and_cargo_fields.py` |
| 53 | `crm/migrations/0008_update_logistics_status_and_route_type.py` |
| 54 | `crm/migrations/0009_alter_logisticianprofile_id_alter_order_status.py` |
| 55 | `crm/migrations/0010_courier_current_latitude_courier_current_longitude_and_more.py` |
| 56 | `crm/migrations/0011_delivery_delivery_date_route_max_duration_minutes_and_more.py` |
| 57 | `crm/migrations/0012_routestop_proof_review_comment_and_more.py` |
| 58 | `crm/migrations/0013_equipment_client_daily_max_weight_kg_and_more.py` |
| 59 | `crm/migrations/0014_dish_default_price.py` |
| 60 | `crm/migrations/0015_dish_daily_capacity.py` |
| 61 | `crm/migrations/0015_dish_uom_fields.py` |
| 62 | `crm/migrations/0016_merge_0015_dish_daily_capacity_0015_dish_uom_fields.py` |
| 63 | `crm/migrations/__init__.py` |
| 64 | `crm/models.py` |
| 65 | `dashboard/__init__.py` |
| 66 | `dashboard/admin.py` |
| 67 | `dashboard/apps.py` |
| 68 | `dashboard/migrations/__init__.py` |
| 69 | `dashboard/models.py` |
| 70 | `dashboard/tests.py` |
| 71 | `dashboard/urls.py` |
| 72 | `dashboard/views.py` |
| 73 | `factory_crm/__init__.py` |
| 74 | `factory_crm/asgi.py` |
| 75 | `factory_crm/settings.py` |
| 76 | `factory_crm/urls.py` |
| 77 | `factory_crm/views.py` |
| 78 | `factory_crm/wsgi.py` |
| 79 | `locustfile.py` |
| 80 | `logistics/__init__.py` |
| 81 | `logistics/admin.py` |
| 82 | `logistics/apps.py` |
| 83 | `logistics/forms.py` |
| 84 | `logistics/migrations/__init__.py` |
| 85 | `logistics/models.py` |
| 86 | `logistics/tests.py` |
| 87 | `logistics/urls.py` |
| 88 | `logistics/views.py` |
| 89 | `manage.py` |
| 90 | `orders/__init__.py` |
| 91 | `orders/admin.py` |
| 92 | `orders/apps.py` |
| 93 | `orders/forms.py` |
| 94 | `orders/migrations/__init__.py` |
| 95 | `orders/models.py` |
| 96 | `orders/tests.py` |
| 97 | `orders/urls.py` |
| 98 | `orders/views.py` |
| 99 | `portal/__init__.py` |
| 100 | `portal/forms.py` |
| 101 | `portal/urls.py` |
| 102 | `portal/utils.py` |
| 103 | `portal/views.py` |
| 104 | `reports/__init__.py` |
| 105 | `reports/admin.py` |
| 106 | `reports/apps.py` |
| 107 | `reports/forms.py` |
| 108 | `reports/migrations/0001_initial.py` |
| 109 | `reports/migrations/0002_report_validation.py` |
| 110 | `reports/migrations/__init__.py` |
| 111 | `reports/models.py` |
| 112 | `reports/tests.py` |
| 113 | `reports/urls.py` |
| 114 | `reports/views.py` |
| 115 | `requirements.txt` |
| 116 | `static/admin_theme.css` |
| 117 | `static/css/app.css` |
| 118 | `static/login_root.css` |
| 119 | `static/manager.css` |
| 120 | `templates/accounts/login.html` |
| 121 | `templates/accounts/login_base.html` |
| 122 | `templates/accounts/password_reset_complete.html` |
| 123 | `templates/accounts/password_reset_confirm.html` |
| 124 | `templates/accounts/password_reset_done.html` |
| 125 | `templates/accounts/password_reset_email.html` |
| 126 | `templates/accounts/password_reset_form.html` |
| 127 | `templates/accounts/password_reset_subject.txt` |
| 128 | `templates/admin/base_site.html` |
| 129 | `templates/admin/index.html` |
| 130 | `templates/admin_panel/access.html` |
| 131 | `templates/admin_panel/backup_schedule.html` |
| 132 | `templates/admin_panel/backups.html` |
| 133 | `templates/admin_panel/data_check.html` |
| 134 | `templates/admin_panel/entities/delete.html` |
| 135 | `templates/admin_panel/entities/detail.html` |
| 136 | `templates/admin_panel/entities/form.html` |
| 137 | `templates/admin_panel/entities/list.html` |
| 138 | `templates/admin_panel/index.html` |
| 139 | `templates/admin_panel/role_form.html` |
| 140 | `templates/admin_panel/roles_list.html` |
| 141 | `templates/admin_panel/user_delete.html` |
| 142 | `templates/admin_panel/user_form.html` |
| 143 | `templates/admin_panel/user_password.html` |
| 144 | `templates/admin_panel/users_list.html` |
| 145 | `templates/base.html` |
| 146 | `templates/clients/delete.html` |
| 147 | `templates/clients/detail.html` |
| 148 | `templates/clients/form.html` |
| 149 | `templates/clients/list.html` |
| 150 | `templates/courier/profile.html` |
| 151 | `templates/courier/route_detail.html` |
| 152 | `templates/courier/routes.html` |
| 153 | `templates/dashboard/admin.html` |
| 154 | `templates/dashboard/logistic.html` |
| 155 | `templates/dashboard/manager.html` |
| 156 | `templates/dashboard/picker.html` |
| 157 | `templates/login_root.html` |
| 158 | `templates/logistics/couriers.html` |
| 159 | `templates/logistics/delivery_card.html` |
| 160 | `templates/logistics/form.html` |
| 161 | `templates/logistics/list.html` |
| 162 | `templates/logistics/profile.html` |
| 163 | `templates/logistics/route_detail.html` |
| 164 | `templates/logistics/route_form.html` |
| 165 | `templates/logistics/routes.html` |
| 166 | `templates/manager/proof_review_list.html` |
| 167 | `templates/manager_clients.html` |
| 168 | `templates/manager_dashboard.html` |
| 169 | `templates/manager_orders.html` |
| 170 | `templates/orders/archive.html` |
| 171 | `templates/orders/delete.html` |
| 172 | `templates/orders/form.html` |
| 173 | `templates/orders/list.html` |
| 174 | `templates/orders/picker_detail.html` |
| 175 | `templates/orders/picker_list.html` |
| 176 | `templates/partials/sidebars/admin.html` |
| 177 | `templates/partials/sidebars/courier.html` |
| 178 | `templates/partials/sidebars/logistic.html` |
| 179 | `templates/partials/sidebars/manager.html` |
| 180 | `templates/partials/sidebars/picker.html` |
| 181 | `templates/portal/base_portal.html` |
| 182 | `templates/portal/client_form.html` |
| 183 | `templates/portal/clients_list.html` |
| 184 | `templates/portal/delivery_plan.html` |
| 185 | `templates/portal/login.html` |
| 186 | `templates/portal/logistic_dashboard.html` |
| 187 | `templates/portal/manager_dashboard.html` |
| 188 | `templates/portal/order_form.html` |
| 189 | `templates/portal/orders_list.html` |
| 190 | `templates/portal/picker_dashboard.html` |
| 191 | `templates/portal/sysadmin_dashboard.html` |
| 192 | `templates/registration/login.html` |
| 193 | `templates/reports/analytics.html` |
| 194 | `templates/reports/form.html` |
| 195 | `templates/reports/list.html` |

2. ТЕКСТ ФАЙЛОВ

1. .github/workflows/pipeline.yaml
```yaml
name: Django CI (build/lint/api/security)

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

env:
  VENV_PATH: .venv
  DJANGO_SETTINGS_MODULE: factory_crm.settings
  SECRET_KEY: ci-temp-secret
  DEBUG: "true"
  ALLOWED_HOSTS: localhost,127.0.0.1
  PIP_CACHE_DIR: ${{ github.workspace }}/.cache/pip

jobs:
  build:
    name: build
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          # Лучше ставить стабильную версию, которую точно поддерживает setup-python
          python-version: "3.12"
          cache: "pip"

      - name: Prepare venv & install deps
        run: |
          echo "Подготовка виртуального окружения и установка зависимостей"
          python --version
          python -m venv "$VENV_PATH"
          source "$VENV_PATH/bin/activate"
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Django check
        run: |
          echo "Проверяю корректность конфигурации Django"
          source "$VENV_PATH/bin/activate"
          python manage.py check
          echo "Проверка конфигурации завершена успешно"

      - name: Collect static
        run: |
          echo "Собираю статические файлы"
          source "$VENV_PATH/bin/activate"
          python manage.py collectstatic --noinput
          echo "Статические файлы собраны"

      - name: Upload staticfiles artifact
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: staticfiles
          path: staticfiles/
          retention-days: 7

  lint:
    name: lint
    runs-on: ubuntu-latest
    needs: [ build ]
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Prepare venv & install deps
        run: |
          python -m venv "$VENV_PATH"
          source "$VENV_PATH/bin/activate"
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Ruff lint (report)
        continue-on-error: true
        run: |
          source "$VENV_PATH/bin/activate"
          pip install ruff
          mkdir -p reports
          ruff check . --output-format=json > reports/ruff.json

      - name: Upload ruff report
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: ruff-report
          path: reports/ruff.json
          retention-days: 7

  api:
    name: api
    runs-on: ubuntu-latest
    needs: [ build ]
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Prepare venv & install deps
        run: |
          python -m venv "$VENV_PATH"
          source "$VENV_PATH/bin/activate"
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Generate OpenAPI schema (drf-spectacular)
        run: |
          echo "Генерирую OpenAPI схему"
          source "$VENV_PATH/bin/activate"
          mkdir -p artifacts
          python manage.py spectacular --file artifacts/openapi.yaml
          echo "OpenAPI схема создана"

      - name: Upload OpenAPI artifact
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: openapi-schema
          path: artifacts/openapi.yaml
          retention-days: 7

  security:
    name: security
    runs-on: ubuntu-latest
    needs: [ build ]
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: "pip"

      - name: Prepare venv & install deps
        run: |
          python -m venv "$VENV_PATH"
          source "$VENV_PATH/bin/activate"
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Bandit (report)
        continue-on-error: true
        run: |
          echo "Запускаю анализ безопасности Bandit"
          source "$VENV_PATH/bin/activate"
          pip install bandit
          mkdir -p reports
          bandit -r . -f json -o reports/bandit.json

      - name: pip-audit (report)
        continue-on-error: true
        run: |
          echo "Проверяю зависимости на известные уязвимости"
          source "$VENV_PATH/bin/activate"
          pip install pip-audit
          mkdir -p reports
          pip-audit -r requirements.txt -f json -o reports/pip-audit.json

      - name: Upload security reports
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: security-reports
          path: reports/
          retention-days: 7
```

2. .gitlab-ci.yml
```yaml
stages:
  - build
  - lint
  - api
  - security

variables:
  VENV_PATH: ".venv"
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"
  DJANGO_SETTINGS_MODULE: "factory_crm.settings"
  SECRET_KEY: "ci-temp-secret"
  DEBUG: "true"
  ALLOWED_HOSTS: "localhost,127.0.0.1"

cache:
  key: "venv-$CI_COMMIT_REF_SLUG"
  paths:
    - .cache/pip/
    - .venv/

before_script:
  - echo "Подготовка виртуального окружения и установка зависимостей"
  - python3 --version
  - python3 -m venv "$VENV_PATH"
  - source "$VENV_PATH/bin/activate"
  - python -m pip install --upgrade pip
  - pip install -r requirements.txt

build:check:
  stage: build
  script:
    - echo "Проверяю корректность конфигурации Django"
    - source "$VENV_PATH/bin/activate"
    - python manage.py check
    - echo "Проверка конфигурации завершена успешно"

build:collectstatic:
  stage: build
  script:
    - echo "Собираю статические файлы"
    - source "$VENV_PATH/bin/activate"
    - python manage.py collectstatic --noinput
    - echo "Статические файлы собраны"
  artifacts:
    when: always
    expire_in: 7 days
    paths:
      - staticfiles/

lint:ruff:
  stage: lint
  script:
    - echo "Запускаю линтер Ruff"
    - source "$VENV_PATH/bin/activate"
    - pip install ruff
    - mkdir -p reports
    - ruff check . --output-format=json > reports/ruff.json || true
    - echo "Отчет Ruff сформирован"
  artifacts:
    when: always
    expire_in: 7 days
    paths:
      - reports/ruff.json
  allow_failure: true

api:schema:
  stage: api
  script:
    - echo "Генерирую OpenAPI схему"
    - source "$VENV_PATH/bin/activate"
    - mkdir -p artifacts
    - python manage.py spectacular --file artifacts/openapi.yaml
    - echo "OpenAPI схема создана"
  artifacts:
    when: always
    expire_in: 7 days
    paths:
      - artifacts/openapi.yaml

security:bandit:
  stage: security
  script:
    - echo "Запускаю анализ безопасности Bandit"
    - source "$VENV_PATH/bin/activate"
    - pip install bandit
    - mkdir -p reports
    - bandit -r . -f json -o reports/bandit.json || true
    - echo "Отчет Bandit сформирован"
  artifacts:
    when: always
    expire_in: 7 days
    paths:
      - reports/bandit.json
  allow_failure: true

security:pip-audit:
  stage: security
  script:
    - echo "Проверяю зависимости на известные уязвимости"
    - source "$VENV_PATH/bin/activate"
    - pip install pip-audit
    - mkdir -p reports
    - pip-audit -r requirements.txt -f json -o reports/pip-audit.json || true
    - echo "Отчет pip-audit сформирован"
  artifacts:
    when: always
    expire_in: 7 days
    paths:
      - reports/pip-audit.json
  allow_failure: true
```

3. README.md
```markdown
# Art Culinary CRM (Django)

Минимальный каркас CRM для завода готовой еды по предоставленной схеме БД.

## Быстрый старт
1. Создать и активировать venv:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Установить зависимости (требуется доступ в интернет или локальный индекс PyPI):
   ```bash
   pip install -r requirements.txt
   ```
3. Заполнить переменные окружения (см. `.env.example`). Для PostgreSQL:
   ```bash
   export $(grep -v '^#' .env.example | xargs)
   ```
   или скопировать `.env` и подставить реальные значения.
4. Применить миграции:
   ```bash
   python manage.py migrate
   ```
   При желании загрузить демо-данные:
   ```bash
   python manage.py loaddata fixtures/sample_data.json
   ```
   Документированный API:
   - схема: http://127.0.0.1:8000/api/schema/
   - Swagger UI: http://127.0.0.1:8000/api/docs/
   - базовый REST: http://127.0.0.1:8000/api/ (endpoints)
5. Создать суперпользователя для доступа в админку:
   ```bash
   python manage.py createsuperuser
   ```
6. Запустить dev-сервер:
   ```bash
   python manage.py runserver
   ```
7. Кастомные кабинеты (без Django admin):
   - Логин: http://127.0.0.1:8000/login/
   - Кабинет менеджера: http://127.0.0.1:8000/manager/
   - Клиенты: http://127.0.0.1:8000/manager/clients/
   - Заказы: http://127.0.0.1:8000/manager/orders/

## Примечания по модели
- Пользователи имеют роли через промежуточную таблицу `UserRole`.
- Клиенты, контакты, этапы, история этапов и взаимодействия отражают воронку продаж.
- Заказы и позиции учитывают как блюда каталога, так и сырьё/ингредиенты и кастомные техкарты.
- Логистика: доставки привязаны к заказам, маршруты и остановки маршрутов управляют курьерами.
- Техкарты блюд содержат состав и варианты выхода/массы.

Структура соответствует предоставленной ER-диаграмме и готова к генерации реальной БД через `migrate`.
```

4. accounts/__init__.py
```python
```

5. accounts/admin.py
```python
from django.contrib import admin

# Register your models here.
```

6. accounts/apps.py
```python
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
```

7. accounts/context_processors.py
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

8. accounts/management/__init__.py
```python

```

9. accounts/management/commands/__init__.py
```python

```

10. accounts/management/commands/seed_demo.py
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

11. accounts/migrations/__init__.py
```python
```

12. accounts/models.py
```python
from django.db import models

# Create your models here.
```

13. accounts/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

14. accounts/urls.py
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

15. accounts/utils.py
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

16. accounts/views.py
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

17. admin_panel/__init__.py
```python
```

18. admin_panel/admin.py
```python
from django.contrib import admin

# Register your models here.
```

19. admin_panel/apps.py
```python
from django.apps import AppConfig


class AdminPanelConfig(AppConfig):
    name = 'admin_panel'
```

20. admin_panel/entity_config.py
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

21. admin_panel/forms.py
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

22. admin_panel/migrations/0001_initial.py
```python
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
```

23. admin_panel/migrations/__init__.py
```python
```

24. admin_panel/models.py
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

25. admin_panel/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

26. admin_panel/urls.py
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

27. admin_panel/views.py
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

28. clients/__init__.py
```python
```

29. clients/admin.py
```python
from django.contrib import admin

# Register your models here.
```

30. clients/apps.py
```python
from django.apps import AppConfig


class ClientsConfig(AppConfig):
    name = 'clients'
```

31. clients/forms.py
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

32. clients/migrations/__init__.py
```python
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

37. create_demo_users.py
```python
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
```

38. crm/__init__.py
```python
# CRM app package
```

39. crm/admin.py
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

40. crm/admin_site.py
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

41. crm/api.py
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

42. crm/apps.py
```python
from django.apps import AppConfig


class CrmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crm'
    verbose_name = 'CRM'
```

43. crm/forms.py
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

44. crm/management/commands/seed_dishes.py
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

45. crm/management/commands/seed_logistics.py
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

46. crm/migrations/0001_initial.py
```python
# Generated by Django 6.0.1 on 2026-02-02 20:43

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CooperationStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название этапа')),
                ('order', models.PositiveSmallIntegerField(default=1, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Этап сотрудничества',
                'verbose_name_plural': 'Этапы сотрудничества',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Телефон')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('client_type', models.CharField(choices=[('store', 'Магазин'), ('cafe', 'Кафе'), ('restaurant', 'Ресторан'), ('distributor', 'Дистрибьютор'), ('other', 'Другое')], default='store', max_length=32, verbose_name='Тип')),
                ('inn', models.CharField(blank=True, max_length=20, verbose_name='ИНН')),
                ('kpp', models.CharField(blank=True, max_length=20, verbose_name='КПП')),
                ('default_delivery_address', models.CharField(blank=True, max_length=255, verbose_name='Адрес доставки по умолчанию')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Телефон')),
                ('status', models.CharField(choices=[('prospect', 'Переговоры'), ('active', 'Активен'), ('paused', 'Приостановлен'), ('lost', 'Закрыт')], default='prospect', max_length=20, verbose_name='Статус')),
                ('responsible_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='ClientContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('position', models.CharField(blank=True, max_length=128, verbose_name='Должность')),
                ('phone', models.CharField(blank=True, max_length=32, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Основной')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='crm.client')),
            ],
            options={
                'verbose_name': 'Контакт клиента',
                'verbose_name_plural': 'Контакты клиента',
            },
        ),
        migrations.CreateModel(
            name='ClientStageHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='changed_stages', to=settings.AUTH_USER_MODEL)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage_history', to='crm.client')),
                ('stage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='histories', to='crm.cooperationstage')),
            ],
            options={
                'verbose_name': 'История этапов клиента',
                'verbose_name_plural': 'Истории этапов клиента',
                'ordering': ['-changed_at'],
            },
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transport_type', models.CharField(blank=True, max_length=64, verbose_name='Тип транспорта')),
                ('experience_years', models.PositiveSmallIntegerField(default=0, verbose_name='Опыт (лет)')),
                ('status', models.CharField(choices=[('active', 'Активен'), ('inactive', 'Не активен'), ('on_route', 'В рейсе')], default='active', max_length=20, verbose_name='Статус')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='courier_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Курьер',
                'verbose_name_plural': 'Курьеры',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('unit', models.CharField(default='шт', max_length=32, verbose_name='Единица измерения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_dishes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Блюдо каталога',
                'verbose_name_plural': 'Блюда каталога',
            },
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_type', models.CharField(choices=[('call', 'Звонок'), ('meeting', 'Встреча'), ('email', 'Email'), ('message', 'Сообщение'), ('other', 'Другое')], max_length=20, verbose_name='Тип')),
                ('note', models.TextField(blank=True, verbose_name='Заметка')),
                ('happened_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата/время')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='crm.client')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='interactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Взаимодействие',
                'verbose_name_plural': 'Взаимодействия',
                'ordering': ['-happened_at'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=50, unique=True, verbose_name='Номер заказа')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес доставки')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('confirmed', 'Подтвержден'), ('in_progress', 'В производстве'), ('shipped', 'Отгружен'), ('delivered', 'Доставлен'), ('cancelled', 'Отменен')], default='draft', max_length=20, verbose_name='Статус')),
                ('comments', models.TextField(blank=True, verbose_name='Комментарии')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Сумма итого')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='crm.client')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField(blank=True, null=True, verbose_name='Время выезда')),
                ('delivered_at', models.DateTimeField(blank=True, null=True, verbose_name='Доставлено')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Адрес')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('is_sent', models.BooleanField(default=False, verbose_name='Отправлен')),
                ('courier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deliveries', to='crm.courier')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliveries', to='crm.order')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_date', models.DateField(verbose_name='Дата маршрута')),
                ('status', models.CharField(choices=[('draft', 'Черновик'), ('planned', 'Запланирован'), ('in_progress', 'В пути'), ('done', 'Завершен')], default='draft', max_length=20, verbose_name='Статус')),
                ('notes', models.TextField(blank=True, verbose_name='Заметки')),
                ('logistician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='routes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
            },
        ),
        migrations.CreateModel(
            name='RouteStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_index', models.PositiveSmallIntegerField(default=1, verbose_name='Порядок')),
                ('planned_time', models.DateTimeField(blank=True, null=True, verbose_name='Плановое время')),
                ('actual_time', models.DateTimeField(blank=True, null=True, verbose_name='Фактическое время')),
                ('note', models.CharField(blank=True, max_length=255, verbose_name='Примечание')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_stops', to='crm.delivery')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stops', to='crm.route')),
            ],
            options={
                'verbose_name': 'Остановка маршрута',
                'verbose_name_plural': 'Остановки маршрута',
                'ordering': ['sequence_index'],
            },
        ),
        migrations.CreateModel(
            name='TechCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_label', models.CharField(max_length=32, verbose_name='Версия/номер')),
                ('description', models.TextField(blank=True, verbose_name='Описание/технология')),
                ('photo_url', models.URLField(blank=True, verbose_name='Фото')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_tech_cards', to=settings.AUTH_USER_MODEL)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tech_cards', to='crm.dish')),
            ],
            options={
                'verbose_name': 'Техкарта блюда',
                'verbose_name_plural': 'Техкарты блюд',
                'unique_together': {('dish', 'version_label')},
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Кол-во')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('line_total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=12, verbose_name='Сумма')),
                ('supply_type', models.CharField(blank=True, max_length=64, verbose_name='Тип поставки/заявки')),
                ('dish', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='crm.dish')),
                ('ingredient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='crm.ingredient')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='crm.order')),
                ('custom_tech_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='crm.techcard')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиции заказа',
            },
        ),
        migrations.CreateModel(
            name='TechCardComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Количество')),
                ('note', models.CharField(blank=True, max_length=255, verbose_name='Примечание')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='crm.ingredient')),
                ('tech_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='crm.techcard')),
            ],
            options={
                'verbose_name': 'Состав техкарты',
                'verbose_name_plural': 'Состав техкарт',
            },
        ),
        migrations.CreateModel(
            name='TechCardVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Количество')),
                ('note', models.CharField(blank=True, max_length=255, verbose_name='Примечание')),
                ('tech_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='crm.techcard')),
            ],
            options={
                'verbose_name': 'Сорт/вариант техкарты',
                'verbose_name_plural': 'Сорта/варианты техкарт',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Роль пользователя',
                'verbose_name_plural': 'Роли пользователей',
                'unique_together': {('user', 'role')},
            },
        ),
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='users', through='crm.UserRole', to='crm.role'),
        ),
        migrations.CreateModel(
            name='CourierAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='crm.courier')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='crm.route')),
            ],
            options={
                'verbose_name': 'Назначение курьера',
                'verbose_name_plural': 'Назначения курьеров',
                'unique_together': {('courier', 'route')},
            },
        ),
    ]
```

47. crm/migrations/0002_client_current_stage.py
```python
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="current_stage",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="clients",
                to="crm.cooperationstage",
                verbose_name="Текущий этап",
            ),
        ),
    ]
```

48. crm/migrations/0003_client_created_at.py
```python
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
```

49. crm/migrations/0004_order_archived.py
```python
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
```

50. crm/migrations/0005_delivery_fields.py
```python
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0004_order_archived"),
    ]

    operations = [
        migrations.AddField(
            model_name="courier",
            name="zone",
            field=models.CharField(blank=True, max_length=128, verbose_name="Зона"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="planned_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Плановая дата/время"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="route",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="deliveries",
                to="crm.route",
            ),
        ),
        migrations.AddField(
            model_name="delivery",
            name="status",
            field=models.CharField(
                choices=[
                    ("unassigned", "Не назначено"),
                    ("planned", "Запланировано"),
                    ("on_route", "В пути"),
                    ("delivered", "Доставлено"),
                    ("cancelled", "Отмена"),
                ],
                default="unassigned",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
    ]
```

51. crm/migrations/0006_picking_session_and_item_fields.py
```python
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0005_delivery_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="picked_quantity",
            field=models.DecimalField(default=0, decimal_places=3, max_digits=10, verbose_name="Собрано фактически"),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="item_status",
            field=models.CharField(
                choices=[
                    ("not_started", "Не начато"),
                    ("in_progress", "В сборке"),
                    ("done", "Собрано"),
                    ("out_of_stock", "Нет в наличии"),
                    ("replaced", "Заменено"),
                ],
                default="not_started",
                max_length=20,
                verbose_name="Статус позиции",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="item_comment",
            field=models.CharField(blank=True, max_length=255, verbose_name="Комментарий по позиции"),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="replacement_text",
            field=models.CharField(blank=True, max_length=255, verbose_name="Замена"),
        ),
        migrations.CreateModel(
            name="PickingSession",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("note", models.TextField(blank=True, verbose_name="Примечание сборщика")),
                ("started_at", models.DateTimeField(blank=True, null=True, verbose_name="Начата")),
                ("finished_at", models.DateTimeField(blank=True, null=True, verbose_name="Завершена")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Обновлено")),
                ("order", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="picking_session", to="crm.order")),
                ("picker", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="picking_sessions", to="crm.user")),
            ],
            options={
                "verbose_name": "Сборка заказа",
                "verbose_name_plural": "Сборки заказов",
            },
        ),
    ]
```

52. crm/migrations/0007_logistics_profile_and_cargo_fields.py
```python
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0006_picking_session_and_item_fields"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogisticianProfile",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("region", models.CharField(blank=True, max_length=128, verbose_name="Регион")),
                ("city", models.CharField(blank=True, max_length=128, verbose_name="Город")),
                ("transport_types", models.JSONField(blank=True, default=list, verbose_name="Доступные типы транспорта")),
                ("timezone", models.CharField(default="UTC", max_length=64, verbose_name="Часовой пояс")),
                ("map_show_traffic", models.BooleanField(default=True, verbose_name="Показывать пробки")),
                (
                    "preferred_route_type",
                    models.CharField(
                        choices=[("fast", "Быстрый"), ("safe", "Безопасный"), ("economic", "Экономичный")],
                        default="fast",
                        max_length=16,
                        verbose_name="Предпочтительный тип маршрута",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name="logistic_profile", to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name": "Профиль логиста",
                "verbose_name_plural": "Профили логистов",
            },
        ),
        migrations.AddField(
            model_name="courier",
            name="payload_capacity_kg",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Грузоподъёмность (кг)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_volume_m3",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Объём кузова (м³)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_length_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Длина кузова (см)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_width_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Ширина кузова (см)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="cargo_height_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Высота кузова (см)"),
        ),
        migrations.AddField(
            model_name="courier",
            name="current_lat",
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name="Текущая широта"),
        ),
        migrations.AddField(
            model_name="courier",
            name="current_lng",
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name="Текущая долгота"),
        ),
        migrations.AddField(
            model_name="courier",
            name="location_updated_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Обновление геолокации"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_weight_kg",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Вес груза (кг)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_volume_m3",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Объём груза (м³)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_length_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Длина груза (см)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_width_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Ширина груза (см)"),
        ),
        migrations.AddField(
            model_name="delivery",
            name="cargo_height_cm",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name="Высота груза (см)"),
        ),
    ]
```

53. crm/migrations/0008_update_logistics_status_and_route_type.py
```python
from django.db import migrations, models


def migrate_courier_status(apps, schema_editor):
    Courier = apps.get_model("crm", "Courier")
    status_map = {
        "active": "free",
        "on_route": "busy",
        "inactive": "offline",
    }
    for old, new in status_map.items():
        Courier.objects.filter(status=old).update(status=new)


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0007_logistics_profile_and_cargo_fields"),
    ]

    operations = [
        migrations.RunPython(migrate_courier_status, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="courier",
            name="status",
            field=models.CharField(
                choices=[("free", "Свободен"), ("busy", "Занят"), ("offline", "Оффлайн")],
                default="free",
                max_length=20,
                verbose_name="Статус",
            ),
        ),
        migrations.AlterField(
            model_name="logisticianprofile",
            name="preferred_route_type",
            field=models.CharField(
                choices=[("fastest", "Самый быстрый"), ("safest", "Самый безопасный"), ("shortest", "Самый короткий")],
                default="fastest",
                max_length=16,
                verbose_name="Предпочтительный тип маршрута",
            ),
        ),
    ]
```

54. crm/migrations/0009_alter_logisticianprofile_id_alter_order_status.py
```python
# Generated by Django 6.0.1 on 2026-02-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_update_logistics_status_and_route_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logisticianprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('draft', 'Новый'), ('in_progress', 'Собирается'), ('confirmed', 'Собран'), ('shipped', 'Передан в доставку'), ('delivered', 'Доставлен'), ('cancelled', 'Отменён')], default='draft', max_length=20, verbose_name='Статус'),
        ),
    ]
```

55. crm/migrations/0010_courier_current_latitude_courier_current_longitude_and_more.py
```python
# Generated by Django 6.0.1 on 2026-02-12 20:17

from django.db import migrations, models


def migrate_courier_status(apps, schema_editor):
    Courier = apps.get_model("crm", "Courier")
    Courier.objects.filter(status="offline").update(status="on_route")


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_alter_logisticianprofile_id_alter_order_status'),
    ]

    operations = [
        migrations.RunPython(migrate_courier_status, migrations.RunPython.noop),
        migrations.AddField(
            model_name='courier',
            name='current_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Текущая широта (альт)'),
        ),
        migrations.AddField(
            model_name='courier',
            name='current_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Текущая долгота (альт)'),
        ),
        migrations.AddField(
            model_name='courier',
            name='max_volume',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Макс. объём (м³)'),
        ),
        migrations.AddField(
            model_name='courier',
            name='max_weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Макс. вес (кг)'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Долгота'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='status',
            field=models.CharField(choices=[('planned', 'Запланирована'), ('in_progress', 'В пути'), ('done', 'Завершена')], default='planned', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='courier',
            name='status',
            field=models.CharField(choices=[('free', 'Свободен'), ('busy', 'Занят'), ('on_route', 'В рейсе')], default='free', max_length=20, verbose_name='Статус'),
        ),
    ]
```

56. crm/migrations/0011_delivery_delivery_date_route_max_duration_minutes_and_more.py
```python
# Generated by Django 6.0.1 on 2026-02-12 21:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def migrate_logistics_statuses(apps, schema_editor):
    Courier = apps.get_model("crm", "Courier")
    Delivery = apps.get_model("crm", "Delivery")
    Route = apps.get_model("crm", "Route")
    RouteStop = apps.get_model("crm", "RouteStop")

    courier_map = {
        "free": "Свободен",
        "busy": "Занят",
        "on_route": "В рейсе",
        "Свободен": "Свободен",
        "Занят": "Занят",
        "В рейсе": "В рейсе",
    }
    for old, new in courier_map.items():
        Courier.objects.filter(status=old).update(status=new)

    delivery_map = {
        "unassigned": "Не назначено",
        "planned": "Запланировано",
        "on_route": "В пути",
        "delivered": "Доставлено",
        "cancelled": "Отменено",
        "Не назначено": "Не назначено",
        "Запланировано": "Запланировано",
        "В пути": "В пути",
        "Доставлено": "Доставлено",
        "Отменено": "Отменено",
    }
    for old, new in delivery_map.items():
        Delivery.objects.filter(status=old).update(status=new)

    route_map = {
        "draft": "Черновик",
        "planned": "Запланирован",
        "in_progress": "Выполняется",
        "done": "Завершён",
        "Черновик": "Черновик",
        "Запланирован": "Запланирован",
        "Опубликован": "Опубликован",
        "Выполняется": "Выполняется",
        "Завершён": "Завершён",
    }
    for old, new in route_map.items():
        Route.objects.filter(status=old).update(status=new)

    stop_map = {
        "planned": "Запланирована",
        "in_progress": "В пути",
        "done": "Доставлено",
        "Черновик": "Черновик",
        "Подтверждена": "Подтверждена",
        "Запланирована": "Запланирована",
        "В пути": "В пути",
        "Доставлено": "Доставлено",
        "Не доставлено": "Не доставлено",
        "Перенесено": "Перенесено",
        "Отменено": "Отменено",
    }
    for old, new in stop_map.items():
        RouteStop.objects.filter(status=old).update(status=new)

    for delivery in Delivery.objects.filter(delivery_date__isnull=True, planned_at__isnull=False):
        delivery.delivery_date = delivery.planned_at.date()
        delivery.save(update_fields=["delivery_date"])




class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_courier_current_latitude_courier_current_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата доставки'),
        ),
        migrations.AddField(
            model_name='route',
            name='max_duration_minutes',
            field=models.PositiveSmallIntegerField(default=720, verbose_name='Макс. длительность (мин)'),
        ),
        migrations.AddField(
            model_name='route',
            name='soft_limit_stops',
            field=models.PositiveSmallIntegerField(default=30, verbose_name='Мягкий лимит точек'),
        ),
        migrations.AddField(
            model_name='route',
            name='strict_mode',
            field=models.BooleanField(default=False, verbose_name='Строгий режим лимита точек'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата доставки'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='failure_reason',
            field=models.TextField(blank=True, verbose_name='Причина недоставки'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='proof_of_delivery',
            field=models.FileField(blank=True, null=True, upload_to='delivery_proofs/', verbose_name='Документ доставки'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='proof_uploaded_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время загрузки документа'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='proof_uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uploaded_delivery_proofs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='routestop',
            name='service_time_minutes',
            field=models.PositiveSmallIntegerField(default=15, verbose_name='Время обслуживания (мин)'),
        ),
        migrations.RunPython(migrate_logistics_statuses, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='courier',
            name='status',
            field=models.CharField(choices=[('Свободен', 'Свободен'), ('Занят', 'Занят'), ('В рейсе', 'В рейсе')], default='Свободен', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.CharField(choices=[('Не назначено', 'Не назначено'), ('Запланировано', 'Запланировано'), ('В пути', 'В пути'), ('Доставлено', 'Доставлено'), ('Отменено', 'Отменено')], default='Не назначено', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='route',
            name='status',
            field=models.CharField(choices=[('Черновик', 'Черновик'), ('Запланирован', 'Запланирован'), ('Опубликован', 'Опубликован'), ('Выполняется', 'Выполняется'), ('Завершён', 'Завершён')], default='Черновик', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='routestop',
            name='status',
            field=models.CharField(choices=[('Черновик', 'Черновик'), ('Подтверждена', 'Подтверждена'), ('Запланирована', 'Запланирована'), ('В пути', 'В пути'), ('Доставлено', 'Доставлено'), ('Не доставлено', 'Не доставлено'), ('Перенесено', 'Перенесено'), ('Отменено', 'Отменено')], default='Черновик', max_length=20, verbose_name='Статус'),
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_role', models.CharField(blank=True, max_length=64, verbose_name='Роль')),
                ('object_type', models.CharField(max_length=64, verbose_name='Тип объекта')),
                ('object_id', models.PositiveIntegerField(verbose_name='ID объекта')),
                ('field_name', models.CharField(blank=True, max_length=64, verbose_name='Поле')),
                ('old_value', models.TextField(blank=True, verbose_name='Старое значение')),
                ('new_value', models.TextField(blank=True, verbose_name='Новое значение')),
                ('reason', models.TextField(blank=True, verbose_name='Причина')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время')),
                ('actor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audit_actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Аудит',
                'verbose_name_plural': 'Аудит',
            },
        ),
    ]
```

57. crm/migrations/0012_routestop_proof_review_comment_and_more.py
```python
# Generated by Django 6.0.1 on 2026-02-12 23:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_delivery_delivery_date_route_max_duration_minutes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='routestop',
            name='proof_review_comment',
            field=models.TextField(blank=True, verbose_name='Комментарий проверки'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='proof_review_status',
            field=models.CharField(choices=[('Ожидает проверки', 'Ожидает проверки'), ('Подтверждено', 'Подтверждено'), ('Отклонено', 'Отклонено')], default='Ожидает проверки', max_length=32, verbose_name='Статус проверки документа'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='proof_reviewed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время проверки'),
        ),
        migrations.AddField(
            model_name='routestop',
            name='proof_reviewed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_delivery_proofs', to=settings.AUTH_USER_MODEL),
        ),
    ]
```

58. crm/migrations/0013_equipment_client_daily_max_weight_kg_and_more.py
```python
# Generated by Django 6.0.1 on 2026-02-13 08:26

import django.db.models.deletion
from django.db import migrations, models


def migrate_order_statuses(apps, schema_editor):
    Order = apps.get_model("crm", "Order")
    status_map = {
        "draft": "Черновик",
        "confirmed": "На проверке",
        "in_progress": "В производстве",
        "shipped": "Отгружен",
        "delivered": "Отгружен",
        "cancelled": "Отменен",
        "Черновик": "Черновик",
        "На проверке": "На проверке",
        "Подтвержден производством": "Подтвержден производством",
        "В производстве": "В производстве",
        "Готов к отгрузке": "Готов к отгрузке",
        "Отгружен": "Отгружен",
        "Отменен": "Отменен",
    }
    for old, new in status_map.items():
        Order.objects.filter(status=old).update(status=new)


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_routestop_proof_review_comment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Оборудование')),
                ('capacity_per_hour', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Производительность/час')),
                ('available_hours', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Доступные часы')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудование',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='daily_max_weight_kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Макс. вес в день (кг)'),
        ),
        migrations.AddField(
            model_name='client',
            name='daily_min_qty',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Мин. объём заказа'),
        ),
        migrations.AddField(
            model_name='client',
            name='guaranteed_volume_kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Гарантированный объём (кг)'),
        ),
        migrations.AddField(
            model_name='dish',
            name='batch_multiple_qty',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Кратность партии'),
        ),
        migrations.AddField(
            model_name='dish',
            name='min_batch_qty',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Мин. партия'),
        ),
        migrations.AddField(
            model_name='dish',
            name='unit_weight_kg',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Вес единицы (кг)'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('Регулярная', 'Регулярная'), ('Разовая', 'Разовая'), ('Срочная', 'Срочная')], default='Разовая', max_length=32, verbose_name='Тип доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='production_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата производства'),
        ),
        migrations.AddField(
            model_name='order',
            name='production_shift',
            field=models.CharField(blank=True, max_length=32, verbose_name='Смена'),
        ),
        migrations.AddField(
            model_name='order',
            name='production_window_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Окно производства (до)'),
        ),
        migrations.AddField(
            model_name='order',
            name='production_window_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Окно производства (с)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Черновик', 'Черновик'), ('На проверке', 'На проверке'), ('Подтвержден производством', 'Подтвержден производством'), ('В производстве', 'В производстве'), ('Готов к отгрузке', 'Готов к отгрузке'), ('Отгружен', 'Отгружен'), ('Отменен', 'Отменен')], default='Черновик', max_length=64, verbose_name='Статус'),
        ),
        migrations.RunPython(migrate_order_statuses, migrations.RunPython.noop),
        migrations.CreateModel(
            name='EquipmentReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_date', models.DateField(verbose_name='Дата производства')),
                ('hours', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Часы')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='crm.equipment')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_reservations', to='crm.order')),
            ],
            options={
                'verbose_name': 'Резерв оборудования',
                'verbose_name_plural': 'Резервы оборудования',
            },
        ),
        migrations.CreateModel(
            name='IngredientReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_date', models.DateField(verbose_name='Дата производства')),
                ('quantity', models.DecimalField(decimal_places=3, default=0, max_digits=12, verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='crm.ingredient')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_reservations', to='crm.order')),
            ],
            options={
                'verbose_name': 'Резерв ингредиента',
                'verbose_name_plural': 'Резервы ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='IngredientStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=3, default=0, max_digits=12, verbose_name='Остаток')),
                ('ingredient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='crm.ingredient')),
            ],
            options={
                'verbose_name': 'Остаток ингредиента',
                'verbose_name_plural': 'Остатки ингредиентов',
            },
        ),
        migrations.CreateModel(
            name='ProductionReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_date', models.DateField(verbose_name='Дата производства')),
                ('weight_kg', models.DecimalField(decimal_places=3, default=0, max_digits=12, verbose_name='Вес (кг)')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_reservations', to='crm.order')),
            ],
            options={
                'verbose_name': 'Резерв мощности производства',
                'verbose_name_plural': 'Резервы мощности производства',
            },
        ),
        migrations.CreateModel(
            name='ClientAllowedTechCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowed_tech_cards', to='crm.client')),
                ('tech_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowed_for_clients', to='crm.techcard')),
            ],
            options={
                'verbose_name': 'Разрешённая техкарта клиента',
                'verbose_name_plural': 'Разрешённые техкарты клиентов',
                'unique_together': {('client', 'tech_card')},
            },
        ),
        migrations.CreateModel(
            name='DishEquipmentRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Минут на единицу')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_requirements', to='crm.dish')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish_requirements', to='crm.equipment')),
            ],
            options={
                'verbose_name': 'Требование оборудования',
                'verbose_name_plural': 'Требования оборудования',
                'unique_together': {('dish', 'equipment')},
            },
        ),
    ]
```

59. crm/migrations/0014_dish_default_price.py
```python
# Generated by Django 6.0.1 on 2026-02-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_equipment_client_daily_max_weight_kg_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='default_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Базовая цена'),
        ),
    ]
```

60. crm/migrations/0015_dish_daily_capacity.py
```python
# Generated by Django 6.0.1 on 2026-02-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0014_dish_default_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='daily_capacity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True, verbose_name='Суточная мощность'),
        ),
    ]
```

61. crm/migrations/0015_dish_uom_fields.py
```python
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
```

62. crm/migrations/0016_merge_0015_dish_daily_capacity_0015_dish_uom_fields.py
```python
# Generated by Django 6.0.1 on 2026-02-16 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0015_dish_daily_capacity'),
        ('crm', '0015_dish_uom_fields'),
    ]

    operations = [
    ]
```

63. crm/migrations/__init__.py
```python
```

64. crm/models.py
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

65. dashboard/__init__.py
```python
```

66. dashboard/admin.py
```python
from django.contrib import admin

# Register your models here.
```

67. dashboard/apps.py
```python
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'
```

68. dashboard/migrations/__init__.py
```python
```

69. dashboard/models.py
```python
from django.db import models

# Create your models here.
```

70. dashboard/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

71. dashboard/urls.py
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

72. dashboard/views.py
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

73. factory_crm/__init__.py
```python
# Factory CRM project package
```

74. factory_crm/asgi.py
```python
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factory_crm.settings')
application = get_asgi_application()
```

75. factory_crm/settings.py
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

76. factory_crm/urls.py
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

77. factory_crm/views.py
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

78. factory_crm/wsgi.py
```python
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factory_crm.settings')
application = get_wsgi_application()
```

79. locustfile.py
```python
import os
import random
from faker import Faker
from locust import HttpUser, task, constant_throughput, SequentialTaskSet, TaskSet

fake = Faker("ru_RU")

class UserFlow(SequentialTaskSet):
    @task
    def open_admin_dashboard(self):
        self.client.get("/dashboard/admin/")

    @task
    def open_admin_panel(self):
        self.client.get("/admin-panel/")

    @task
    def open_admin_users(self):
        self.client.get("/admin-panel/users/")

    @task
    def open_admin_roles(self):
        self.client.get("/admin-panel/roles/")

    @task
    def open_admin_backups(self):
        self.client.get("/admin-panel/backups/")


class RandomAct(TaskSet):
    def on_start(self):
        self.api_headers = {"Accept": "application/json"}
        self.client_ids = []
        self.created_clients = 0
        self._auth()

    def _auth(self):
        if "Authorization" in self.api_headers:
            return True
        username = os.getenv("LOCUST_USERNAME", "admin_demo")
        password = os.getenv("LOCUST_PASSWORD", "AdminDemo123!")
        resp = self.client.post(
            "/api/token/",
            json={"username": username, "password": password},
            name="/api/token/",
        )
        if resp.status_code != 200:
            return False
        try:
            token = resp.json().get("access")
        except ValueError:
            return False
        if not token:
            return False
        self.api_headers["Authorization"] = f"Bearer {token}"
        return True

    def _fetch_client_ids(self):
        if not self._auth():
            return
        resp = self.client.get("/api/clients/", headers=self.api_headers, name="/api/clients/")
        if resp.status_code != 200:
            return
        try:
            data = resp.json()
        except ValueError:
            return
        ids = [item.get("id") for item in data.get("results", []) if item.get("id")]
        self.client_ids = ids[:5]

    @task(10)
    def get_clients(self):
        if not self._auth():
            return
        self.client.get("/api/clients/", headers=self.api_headers)

    @task(10)
    def get_client_detail(self):
        if not self._auth():
            return
        if not self.client_ids:
            self._fetch_client_ids()
        if not self.client_ids:
            return
        client_id = random.choice(self.client_ids)
        self.client.get(f"/api/clients/{client_id}/", headers=self.api_headers)

    @task(10)
    def get_orders(self):
        if not self._auth():
            return
        self.client.get("/api/orders/", headers=self.api_headers)

    @task(1)
    def create_client(self):
        if not self._auth():
            return
        if self.created_clients >= 1:
            return
        payload = {
            "name": fake.company()[:255],
            "client_type": random.choice(["store", "cafe", "restaurant", "distributor", "other"]),
            "inn": str(fake.random_number(digits=10, fix_len=True)),
            "kpp": str(fake.random_number(digits=9, fix_len=True)),
            "default_delivery_address": fake.street_address()[:255],
            "email": fake.email(),
            "phone": fake.msisdn()[:15],
            "status": random.choice(["prospect", "active", "paused", "lost"]),
        }
        resp = self.client.post("/api/clients/", json=payload, headers=self.api_headers)
        if resp.status_code == 201:
            self.created_clients += 1
            try:
                new_id = resp.json().get("id")
            except ValueError:
                new_id = None
            if new_id:
                self.client_ids.append(new_id)

class WebsiteUser(HttpUser):
    wait_time = constant_throughput(5)
    tasks = [UserFlow, RandomAct]
```

80. logistics/__init__.py
```python
```

81. logistics/admin.py
```python
from django.contrib import admin

# Register your models here.
```

82. logistics/apps.py
```python
from django.apps import AppConfig


class LogisticsConfig(AppConfig):
    name = 'logistics'
```

83. logistics/forms.py
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

84. logistics/migrations/__init__.py
```python
```

85. logistics/models.py
```python
from django.db import models

# Create your models here.
```

86. logistics/tests.py
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

87. logistics/urls.py
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

88. logistics/views.py
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

89. manage.py
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

90. orders/__init__.py
```python
```

91. orders/admin.py
```python
from django.contrib import admin

# Register your models here.
```

92. orders/apps.py
```python
from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'
```

93. orders/forms.py
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

94. orders/migrations/__init__.py
```python
```

95. orders/models.py
```python
from django.db import models

# Create your models here.
```

96. orders/tests.py
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

97. orders/urls.py
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

98. orders/views.py
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

99. portal/__init__.py
```python
# Portal app for custom dashboards and CRUD (no Django admin)
```

100. portal/forms.py
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

101. portal/urls.py
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

102. portal/utils.py
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

103. portal/views.py
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

104. reports/__init__.py
```python
```

105. reports/admin.py
```python
from django.contrib import admin

# Register your models here.
```

106. reports/apps.py
```python
from django.apps import AppConfig


class ReportsConfig(AppConfig):
    name = 'reports'
```

107. reports/forms.py
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

108. reports/migrations/0001_initial.py
```python
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
```

109. reports/migrations/0002_report_validation.py
```python
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
```

110. reports/migrations/__init__.py
```python
```

111. reports/models.py
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

112. reports/tests.py
```python
from django.test import TestCase

# Create your tests here.
```

113. reports/urls.py
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

114. reports/views.py
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

115. requirements.txt
```text
Django==6.0.1
psycopg[binary]==3.3.2
djangorestframework==3.15.2
drf-spectacular==0.27.2
djangorestframework-simplejwt==5.3.1
django-filter==24.3
django-cors-headers==4.4.0
Faker==24.8.0
```

116. static/admin_theme.css
```css
/* Modern dark-blue admin theme for Art Culinary CRM */
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&display=swap');

:root {
  /* базовая палитра: FFFFFF, 0059FF, 041A53, 030923, 000000 */
  --bg: #030923;
  --bg-2: #041a53;
  --panel: #041a53;
  --panel-2: #030923;
  --border: #000000;
  --card: #041a53;
  --card-hover: #0059ff1a;
  --accent: #0059ff;
  --accent-2: #0059ff;
  --success: #0059ff;
  --warning: #0059ff;
  --danger: #0059ff;
  --text: #ffffff;
  --muted: #9fb1d9;
  --shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
  --radius: 14px;
  --field-bg: #f8fbff;
  --field-border: #d5ddf5;
  --field-text: #0b1021;
}

[data-theme="light"] {
  --bg: #ffffff;
  --bg-2: #ffffff;
  --panel: #ffffff;
  --panel-2: #ffffff;
  --border: #e5e7eb;
  --card: #ffffff;
  --card-hover: #f8fafc;
  --accent: #0059ff;
  --accent-2: #0059ff;
  --success: #0059ff;
  --warning: #0059ff;
  --danger: #0059ff;
  --text: #000000;
  --muted: #041a53;
  --shadow: 0 10px 26px rgba(0, 0, 0, 0.08);
  --field-bg: #f8fbff;
  --field-border: #d5ddf5;
  --field-text: #0b1021;
}

body, #container {
  position: relative;
  background:
    radial-gradient(circle at 20% 20%, rgba(0, 89, 255, 0.22), transparent 35%),
    radial-gradient(circle at 80% 0%, rgba(4, 26, 83, 0.25), transparent 35%),
    linear-gradient(135deg, #030923 0%, #041a53 45%, #030923 100%);
  color: var(--text);
  font-family: 'Manrope', 'Inter', 'Segoe UI', sans-serif;
}

[data-theme="light"] body,
[data-theme="light"] #container {
  background:
    linear-gradient(180deg, #ffffff 0%, #ffffff 100%),
    radial-gradient(circle at 85% 15%, rgba(0, 89, 255, 0.10), transparent 32%),
    radial-gradient(circle at 12% 85%, rgba(4, 26, 83, 0.08), transparent 28%);
}
#header {
  background: linear-gradient(90deg, var(--bg-2), #000000);
  border-bottom: 1px solid var(--border);
  box-shadow: 0 6px 18px rgba(0,0,0,0.35);
}

[data-theme=\"light\"] #header {
  background: #ffffff;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.06);
}

#branding h1, #branding h1 a {
  color: var(--text);
  font-weight: 700;
  letter-spacing: 0.4px;
}

#user-tools, #user-tools a { color: var(--muted); }
#user-tools, #user-tools a { color: var(--text) !important; }

a:link, a:visited { color: var(--accent); }
a:hover { color: var(--accent-2); }

.breadcrumbs,
.breadcrumbs a { color: var(--text); }

/* Навигация/сайдбар — только палитра синих и серых */
#nav-sidebar {
  background: #ffffff;
  border-right: 1px solid #e5e7eb;
}

#nav-sidebar a,
#nav-sidebar caption,
#nav-sidebar th {
  color: #041a53 !important;
}

#nav-sidebar .current-model,
#nav-sidebar .current-app {
  background: rgba(0, 89, 255, 0.08);
  border-left: 3px solid #0059ff;
}

.module, .dashboard .module table {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}

.module h2, .module caption {
  background: transparent;
  border: none;
  color: var(--text);
  font-weight: 700;
}

.button, .button.default, input[type=submit], input[type=submit].default {
  background: linear-gradient(120deg, var(--accent), var(--accent-2));
  border: none;
  color: #ffffff;
  font-weight: 700;
  border-radius: 10px;
  padding: 9px 16px;
  box-shadow: 0 10px 24px rgba(0, 89, 255, 0.35);
  transition: transform 120ms ease, box-shadow 120ms ease;
}

[data-theme="light"] .button,
[data-theme="light"] .button.default,
[data-theme="light"] input[type=submit],
[data-theme="light"] input[type=submit].default {
  color: #0b1021;
  box-shadow: 0 10px 24px rgba(0, 89, 255, 0.2);
}

.button:hover, .button.default:hover,
input[type=submit]:hover, input[type=submit].default:hover {
  transform: translateY(-1px);
  box-shadow: 0 12px 28px rgba(0, 194, 255, 0.35);
}

table#result_list {
  background: transparent;
}

table#result_list thead th {
  background: var(--panel-2);
  color: var(--text);
  border-color: var(--border);
}

[data-theme="dark"] table#result_list th,
[data-theme="dark"] table#result_list td,
[data-theme="dark"] table#result_list a {
  color: #ffffff !important;
}

[data-theme="light"] table#result_list thead th {
  background: #f1f5ff;
  color: #041a53;
  border-color: #e5e7eb;
}

table#result_list tbody tr:nth-child(even) { background: rgba(255,255,255,0.012); }
table#result_list tbody tr:hover { background: rgba(0, 89, 255, 0.08); }

fieldset, .aligned, .inline-group {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}

[data-theme="light"] fieldset,
[data-theme="light"] .aligned,
[data-theme="light"] .inline-group {
  background: #ffffff;
  border: 1px solid #e5e7eb;
}

input, select, textarea {
  background: var(--field-bg);
  border: 1px solid var(--field-border);
  color: var(--field-text);
  border-radius: 10px;
  box-shadow: none;
}

[data-theme="light"] input,
[data-theme="light"] select,
[data-theme="light"] textarea {
  background: var(--field-bg);
  border: 1px solid var(--field-border);
  color: var(--field-text);
}

/* Усиленные стили, чтобы в светлой теме не появлялся тёмный фон/градиент */
select,
[data-theme="light"] select {
  background-color: var(--field-bg) !important;
  border-color: var(--field-border) !important;
  color: var(--field-text) !important;
  box-shadow: none !important;
}

textarea,
[data-theme="light"] textarea {
  background-color: var(--field-bg) !important;
  border-color: var(--field-border) !important;
  color: var(--field-text) !important;
  box-shadow: none !important;
}

.related-widget-wrapper select,
[data-theme="light"] .related-widget-wrapper select {
  background-color: var(--field-bg) !important;
  border-color: var(--field-border) !important;
  color: var(--field-text) !important;
}

.vTextField, .vLargeTextField,
[data-theme="light"] .vTextField, [data-theme="light"] .vLargeTextField {
  background-color: var(--field-bg) !important;
  border-color: var(--field-border) !important;
  color: var(--field-text) !important;
}

input:focus, select:focus, textarea:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 2px rgba(0, 89, 255, 0.35);
}

.object-tools a {
  background: linear-gradient(120deg, var(--accent), var(--accent-2));
  color: var(--text);
  border: none;
  border-radius: 10px;
}

.dashboard .module {
  padding: 0.4rem 0.8rem 0.8rem;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  width: 100%;
  align-items: start;
}

.dash-card {
  background: linear-gradient(160deg, rgba(0, 89, 255, 0.18), rgba(3, 9, 35, 0.7)),
              var(--panel);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: var(--radius);
  padding: 14px 16px;
  box-shadow: var(--shadow);
}

[data-theme="light"] .dash-card {
  background: var(--panel);
  border: 1px solid rgba(0,0,0,0.04);
}

.dash-card__header h2 {
  margin: 0 0 8px;
  font-size: 16px;
  letter-spacing: 0.3px;
}

.dash-card__body {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.dash-entry {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

[data-theme="light"] .dash-entry {
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.dash-entry:last-child { border-bottom: none; }

.dash-entry__title a {
  font-weight: 600;
  color: var(--text);
}

.dash-entry__actions {
  display: flex;
  gap: 8px;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  border-radius: 999px;
  padding: 6px 10px;
  font-weight: 600;
  font-size: 12px;
  text-decoration: none;
  color: #ffffff;
}

.pill--primary {
  background: linear-gradient(120deg, var(--accent), var(--accent-2));
  box-shadow: 0 8px 18px rgba(0, 89, 255, 0.3);
}

.pill--ghost {
  background: rgba(255,255,255,0.08);
  color: var(--text);
  border: 1px solid rgba(255,255,255,0.1);
}

[data-theme="light"] .pill,
[data-theme="light"] .pill a {
  color: #0b1021 !important;
}

[data-theme="light"] .pill--ghost {
  background: rgba(0,0,0,0.06);
  border-color: rgba(0,0,0,0.08);
  color: #0b1021 !important;
}

/* Текстовые элементы явно следуют теме */
h1, h2, h3, h4, h5, h6,
label, legend, th, td,
p, li, a {
  color: var(--text);
}

[data-theme="light"] h1, [data-theme="light"] h2, [data-theme="light"] h3,
[data-theme="light"] h4, [data-theme="light"] h5, [data-theme="light"] h6,
[data-theme="light"] label, [data-theme="light"] legend,
[data-theme="light"] th, [data-theme="light"] td,
[data-theme="light"] p, [data-theme="light"] li, [data-theme="light"] a {
  color: var(--text);
}

/* В тёмной теме весь текст — белый принудительно */
[data-theme="dark"] *, [data-theme="dark"] *::placeholder {
  color: #ffffff !important;
  border-color: inherit;
}

/* В светлой теме возвращаем placeholder к тёмному */
[data-theme="light"] *::placeholder {
  color: #4b5563;
}

/* Скрыть стандартную кнопку смены темы Django (оставляем свою) */
button[aria-label="Toggle theme"]:not(#theme-toggle),
.theme-toggle:not(#theme-toggle) {
  display: none !important;
}

.grp-object-tools a, .grp-add-handler, .grp-remove-handler {
  background: var(--accent);
  color: #fff;
}

.errornote, .errorlist li { background: rgba(244, 63, 94, 0.15); border-color: var(--danger); color: #ffcbd7; }
.success { background: rgba(22, 196, 127, 0.18); color: #b6f3d8; }
.warning { background: rgba(251, 191, 36, 0.16); color: #fde8b2; }

/* Ошибки и валидация в синей гамме */
.errornote, .errorlist li {
  background: rgba(0, 89, 255, 0.12);
  border-color: #0059ff;
  color: #041a53;
}

.errorlist li a { color: #0059ff; }

.form-row.errors,
.errors {
  background: rgba(0, 89, 255, 0.06);
  border-color: #0059ff !important;
}

.form-row.errors input,
.form-row.errors select,
.form-row.errors textarea,
.errors input,
.errors select,
.errors textarea {
  background: #f0f6ff !important;
  border-color: #0059ff !important;
  color: #0b1021 !important;
  box-shadow: none !important;
}

.dashboard-full {
  width: 100%;
  max-width: none;
  padding-right: 0;
}

#content {
  margin: 0 auto;
  width: 100%;
  padding: 24px;
  max-width: none;
}

.theme-toggle {
  margin-left: 12px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.14);
  color: var(--text);
  border-radius: 10px;
  padding: 6px 10px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-weight: 600;
  transition: background 120ms ease, transform 120ms ease;
}

.theme-toggle:hover { background: rgba(255,255,255,0.14); transform: translateY(-1px); }

[data-theme=\"light\"] .theme-toggle {
  background: rgba(0,0,0,0.05);
  border-color: rgba(0,0,0,0.08);
}

.theme-toggle__icon {
  font-size: 16px;
  letter-spacing: 4px;
}

/* Quickbar */
.admin-quickbar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 6px 12px;
}

.nav-filter-input {
  background: var(--field-bg);
  border: 1px solid var(--field-border);
  color: var(--field-text);
  border-radius: 10px;
  padding: 6px 10px;
  min-width: 240px;
}

.nav-filter-wrap {
  padding: 10px 12px 6px;
  border-bottom: 1px solid var(--border);
}

/* Login page */
.login-hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background: #f7f8fa;
}

.login-card {
  width: min(420px, 90vw);
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  padding: 28px 26px;
  box-shadow: 0 14px 36px rgba(15, 23, 42, 0.12);
  position: relative;
  z-index: 1;
}

.login-card h1 {
  margin: 0 0 6px;
}

.login-subtitle {
  margin: 0 0 16px;
  color: var(--muted);
  font-size: 14px;
}

.login-card .form-row {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 12px;
}

.login-card label {
  font-weight: 600;
  color: #0f172a;
}

.login-card input[type=\"text\"], .login-card input[type=\"password\"] {
  background: #ffffff;
  border: 1px solid #d5d9e0;
  color: #0f172a;
  border-radius: 8px;
  padding: 10px 12px;
}

.login-card input[type=\"text\"]:focus,
.login-card input[type=\"password\"]:focus {
  border-color: #1e5cf5;
  box-shadow: 0 0 0 3px rgba(30, 92, 245, 0.18);
}

.login-card .form-actions {
  margin-top: 12px;
  display: flex;
  justify-content: stretch;
  flex-direction: column;
  gap: 10px;
}

.remember-row {
  flex-direction: row !important;
  align-items: center;
  gap: 8px;
}

.button-wide {
  width: 100%;
  text-align: center;
}

.login-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.login-logo {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: linear-gradient(135deg, #1e5cf5, #113a8f);
  color: #ffffff;
  font-weight: 800;
  display: grid;
  place-items: center;
  box-shadow: 0 10px 24px rgba(30, 92, 245, 0.35);
}

.login-blob {
  position: absolute;
  inset: -20% -10% auto auto;
  width: 320px;
  height: 320px;
  background: radial-gradient(circle at 30% 30%, rgba(0,89,255,0.28), transparent 40%),
              radial-gradient(circle at 70% 60%, rgba(0,89,255,0.18), transparent 35%);
  filter: blur(36px);
  opacity: 0.8;
}
```

117. static/css/app.css
```css
:root {
  --bg: #f6f7fb;
  --surface: #ffffff;
  --surface-2: #f8fafc;
  --text: #0f172a;
  --text-muted: #6b7280;
  --border: #e5e7eb;
  --primary: #2563eb;
  --table-header: #f1f5ff;
  --table-row: #ffffff;
  --table-row-hover: #edf2ff;

  --bg-2: var(--surface-2);
  --card: var(--surface);
  --muted: var(--text-muted);
  --primary-2: #1d4ed8;
  --chip: #eef2ff;
  --shadow: 0 16px 40px rgba(15, 23, 42, 0.08);
  --radius: 14px;
}

[data-theme="dark"] {
  --bg: #0b1021;
  --surface: #111827;
  --surface-2: #0f172a;
  --text: #eaeaea;
  --text-secondary: #c0c0c0;
  --text-muted: #9a9a9a;
  --heading-text: #f5f5f5;
  --card-text: #eaeaea;
  --border: #1f2937;
  --primary: #3b82f6;
  --table-header: #0f172a;
  --table-row: #111827;
  --table-row-hover: rgba(59, 130, 246, 0.14);

  --bg-2: var(--surface-2);
  --card: var(--surface);
  --muted: var(--text-muted);
  --primary-2: #2563eb;
  --chip: #0f172a;
  --shadow: 0 18px 48px rgba(0, 0, 0, 0.35);
}

* { box-sizing: border-box; }
body {
  font-family: "Inter", "Manrope", "Segoe UI", sans-serif;
  background: radial-gradient(1200px 600px at 10% -10%, rgba(37, 99, 235, 0.12), transparent 60%),
              radial-gradient(800px 400px at 80% 0%, rgba(37, 99, 235, 0.08), transparent 55%),
              var(--bg);
  color: var(--text);
}

a { color: var(--primary); }
a:hover { color: var(--primary-2); }

[data-theme="dark"] body {
  background: radial-gradient(1200px 600px at 10% -10%, rgba(59, 130, 246, 0.18), transparent 60%),
              radial-gradient(800px 400px at 80% 0%, rgba(59, 130, 246, 0.12), transparent 55%),
              var(--bg);
}

[data-theme="dark"] {
  color: var(--text) !important;
}

[data-theme="dark"] p,
[data-theme="dark"] span,
[data-theme="dark"] small,
[data-theme="dark"] th,
[data-theme="dark"] td,
[data-theme="dark"] .card,
[data-theme="dark"] .card * ,
[data-theme="dark"] .table,
[data-theme="dark"] .table * ,
[data-theme="dark"] .btn,
[data-theme="dark"] .btn * ,
[data-theme="dark"] .dropdown,
[data-theme="dark"] .dropdown * ,
[data-theme="dark"] .nav,
[data-theme="dark"] .nav * {
  color: var(--text) !important;
}

[data-theme="dark"] .text-dark,
[data-theme="dark"] .text-body,
[data-theme="dark"] .text-secondary,
[data-theme="dark"] .text-muted,
[data-theme="dark"] .text-body-secondary,
[data-theme="dark"] .text-body-tertiary {
  color: var(--text-muted) !important;
}

[data-theme="dark"] h1,
[data-theme="dark"] h2,
[data-theme="dark"] h3,
[data-theme="dark"] h4,
[data-theme="dark"] h5,
[data-theme="dark"] h6,
[data-theme="dark"] .card h1,
[data-theme="dark"] .card h2,
[data-theme="dark"] .card h3,
[data-theme="dark"] .card h4,
[data-theme="dark"] .card h5,
[data-theme="dark"] .card h6 {
  color: var(--heading-text);
}

[data-theme="dark"] .text-muted,
[data-theme="dark"] .text-secondary,
[data-theme="dark"] .text-body-secondary,
[data-theme="dark"] .form-text,
[data-theme="dark"] small,
[data-theme="dark"] .small,
[data-theme="dark"] .kpi-label,
[data-theme="dark"] .breadcrumbs,
[data-theme="dark"] .system-name,
[data-theme="dark"] .link-muted,
[data-theme="dark"] .table caption {
  color: var(--text-muted);
}

[data-theme="dark"] .table thead th {
  color: var(--text-secondary);
}

[data-theme="dark"] .card {
  color: var(--card-text);
}

[data-theme="dark"] .btn-outline-secondary {
  color: var(--text);
}

[data-theme="dark"] .btn-outline-secondary:hover,
[data-theme="dark"] .btn-outline-secondary:focus {
  color: var(--text);
  background: rgba(255, 255, 255, 0.06);
  border-color: var(--border);
}

.app-shell {
  display: grid;
  grid-template-columns: 250px 1fr;
  min-height: 100vh;
}

.sidebar {
  background: var(--bg-2);
  border-right: 1px solid var(--border);
  padding: 28px 18px;
  position: sticky;
  top: 0;
  height: 100vh;
}

.sidebar .logo {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  margin-bottom: 22px;
}

.menu-title {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin: 18px 0 8px;
}

.menu a {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 10px;
  color: var(--text);
  text-decoration: none;
}

.menu a.active, .menu a:hover {
  background: rgba(37, 99, 235, 0.12);
  color: var(--primary);
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  border-bottom: 1px solid var(--border);
  background: var(--bg-2);
}

.topbar-left {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.system-name {
  font-size: 12px;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.page-title {
  font-size: 18px;
  font-weight: 600;
}

.content {
  min-height: calc(100vh - 64px);
}

.breadcrumbs {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 16px;
}

.breadcrumbs a {
  color: var(--muted);
  text-decoration: none;
}

.breadcrumbs a:hover {
  color: var(--primary);
}

.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: 16px;
}

.kpi-card {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.kpi-value { font-size: 26px; font-weight: 700; }
.kpi-label { color: var(--muted); font-size: 13px; }

.table {
  color: var(--text);
  --bs-table-bg: var(--table-row);
  --bs-table-striped-bg: var(--table-row);
  --bs-table-color: var(--text);
  --bs-table-border-color: var(--border);
}

.table caption {
  color: var(--text-muted);
}

.notify-stack {
  position: fixed;
  top: 18px;
  right: 18px;
  z-index: 1200;
  display: grid;
  gap: 10px;
  width: min(92vw, 390px);
}

.notify-card {
  position: relative;
  overflow: hidden;
  border-radius: 14px;
  border: 1px solid rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(8px);
  box-shadow: 0 12px 36px rgba(15, 23, 42, 0.22);
  display: grid;
  grid-template-columns: 34px 1fr 26px;
  gap: 10px;
  align-items: start;
  padding: 12px 12px 14px 12px;
  transform: translateX(22px);
  opacity: 0;
  transition: transform 0.26s ease, opacity 0.26s ease;
}

.notify-card[data-level="success"] {
  background: linear-gradient(135deg, rgba(22, 163, 74, 0.95), rgba(5, 150, 105, 0.86));
  color: #f0fff7;
}

.notify-card[data-level="danger"] {
  background: linear-gradient(135deg, rgba(220, 38, 38, 0.95), rgba(190, 24, 93, 0.9));
  color: #fff3f3;
}

.notify-card[data-level="warning"] {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.98), rgba(217, 119, 6, 0.94));
  color: #fff8ed;
}

.notify-card[data-level="info"] {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.95), rgba(59, 130, 246, 0.88));
  color: #eff6ff;
}

.notify-card.is-visible {
  transform: translateX(0);
  opacity: 1;
}

.notify-card.is-hiding {
  transform: translateX(24px);
  opacity: 0;
}

.notify-icon {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.22);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  line-height: 1;
}

.notify-title {
  font-size: 13px;
  letter-spacing: 0.01em;
  text-transform: uppercase;
  opacity: 0.92;
}

.notify-text {
  margin-top: 2px;
  font-size: 14px;
  line-height: 1.35;
  font-weight: 600;
}

.notify-close {
  border: 0;
  background: transparent;
  color: inherit;
  width: 24px;
  height: 24px;
  border-radius: 8px;
  font-size: 18px;
  line-height: 1;
  opacity: 0.9;
  cursor: pointer;
}

.notify-close:hover {
  background: rgba(255, 255, 255, 0.18);
  opacity: 1;
}

.notify-progress {
  position: absolute;
  left: 0;
  bottom: 0;
  height: 3px;
  width: 100%;
  background: rgba(255, 255, 255, 0.35);
  transform-origin: left center;
  animation: notify-progress 5.2s linear forwards;
}

@keyframes notify-progress {
  from { transform: scaleX(1); }
  to { transform: scaleX(0); }
}

@media (max-width: 640px) {
  .notify-stack {
    top: 12px;
    right: 12px;
    left: 12px;
    width: auto;
  }
}

.table > :not(caption) > * > * {
  background-color: var(--table-row);
  color: var(--text);
  border-color: var(--border);
}

.table thead th {
  background: var(--table-header);
  color: var(--text-muted);
  font-weight: 600;
  border-bottom: 1px solid var(--border);
}

.table tbody tr {
  background: var(--table-row);
}

.table tbody tr:hover {
  background: var(--table-row-hover);
}

.btn-primary {
  background: var(--primary);
  border-color: var(--primary);
}
.btn-primary:hover { background: var(--primary-2); border-color: var(--primary-2); }
.btn-outline-secondary { border-color: var(--border); color: var(--text); }

.form-control, .form-select {
  border-radius: 10px;
  border: 1px solid var(--border);
  background: var(--bg-2);
  color: var(--text);
}

.form-control:focus, .form-select:focus {
  border-color: var(--primary);
  box-shadow: 0 0 0 0.2rem rgba(37, 99, 235, 0.12);
}

.theme-toggle {
  border: 1px solid var(--border);
  background: var(--bg-2);
  border-radius: 10px;
  padding: 6px 10px;
  cursor: pointer;
  display: inline-flex;
  gap: 8px;
  align-items: center;
}

.status-pill {
  display: inline-flex;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
  background: var(--chip);
  color: var(--text);
}

.status-pill.primary { color: var(--primary); }
.status-pill.success { color: #16a34a; }
.status-pill.warn { color: #d97706; }
.status-pill.danger { color: #dc2626; }

.badge-soft {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 12px;
  font-weight: 600;
  background: var(--chip);
  color: var(--text);
}

.badge-soft.success { color: #16a34a; }
.badge-soft.primary { color: var(--primary); }
.badge-soft.warn { color: #d97706; }
.badge-soft.danger { color: #dc2626; }

.chart {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 12px;
  margin-top: 16px;
}

.chart-bar {
  background: var(--bg-2);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 12px;
}

.chart-bar__value {
  height: 120px;
  display: flex;
  align-items: flex-end;
}

.chart-bar__value span {
  display: block;
  width: 100%;
  border-radius: 10px;
  background: linear-gradient(180deg, var(--primary), var(--primary-2));
}

.auth-body {
  min-height: 100vh;
  background: radial-gradient(900px 400px at 10% -10%, rgba(37, 99, 235, 0.15), transparent 60%),
              var(--bg);
}

[data-theme="dark"] .auth-body {
  background: radial-gradient(900px 400px at 10% -10%, rgba(59, 130, 246, 0.22), transparent 60%),
              var(--bg);
}

.auth-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 28px;
}

.auth-logo { font-weight: 700; }

.auth-shell {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: calc(100vh - 72px);
  padding: 24px;
}

.auth-card {
  width: 100%;
  max-width: 420px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px;
  box-shadow: var(--shadow);
  padding: 28px;
}

.auth-title { font-size: 22px; font-weight: 700; margin-bottom: 6px; }
.auth-subtitle { color: var(--muted); margin-bottom: 20px; }
.link-muted { color: var(--muted); text-decoration: none; }
.link-muted:hover { color: var(--primary); }

.list-group-item {
  background: var(--card);
  border-color: var(--border);
  color: var(--text);
}

.nav-tabs .nav-link {
  color: var(--muted);
  border-color: transparent;
}
.nav-tabs .nav-link.active {
  color: var(--text);
  background: var(--bg-2);
  border-color: var(--border);
}

.alert-error {
  color: #7f1d1d;
  background-color: #fee2e2;
  border-color: #fecaca;
}

[data-theme="dark"] .alert-error {
  color: #fecaca;
  background-color: rgba(127, 29, 29, 0.25);
  border-color: rgba(127, 29, 29, 0.4);
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

.filters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
}

.empty-state {
  text-align: center;
  padding: 40px;
  color: var(--muted);
}

@media (max-width: 992px) {
  .app-shell { grid-template-columns: 1fr; }
  .sidebar { position: relative; height: auto; }
}
```

118. static/login_root.css
```css
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: 'Inter', 'Segoe UI', sans-serif;
  background: #f4f6f9;
  color: #0f172a;
}
.root-login {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 24px;
}
.login-card {
  width: min(420px, 90vw);
  background: #ffffff;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  box-shadow: 0 16px 40px rgba(15,23,42,0.12);
  padding: 28px 26px;
  display: grid;
  gap: 12px;
}
.logo {
  width: 48px; height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, #1e5cf5, #113a8f);
  color: #fff;
  display: grid; place-items: center;
  font-weight: 800;
  box-shadow: 0 10px 24px rgba(30,92,245,0.25);
}
h1 { margin: 0; font-size: 22px; }
.subtitle { margin: 0; color: #6b7280; font-size: 14px; }
form { display: grid; gap: 10px; }
label { font-weight: 600; color: #0f172a; }
input {
  padding: 10px 12px;
  border: 1px solid #d5d9e0;
  border-radius: 8px;
  background: #fff;
  color: #0f172a;
}
input:focus {
  border-color: #1e5cf5;
  box-shadow: 0 0 0 3px rgba(30, 92, 245, 0.18);
  outline: none;
}
.btn.primary {
  background: linear-gradient(120deg, #1e5cf5, #3b82f6);
  border: none;
  color: #fff;
  padding: 10px 14px;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  box-shadow: 0 10px 24px rgba(30,92,245,0.25);
}
.btn.primary:hover { filter: brightness(1.05); }
.link {
  text-align: center;
  color: #1e5cf5;
  text-decoration: none;
  font-weight: 600;
}
.link:hover { text-decoration: underline; }
```

119. static/manager.css
```css
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: 'Inter', 'Segoe UI', sans-serif;
  background: #f4f6f9;
  color: #0f172a;
}
.layout { display: grid; grid-template-columns: 240px 1fr; min-height: 100vh; }
.sidebar {
  background: #111827;
  color: #e5e7eb;
  padding: 24px 16px;
}
.logo {
  width: 44px; height: 44px; border-radius: 12px;
  background: linear-gradient(135deg, #1e5cf5, #113a8f);
  display: grid; place-items: center; font-weight: 800; color: #fff; margin-bottom: 24px;
}
.menu { display: flex; flex-direction: column; gap: 8px; }
.menu-item {
  color: #e5e7eb; text-decoration: none; padding: 10px 12px; border-radius: 8px;
}
.menu-item:hover, .menu-item.active { background: #1f2937; color: #fff; }

.content { padding: 20px 24px; }
.topbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 16px; background: #fff; border: 1px solid #e5e7eb;
  border-radius: 10px; box-shadow: 0 6px 18px rgba(15,23,42,0.06); margin-bottom: 18px;
}
.userbox { display: flex; align-items: center; gap: 12px; }
.user-name { font-weight: 600; }
.logout { color: #1e5cf5; text-decoration: none; font-weight: 600; }
.logout:hover { text-decoration: underline; }

.card {
  background: #fff; border: 1px solid #e5e7eb; border-radius: 12px;
  box-shadow: 0 8px 20px rgba(15,23,42,0.06); padding: 16px; margin-bottom: 16px;
}
.card-head { display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; margin-bottom: 12px; }
.muted { color: #6b7280; margin: 0; }
.actions { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.input {
  padding: 8px 10px; border: 1px solid #d5d9e0; border-radius: 8px; background: #fff; min-width: 180px;
}
.btn {
  border: 1px solid #d5d9e0; background: #fff; padding: 8px 12px; border-radius: 8px; cursor: pointer; font-weight: 600; color: #0f172a;
}
.btn.primary { background: linear-gradient(120deg, #1e5cf5, #3b82f6); border: none; color: #fff; box-shadow: 0 8px 20px rgba(30,92,245,0.25); }
.btn.ghost { background: #f8f9fb; }

.table-wrap { overflow: auto; }
table { width: 100%; border-collapse: collapse; }
th, td { padding: 10px 8px; text-align: left; border-bottom: 1px solid #eef1f5; }
th { color: #4b5563; font-weight: 600; font-size: 13px; }
.row-actions { display: flex; gap: 8px; }
.link { background: none; border: none; color: #1e5cf5; cursor: pointer; font-weight: 600; }
.link.danger { color: #dc2626; }

.badge { padding: 4px 8px; border-radius: 999px; font-size: 12px; font-weight: 600; }
.badge.success { background: #e8f5e9; color: #15803d; }
.badge.info { background: #e0f2ff; color: #0b6bcb; }
.badge.warning { background: #fff7ed; color: #c2410c; }
.badge.danger { background: #fef2f2; color: #b91c1c; }
.badge.neutral { background: #f3f4f6; color: #374151; }

.kpi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; }
.kpi { background: #f8f9fb; border: 1px solid #e5e7eb; border-radius: 10px; padding: 12px; }
.kpi-title { color: #6b7280; font-size: 13px; }
.kpi-value { font-size: 22px; font-weight: 700; color: #0f172a; }

.grid-2 { display: block; }

.link-muted { color: #1e5cf5; text-decoration: none; font-weight: 600; }
.link-muted:hover { text-decoration: underline; }

.form-grid { display: grid; gap: 10px; max-width: 480px; }
.form-grid p { margin: 0; display: flex; flex-direction: column; gap: 4px; }
.form-grid label { font-weight: 600; color: #0f172a; }
.form-grid input, .form-grid textarea, .form-grid select {
  padding: 10px 12px; border: 1px solid #d5d9e0; border-radius: 8px; background: #fff; color: #0f172a;
}
.form-grid input:focus, .form-grid textarea:focus, .form-grid select:focus {
  border-color: #1e5cf5;
  box-shadow: 0 0 0 3px rgba(30,92,245,0.18);
  outline: none;
}

@media (max-width: 960px) {
  .layout { grid-template-columns: 72px 1fr; }
  .menu-item { padding: 10px 8px; font-size: 13px; }
  .sidebar { padding: 16px 8px; }
}
```

120. templates/accounts/login.html
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

121. templates/accounts/login_base.html
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

122. templates/accounts/password_reset_complete.html
```html
{% extends "accounts/login_base.html" %}
{% block content %}
  <h1 class="auth-title">Пароль обновлён</h1>
  <p class="auth-subtitle">Теперь вы можете войти с новым паролем.</p>
  <a href="/login/" class="btn btn-primary w-100">Перейти ко входу</a>
{% endblock %}
```

123. templates/accounts/password_reset_confirm.html
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

124. templates/accounts/password_reset_done.html
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

125. templates/accounts/password_reset_email.html
```html
{% load i18n %}{% autoescape off %}
Вы запросили сброс пароля для аккаунта {{ user.email }}.

Для установки нового пароля перейдите по ссылке:
{{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}

Если вы не отправляли запрос, просто проигнорируйте это письмо.
{% endautoescape %}
```

126. templates/accounts/password_reset_form.html
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

127. templates/accounts/password_reset_subject.txt
```text
Сброс пароля для Art Culinary CRM
```

128. templates/admin/base_site.html
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

129. templates/admin/index.html
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

130. templates/admin_panel/access.html
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

131. templates/admin_panel/backup_schedule.html
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

132. templates/admin_panel/backups.html
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

133. templates/admin_panel/data_check.html
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

134. templates/admin_panel/entities/delete.html
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

135. templates/admin_panel/entities/detail.html
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

136. templates/admin_panel/entities/form.html
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

137. templates/admin_panel/entities/list.html
```html
{% extends "base.html" %}

{% block title %}{{ entity.label }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Админ‑панель: {{ entity.label }}{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/admin/">Кабинет администратора</a> /
  <a href="/admin-panel/">Админ‑панель</a> /
  {{ entity.label }}
{% endblock %}

{% block content %}
  <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
    <div>
      <h4 class="mb-1">{{ entity.label }}</h4>
      <div class="text-muted">Список записей с поиском и фильтрами</div>
    </div>
    <a href="/admin-panel/entities/{{ entity.slug }}/create/" class="btn btn-primary">Добавить</a>
  </div>

  <div class="card mb-3">
    <form class="row g-2 align-items-end" method="get">
      <div class="col-md-4">
        <label class="form-label">Поиск</label>
        <input type="text" name="q" class="form-control" value="{{ query }}" placeholder="Введите ключевые данные">
      </div>
      {% for f in filters %}
        <div class="col-md-3">
          <label class="form-label">{{ f.label }}</label>
          <select name="{{ f.name }}" class="form-select">
            <option value="">Все</option>
            {% for opt in f.options %}
              <option value="{{ opt.value }}" {% if opt.value|stringformat:"s" == f.value|stringformat:"s" %}selected{% endif %}>
                {{ opt.label }}
              </option>
            {% endfor %}
          </select>
        </div>
      {% endfor %}
      {% for d in date_filters %}
        <div class="col-md-3">
          <label class="form-label">{{ d.label }} с</label>
          <input type="date" name="{{ d.name }}_from" value="{{ d.from }}" class="form-control">
        </div>
        <div class="col-md-3">
          <label class="form-label">{{ d.label }} по</label>
          <input type="date" name="{{ d.name }}_to" value="{{ d.to }}" class="form-control">
        </div>
      {% endfor %}
      <div class="col-md-3">
        <label class="form-label">Сортировка</label>
        <select name="sort" class="form-select">
          <option value="">По умолчанию</option>
          {% for opt in sort_options %}
            <option value="{{ opt.value }}" {% if opt.value == sort_field %}selected{% endif %}>{{ opt.label }}</option>
          {% endfor %}
        </select>
      </div>
      <div class="col-md-3">
        <label class="form-label">Направление</label>
        <select name="dir" class="form-select">
          <option value="desc" {% if sort_dir == "desc" %}selected{% endif %}>По убыванию</option>
          <option value="asc" {% if sort_dir == "asc" %}selected{% endif %}>По возрастанию</option>
        </select>
      </div>
      <div class="col-md-2">
        <button class="btn btn-outline-secondary w-100" type="submit">Применить</button>
      </div>
    </form>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            {% for header in headers %}
              <th>{{ header }}</th>
            {% endfor %}
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {% for row in rows %}
            <tr>
              {% for cell in row.cells %}
                <td>{{ cell }}</td>
              {% endfor %}
              <td>
                <div class="d-flex flex-wrap gap-2">
                  <a class="btn btn-sm btn-outline-secondary" href="/admin-panel/entities/{{ entity.slug }}/{{ row.obj.pk }}/">Открыть</a>
                  <a class="btn btn-sm btn-outline-secondary" href="/admin-panel/entities/{{ entity.slug }}/{{ row.obj.pk }}/edit/">Редактировать</a>
                  <a class="btn btn-sm btn-outline-danger" href="/admin-panel/entities/{{ entity.slug }}/{{ row.obj.pk }}/delete/">Удалить</a>
                </div>
              </td>
            </tr>
          {% empty %}
            <tr>
              <td colspan="{{ headers|length|add:'1' }}" class="text-muted">Записей не найдено</td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  {% if page_obj and paginator.num_pages > 1 %}
    <nav class="mt-3">
      <ul class="pagination">
        <li class="page-item {% if not page_obj.has_previous %}disabled{% endif %}">
          {% if page_obj.has_previous %}
            <a class="page-link" href="?page={{ page_obj.previous_page_number }}{% if query_string %}&{{ query_string }}{% endif %}">Назад</a>
          {% else %}
            <span class="page-link">Назад</span>
          {% endif %}
        </li>
        {% for page in paginator.page_range %}
          {% if page == page_obj.number %}
            <li class="page-item active"><span class="page-link">{{ page }}</span></li>
          {% elif page >= page_obj.number|add:"-2" and page <= page_obj.number|add:"2" %}
            <li class="page-item"><a class="page-link" href="?page={{ page }}{% if query_string %}&{{ query_string }}{% endif %}">{{ page }}</a></li>
          {% endif %}
        {% endfor %}
        <li class="page-item {% if not page_obj.has_next %}disabled{% endif %}">
          {% if page_obj.has_next %}
            <a class="page-link" href="?page={{ page_obj.next_page_number }}{% if query_string %}&{{ query_string }}{% endif %}">Вперёд</a>
          {% else %}
            <span class="page-link">Вперёд</span>
          {% endif %}
        </li>
      </ul>
    </nav>
  {% endif %}
{% endblock %}
```

138. templates/admin_panel/index.html
```html
{% extends "base.html" %}

{% block title %}Админ-панель{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Административная панель{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/admin/">Кабинет администратора</a> / Админ‑панель
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Админ‑панель</h4>
  </div>

  <div class="row g-3 mb-3">
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.users }}</div>
        <div class="kpi-label">Пользователей</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.roles }}</div>
        <div class="kpi-label">Ролей</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.backups }}</div>
        <div class="kpi-label">Резервных копий</div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="d-flex flex-wrap justify-content-between align-items-center gap-2 mb-3">
      <h6 class="mb-0">Сущности и быстрый поиск</h6>
      <form id="entity-search" class="d-flex gap-2" method="get" data-base="/admin-panel/entities/">
        <select name="entity" class="form-select" style="min-width: 220px;">
          {% for e in entities %}
            <option value="{{ e.slug }}">{{ e.label }}</option>
          {% endfor %}
        </select>
        <input type="text" name="q" class="form-control" placeholder="Быстрый поиск">
        <button class="btn btn-primary" type="submit">Найти</button>
      </form>
    </div>

    <div class="row row-cols-1 row-cols-md-3 g-3">
      {% for e in entities %}
        <div class="col">
          <a class="card text-decoration-none h-100" href="/admin-panel/entities/{{ e.slug }}/">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <div class="fw-semibold">{{ e.label }}</div>
                <div class="text-muted small">Записей: {{ e.count }}</div>
              </div>
              <span class="status-pill">Открыть</span>
            </div>
          </a>
        </div>
      {% endfor %}
    </div>
  </div>

  <script>
    const searchForm = document.getElementById("entity-search");
    if (searchForm) {
      searchForm.addEventListener("submit", (e) => {
        const slug = searchForm.entity.value;
        searchForm.action = `${searchForm.dataset.base}${slug}/`;
      });
    }
  </script>
{% endblock %}
```

139. templates/admin_panel/role_form.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/roles/">Роли</a> / {{ title }}
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
        <a href="/admin-panel/roles/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

140. templates/admin_panel/roles_list.html
```html
{% extends "base.html" %}

{% block title %}Роли{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Роли{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/">Админ‑панель</a> / Роли
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Роли</h4>
    <a href="/admin-panel/roles/create/" class="btn btn-primary">Создать роль</a>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Название</th>
          </tr>
        </thead>
        <tbody>
          {% for r in roles %}
            <tr>
              <td>{{ r.name }}</td>
            </tr>
          {% empty %}
            <tr><td class="text-muted">Ролей нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

141. templates/admin_panel/user_delete.html
```html
{% extends "base.html" %}

{% block title %}Удаление пользователя{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Удаление пользователя{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/users/">Пользователи</a> / Удаление
{% endblock %}

{% block content %}
  <div class="card">
    <h5>Удалить пользователя «{{ object.username }}»?</h5>
    <p class="text-muted">Действие нельзя отменить.</p>
    <form method="post">
      {% csrf_token %}
      <button class="btn btn-danger">Удалить</button>
      <a href="/admin-panel/users/" class="btn btn-outline-secondary">Отмена</a>
    </form>
  </div>
{% endblock %}
```

142. templates/admin_panel/user_form.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/users/">Пользователи</a> / {{ title }}
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
        <a href="/admin-panel/users/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

143. templates/admin_panel/user_password.html
```html
{% extends "base.html" %}

{% block title %}Смена пароля{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Смена пароля{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/users/">Пользователи</a> / Смена пароля
{% endblock %}

{% block content %}
  <div class="card">
    <h6>Пользователь: {{ user_obj.username }}</h6>
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
        <a href="/admin-panel/users/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

144. templates/admin_panel/users_list.html
```html
{% extends "base.html" %}

{% block title %}Пользователи{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Пользователи{% endblock %}
{% block breadcrumbs %}
  <a href="/admin-panel/">Админ‑панель</a> / Пользователи
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Пользователи</h4>
    <a href="/admin-panel/users/create/" class="btn btn-primary">Создать пользователя</a>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Логин</th>
            <th>ФИО</th>
            <th>Роли</th>
            <th>Email</th>
            <th>Активен</th>
            <th>Дата создания</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {% for u in users %}
            <tr>
              <td>{{ u.username }}</td>
              <td>{{ u.full_name }}</td>
              <td>
                {% for r in u.roles.all %}
                  <span class="badge-soft primary">{{ r.name }}</span>
                {% empty %}
                  —
                {% endfor %}
              </td>
              <td>{{ u.email }}</td>
              <td>{{ u.is_active|yesno:"Да,Нет" }}</td>
              <td>{{ u.date_joined|date:"d.m.Y" }}</td>
              <td class="text-end">
                <a class="btn btn-sm btn-outline-secondary" href="/admin-panel/users/{{ u.id }}/edit/">Изменить</a>
                <a class="btn btn-sm btn-outline-secondary" href="/admin-panel/users/{{ u.id }}/password/">Пароль</a>
                <form method="post" action="/admin-panel/users/{{ u.id }}/toggle/" class="d-inline">
                  {% csrf_token %}
                  <button class="btn btn-sm btn-outline-secondary">
                    {% if u.is_active %}Блокировать{% else %}Разблокировать{% endif %}
                  </button>
                </form>
                <a class="btn btn-sm btn-outline-danger" href="/admin-panel/users/{{ u.id }}/delete/">Удалить</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="7" class="text-muted">Пользователей нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

145. templates/base.html
```html
{% load static %}
<!doctype html>
<html lang="ru" data-theme="light">
<head>
  <meta charset="utf-8">
  <title>{% block title %}Art Culinary CRM{% endblock %}</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@400;600;700&display=swap" rel="stylesheet">
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
<body>
  <div class="app-shell">
    <aside class="sidebar">
      {% block sidebar %}
        {% if is_admin %}
          {% include "partials/sidebars/admin.html" %}
        {% elif is_logistic %}
          {% include "partials/sidebars/logistic.html" %}
        {% elif is_picker %}
          {% include "partials/sidebars/picker.html" %}
        {% elif is_courier %}
          {% include "partials/sidebars/courier.html" %}
        {% else %}
          {% include "partials/sidebars/manager.html" %}
        {% endif %}
      {% endblock %}
    </aside>

    <div class="main">
      <div class="topbar">
        <div class="topbar-left">
          <div class="system-name">Art Culinary CRM</div>
          <div class="page-title">{% block topbar_title %}Панель{% endblock %}</div>
        </div>
        <div class="d-flex align-items-center gap-3">
          <button id="theme-toggle" class="theme-toggle" type="button" aria-label="Сменить тему">
            <span id="theme-icon">☾</span>
            <span id="theme-label">Светлая</span>
          </button>
          {% if request.user.is_authenticated %}
            <span class="text-muted">{{ request.user.full_name|default:request.user.username }}</span>
            <a href="/logout/" class="btn btn-outline-secondary btn-sm">Выйти</a>
          {% endif %}
        </div>
      </div>

      <main class="content p-4">
        <div class="breadcrumbs">
          {% block breadcrumbs %}
            <a href="/dashboard/">Главная</a>
          {% endblock %}
        </div>

        {% if messages %}
          <div class="notify-stack" aria-live="polite" aria-atomic="true">
            {% for message in messages %}
              <div
                class="notify-card"
                role="status"
                data-delay="5200"
                data-level="{% if 'success' in message.tags %}success{% elif 'error' in message.tags or 'danger' in message.tags %}danger{% elif 'warning' in message.tags %}warning{% else %}info{% endif %}"
              >
                <div class="notify-icon">
                  {% if 'success' in message.tags %}✔{% elif 'error' in message.tags or 'danger' in message.tags %}✖{% elif 'warning' in message.tags %}!{% else %}i{% endif %}
                </div>
                <div class="notify-content">
                  <div class="notify-title">
                    {% if 'success' in message.tags %}Успешно{% elif 'error' in message.tags or 'danger' in message.tags %}Ошибка{% elif 'warning' in message.tags %}Внимание{% else %}Сообщение{% endif %}
                  </div>
                  <div class="notify-text">{{ message }}</div>
                </div>
                <button type="button" class="notify-close" aria-label="Закрыть">×</button>
                <div class="notify-progress"></div>
              </div>
            {% endfor %}
          </div>
        {% endif %}

        {% block content %}{% endblock %}
      </main>
    </div>
  </div>

  <script>
    const key = "crm_theme";
    const html = document.documentElement;
    const btn = document.getElementById("theme-toggle");
    const icon = document.getElementById("theme-icon");
    const label = document.getElementById("theme-label");
    const applyTheme = (t) => { html.setAttribute("data-theme", t); localStorage.setItem(key, t); };
    const saved = localStorage.getItem(key) || "light";
    applyTheme(saved);
    const updateToggle = () => {
      const isDark = html.getAttribute("data-theme") === "dark";
      icon.textContent = isDark ? "☀︎" : "☾";
      label.textContent = isDark ? "Тёмная" : "Светлая";
    };
    updateToggle();
    btn.addEventListener("click", () => {
      const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
      updateToggle();
    });
  </script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    if (window.lucide) {
      lucide.createIcons();
    }
  </script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const cards = document.querySelectorAll(".notify-card");
      cards.forEach((card, index) => {
        const delay = parseInt(card.dataset.delay || "5000", 10);
        card.style.animationDelay = `${index * 80}ms`;
        card.classList.add("is-visible");

        const closeBtn = card.querySelector(".notify-close");
        const closeCard = () => {
          card.classList.remove("is-visible");
          card.classList.add("is-hiding");
          window.setTimeout(() => card.remove(), 260);
        };

        if (closeBtn) {
          closeBtn.addEventListener("click", closeCard);
        }
        window.setTimeout(closeCard, delay);
      });
    });
  </script>
  {% block extra_js %}{% endblock %}
</body>
</html>
```

146. templates/clients/delete.html
```html
{% extends "base.html" %}

{% block title %}Удаление клиента{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Удаление клиента{% endblock %}
{% block breadcrumbs %}
  <a href="/clients/">Клиенты</a> / Удаление
{% endblock %}

{% block content %}
  <div class="card">
    <h5>Удалить клиента «{{ object.name }}»?</h5>
    <p class="text-muted">Действие нельзя отменить.</p>
    <form method="post">
      {% csrf_token %}
      <button class="btn btn-danger">Удалить</button>
      <a href="/clients/" class="btn btn-outline-secondary">Отмена</a>
    </form>
  </div>
{% endblock %}
```

147. templates/clients/detail.html
```html
{% extends "base.html" %}

{% block title %}Карточка клиента{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Карточка клиента{% endblock %}
{% block breadcrumbs %}
  <a href="/clients/">Клиенты</a> / Карточка
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">{{ client.name }}</h4>
    <div class="d-flex gap-2">
      <a href="/clients/{{ client.id }}/edit/" class="btn btn-outline-secondary">Редактировать</a>
      <a href="/clients/" class="btn btn-outline-secondary">К списку</a>
    </div>
  </div>

  <div class="row g-3 mb-3">
    <div class="col-lg-8">
      <div class="card">
        <h6>Основная информация</h6>
        <div class="row g-3 mt-1">
          <div class="col-md-6"><strong>Тип:</strong> {{ client.get_client_type_display }}</div>
          <div class="col-md-6"><strong>Статус:</strong> {{ client.get_status_display }}</div>
          <div class="col-md-6"><strong>Этап:</strong> {{ client.current_stage.name|default:"—" }}</div>
          <div class="col-md-6"><strong>Менеджер:</strong> {{ client.responsible_manager.full_name|default:"—" }}</div>
          <div class="col-md-6"><strong>Телефон:</strong> {{ client.phone|default:"—" }}</div>
          <div class="col-md-6"><strong>Email:</strong> {{ client.email|default:"—" }}</div>
          <div class="col-12"><strong>Адрес доставки:</strong> {{ client.default_delivery_address|default:"—" }}</div>
        </div>
      </div>
    </div>
    <div class="col-lg-4">
      <div class="card">
        <h6>Смена этапа</h6>
        <form method="post">
          {% csrf_token %}
          <input type="hidden" name="action" value="change_stage">
          <div class="mb-2">
            {{ stage_form.stage }}
            {% if stage_form.stage.errors %}<div class="text-danger small">{{ stage_form.stage.errors|striptags }}</div>{% endif %}
          </div>
          <div class="mb-2">
            {{ stage_form.comment }}
          </div>
          <button class="btn btn-primary w-100">Обновить этап</button>
        </form>
      </div>
    </div>
  </div>

  <ul class="nav nav-tabs mb-3" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#tab-interactions" type="button">Взаимодействия</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" data-bs-toggle="tab" data-bs-target="#tab-orders" type="button">Заказы клиента</button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" data-bs-toggle="tab" data-bs-target="#tab-history" type="button">История этапов</button>
    </li>
  </ul>

  <div class="tab-content">
    <div class="tab-pane fade show active" id="tab-interactions">
      <div class="card">
        <div class="section-header">
          <h6 class="mb-0">Журнал взаимодействий</h6>
        </div>
        <form method="post" class="mb-3">
          {% csrf_token %}
          <input type="hidden" name="action" value="add_interaction">
          <div class="row g-2">
            <div class="col-md-4">{{ interaction_form.interaction_type }}</div>
            <div class="col-md-4">{{ interaction_form.happened_at }}</div>
            <div class="col-md-12">{{ interaction_form.note }}</div>
          </div>
          <button class="btn btn-outline-secondary mt-2">Добавить запись</button>
        </form>
        <div class="table-responsive">
          <table class="table mb-0">
            <thead>
              <tr>
                <th>Тип</th>
                <th>Комментарий</th>
                <th>Дата/время</th>
                <th>Менеджер</th>
              </tr>
            </thead>
            <tbody>
              {% for i in interactions %}
                <tr>
                  <td>{{ i.get_interaction_type_display }}</td>
                  <td>{{ i.note|default:"—" }}</td>
                  <td>{{ i.happened_at|date:"d.m.Y H:i" }}</td>
                  <td>{{ i.manager.full_name|default:"—" }}</td>
                </tr>
              {% empty %}
                <tr><td colspan="4" class="text-muted">Записей нет</td></tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="tab-pane fade" id="tab-orders">
      <div class="card">
        <div class="table-responsive">
          <table class="table mb-0">
            <thead>
              <tr>
                <th>Номер</th>
                <th>Сумма</th>
                <th>Статус</th>
                <th>Дата</th>
              </tr>
            </thead>
            <tbody>
              {% for o in client_orders %}
                <tr>
                  <td>{{ o.order_number }}</td>
                  <td>{{ o.total_amount }}</td>
                  <td>{{ o.get_status_display }}</td>
                  <td>{{ o.created_at|date:"d.m.Y" }}</td>
                </tr>
              {% empty %}
                <tr><td colspan="4" class="text-muted">Заказов нет</td></tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="tab-pane fade" id="tab-history">
      <div class="card">
        <ul class="list-group list-group-flush">
          {% for h in stage_history %}
            <li class="list-group-item bg-transparent">
              <div class="fw-semibold">{{ h.stage.name|default:"—" }}</div>
              <div class="text-muted small">{{ h.changed_at|date:"d.m.Y H:i" }}</div>
              <div class="small">{{ h.comment|default:"" }}</div>
            </li>
          {% empty %}
            <li class="list-group-item text-muted bg-transparent">История пуста</li>
          {% endfor %}
        </ul>
      </div>
    </div>
  </div>
{% endblock %}
```

148. templates/clients/form.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/clients/">Клиенты</a> / {{ title }}
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
        <a href="/clients/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

149. templates/clients/list.html
```html
{% extends "base.html" %}

{% block title %}Клиенты{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Клиенты{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/manager/">Кабинет менеджера</a> / Клиенты / Список
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Клиенты</h4>
    <a href="/clients/create/" class="btn btn-primary">Добавить клиента</a>
  </div>

  <div class="card mb-3">
    <form class="filters" method="get">
      <input class="form-control" type="text" name="q" value="{{ request.GET.q }}" placeholder="Поиск по имени, телефону, почте">
      <select class="form-select" name="status">
        <option value="">Все статусы</option>
        {% for value, label in status_choices %}
          <option value="{{ value }}" {% if request.GET.status == value %}selected{% endif %}>{{ label }}</option>
        {% endfor %}
      </select>
      <select class="form-select" name="stage">
        <option value="">Все этапы</option>
        {% for s in stages %}
          <option value="{{ s.id }}" {% if request.GET.stage == s.id|stringformat:"s" %}selected{% endif %}>{{ s.name }}</option>
        {% endfor %}
      </select>
      <select class="form-select" name="sort">
        <option value="">Сортировка</option>
        <option value="created_at" {% if request.GET.sort == "created_at" %}selected{% endif %}>По дате ↑</option>
        <option value="-created_at" {% if request.GET.sort == "-created_at" %}selected{% endif %}>По дате ↓</option>
        <option value="name" {% if request.GET.sort == "name" %}selected{% endif %}>По названию A‑Я</option>
        <option value="-name" {% if request.GET.sort == "-name" %}selected{% endif %}>По названию Я‑A</option>
      </select>
      <button class="btn btn-outline-secondary" type="submit">Фильтр</button>
    </form>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Название/ФИО</th>
            <th>Телефон</th>
            <th>Электронная почта</th>
            <th>Этап</th>
            <th>Статус</th>
            <th>Дата создания</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {% for c in clients %}
            <tr>
              <td><a href="/clients/{{ c.id }}/" class="text-decoration-none">{{ c.name }}</a></td>
              <td>{{ c.phone|default:"—" }}</td>
              <td>{{ c.email|default:"—" }}</td>
              <td>{{ c.current_stage.name|default:"—" }}</td>
              <td>
                <span class="badge-soft {% if c.status == 'active' %}success{% elif c.status == 'lost' %}danger{% else %}warn{% endif %}">
                  {{ c.get_status_display }}
                </span>
              </td>
              <td>{{ c.created_at|date:"d.m.Y" }}</td>
              <td class="text-end">
                <a class="btn btn-sm btn-outline-secondary" href="/clients/{{ c.id }}/edit/">Изменить</a>
                <a class="btn btn-sm btn-outline-danger" href="/clients/{{ c.id }}/delete/">Удалить</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="6" class="text-muted">Нет клиентов</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

150. templates/courier/profile.html
```html
{% extends "base.html" %}

{% block title %}Профиль курьера{% endblock %}
{% block sidebar %}{% include "partials/sidebars/courier.html" %}{% endblock %}
{% block topbar_title %}Профиль курьера{% endblock %}
{% block breadcrumbs %}
  <a href="/logistics/courier/routes/">Кабинет курьера</a> / Профиль
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Профиль курьера</h4>
  </div>

  <div class="row g-3">
    <div class="col-lg-5">
      <div class="card">
        <h6>Текущие параметры</h6>
        <div class="small text-muted">Тип транспорта</div>
        <div class="fw-semibold mb-2">{{ courier.transport_type|default:"—" }}</div>
        <div class="small text-muted">Зона</div>
        <div class="fw-semibold mb-2">{{ courier.zone|default:"—" }}</div>
        <div class="small text-muted">Статус</div>
        <div class="fw-semibold mb-2">{{ courier.status|default:"—" }}</div>
        <div class="small text-muted">Грузоподъёмность (кг)</div>
        <div class="fw-semibold mb-2">{{ courier.payload_capacity_kg|default:"—" }}</div>
      </div>
    </div>
    <div class="col-lg-7">
      <div class="card">
        <h6>Редактирование профиля</h6>
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
            <a href="/logistics/courier/routes/" class="btn btn-outline-secondary">К маршрутам</a>
          </div>
        </form>
      </div>
    </div>
  </div>
{% endblock %}
```

151. templates/courier/route_detail.html
```html
{% extends "base.html" %}

{% block title %}Маршрут курьера{% endblock %}
{% block sidebar %}{% include "partials/sidebars/courier.html" %}{% endblock %}
{% block topbar_title %}Маршрут{% endblock %}
{% block breadcrumbs %}
  <a href="/logistics/courier/routes/">Курьер</a> / Маршрут
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Маршрут на {{ route.planned_date|date:"d.m.Y" }}</h4>
    <a href="/logistics/courier/routes/" class="btn btn-outline-secondary">Назад</a>
  </div>

  <div class="card mb-3">
    <div class="section-header">
      <h6 class="mb-0">Навигация</h6>
      <a id="open-route-maps" class="btn btn-outline-secondary" href="#" target="_blank" rel="noopener">Открыть в Google Maps</a>
    </div>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Порядок</th>
            <th>Адрес</th>
            <th>План</th>
            <th>Вес/Объём</th>
            <th>Статус</th>
            <th>Проверка</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for s in stops %}
            <tr>
              <td>{{ s.sequence_index }}</td>
              <td>{{ s.delivery.address|default:s.delivery.order.address|default:"—" }}</td>
              <td>{{ s.planned_time|date:"d.m.Y H:i"|default:"—" }}</td>
              <td>{{ s.delivery.cargo_weight_kg|default:"—" }} / {{ s.delivery.cargo_volume_m3|default:"—" }}</td>
              <td>{{ s.status }}</td>
              <td>{{ s.proof_review_status }}</td>
              <td class="text-end">
                <form method="post" action="/logistics/courier/stops/{{ s.id }}/update/" class="d-inline">
                  {% csrf_token %}
                  <input type="hidden" name="status" value="В пути">
                  <button class="btn btn-sm btn-outline-secondary">В пути</button>
                </form>
                <button class="btn btn-sm btn-outline-secondary" data-bs-toggle="collapse" data-bs-target="#done-{{ s.id }}">Доставлено</button>
                <button class="btn btn-sm btn-outline-secondary" data-bs-toggle="collapse" data-bs-target="#fail-{{ s.id }}">Не доставлено</button>
              </td>
            </tr>
            <tr class="collapse" id="done-{{ s.id }}">
              <td colspan="6">
                <form method="post" action="/logistics/courier/stops/{{ s.id }}/proof/" enctype="multipart/form-data" class="row g-2">
                  {% csrf_token %}
                  <div class="col-md-6">
                    <label class="form-label">Документ доставки (PDF/JPG/PNG)</label>
                    <input type="file" name="proof_of_delivery" class="form-control" required>
                  </div>
                  <div class="col-md-6 d-flex align-items-end gap-2">
                    <input type="hidden" name="status" value="Доставлено">
                    <button class="btn btn-primary">Загрузить и завершить</button>
                    {% if s.proof_of_delivery %}
                      <a class="btn btn-outline-secondary" href="{{ s.proof_of_delivery.url }}" target="_blank">Просмотр</a>
                    {% endif %}
                  </div>
                </form>
              </td>
            </tr>
            <tr class="collapse" id="fail-{{ s.id }}">
              <td colspan="6">
                <form method="post" action="/logistics/courier/stops/{{ s.id }}/update/" class="row g-2">
                  {% csrf_token %}
                  <input type="hidden" name="status" value="Не доставлено">
                  <div class="col-md-6">
                    <label class="form-label">Причина</label>
                    <input type="text" name="failure_reason" class="form-control" required>
                  </div>
                  <div class="col-md-6">
                    <label class="form-label">Комментарий</label>
                    <input type="text" name="note" class="form-control">
                  </div>
                  <div class="col-md-12">
                    <button class="btn btn-primary">Подтвердить</button>
                  </div>
                </form>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="6" class="text-muted">Остановок нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <script>
    (function() {
      const addresses = [];
      {% for s in stops %}
        {% if s.delivery.address or s.delivery.order.address %}
          addresses.push("{{ s.delivery.address|default:s.delivery.order.address|escapejs }}");
        {% endif %}
      {% endfor %}
      if (addresses.length >= 2) {
        const origin = encodeURIComponent(addresses[0]);
        const destination = encodeURIComponent(addresses[addresses.length - 1]);
        const waypoints = addresses.slice(1, -1).map(encodeURIComponent).join("|");
        let url = `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${destination}`;
        if (waypoints) url += `&waypoints=${waypoints}`;
        const link = document.getElementById("open-route-maps");
        if (link) link.href = url;
      }
    })();
  </script>
{% endblock %}
```

152. templates/courier/routes.html
```html
{% extends "base.html" %}

{% block title %}Маршруты курьера{% endblock %}
{% block sidebar %}{% include "partials/sidebars/courier.html" %}{% endblock %}
{% block topbar_title %}Маршруты курьера{% endblock %}
{% block breadcrumbs %}
  <a href="/logistics/courier/routes/">Курьер</a> / Маршруты
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Мои маршруты</h4>
  </div>

  <div class="card mb-3">
    <form method="get" class="row g-2 align-items-end">
      <div class="col-md-4">
        <label class="form-label">Дата</label>
        <input type="date" name="date" value="{{ request.GET.date }}" class="form-control">
      </div>
      <div class="col-md-4 d-flex gap-2">
        <button class="btn btn-primary">Применить</button>
        <a href="/logistics/courier/routes/" class="btn btn-outline-secondary">Сбросить</a>
      </div>
    </form>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Дата</th>
            <th>Статус</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for r in routes %}
            <tr>
              <td>{{ r.planned_date|date:"d.m.Y" }}</td>
              <td>{{ r.status }}</td>
              <td class="text-end">
                <a href="/logistics/courier/routes/{{ r.id }}/" class="btn btn-sm btn-outline-secondary">Открыть</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="3" class="text-muted">Маршрутов нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

153. templates/dashboard/admin.html
```html
{% extends "base.html" %}

{% block title %}Панель администратора{% endblock %}
{% block sidebar %}{% include "partials/sidebars/admin.html" %}{% endblock %}
{% block topbar_title %}Панель администратора системы{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/admin/">Кабинет администратора</a> / Обзор
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Обзор системы</h4>
    <div class="d-flex gap-2">
      <a href="/admin-panel/users/create/" class="btn btn-primary">Новый пользователь</a>
      <a href="/admin-panel/backups/" class="btn btn-outline-secondary">Бэкапы</a>
    </div>
  </div>

  <div class="row g-3 mb-4">
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.clients }}</div>
        <div class="kpi-label">Клиентов</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.orders }}</div>
        <div class="kpi-label">Заказов</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.reports }}</div>
        <div class="kpi-label">Отчётов</div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="section-header">
      <h6 class="mb-0">Быстрые действия</h6>
    </div>
    <div class="d-flex flex-wrap gap-2">
      <a href="/admin-panel/users/" class="btn btn-outline-secondary">Пользователи</a>
      <a href="/admin-panel/roles/" class="btn btn-outline-secondary">Роли</a>
      <a href="/clients/" class="btn btn-outline-secondary">Клиенты</a>
      <a href="/orders/" class="btn btn-outline-secondary">Заказы</a>
    </div>
  </div>
{% endblock %}
```

154. templates/dashboard/logistic.html
```html
{% extends "base.html" %}

{% block title %}Панель логиста{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}Панель логиста{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/logistic/">Кабинет логиста</a> / Обзор
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Обзор логистики</h4>
    <a href="/logistics/" class="btn btn-primary">К доставкам</a>
  </div>

  <div class="row g-3 mb-4">
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.couriers_total }}</div>
        <div class="kpi-label">Всего курьеров</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.couriers_free }}</div>
        <div class="kpi-label">Свободные курьеры</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.active_cargo }}</div>
        <div class="kpi-label">Активные грузы</div>
      </div>
    </div>
  </div>

  <div class="row g-3 mb-4">
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.deliveries }}</div>
        <div class="kpi-label">Всего доставок</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.pending }}</div>
        <div class="kpi-label">Ожидают отправки</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">Быстрый доступ</div>
        <div class="d-flex gap-2 mt-2">
          <a href="/logistics/couriers/" class="btn btn-outline-secondary btn-sm">Курьеры</a>
          <a href="/logistics/routes/" class="btn btn-outline-secondary btn-sm">Маршруты</a>
        </div>
      </div>
    </div>
  </div>

  <div class="card mb-4">
    <div class="section-header">
      <h6 class="mb-0">Быстрая фильтрация курьеров</h6>
      <a href="/logistics/couriers/" class="link-muted">Открыть список</a>
    </div>
    <div class="d-flex flex-wrap gap-2">
      <a href="/logistics/couriers/?status=Свободен" class="btn btn-outline-secondary btn-sm">Свободные</a>
      <a href="/logistics/couriers/?status=Занят" class="btn btn-outline-secondary btn-sm">Занятые</a>
      <a href="/logistics/couriers/?status=В%20рейсе" class="btn btn-outline-secondary btn-sm">В рейсе</a>
    </div>
  </div>

  <div class="row g-3 mb-4">
    <div class="col-lg-4">
      <div class="card">
        <h6>Активные маршруты</h6>
        <ul class="list-group list-group-flush">
          {% for r in routes_payload %}
            <li class="list-group-item bg-transparent">
              <div class="fw-semibold">{{ r.title }}</div>
              <div class="small text-muted">{{ r.status }}</div>
              <button class="btn btn-sm btn-outline-secondary mt-2" data-route-id="{{ r.id }}">Показать на карте</button>
            </li>
          {% empty %}
            <li class="list-group-item text-muted bg-transparent">Активных маршрутов нет</li>
          {% endfor %}
        </ul>
      </div>
    </div>
    <div class="col-lg-8">
      <div class="card">
        <h6>Карта активных маршрутов</h6>
        <div id="logistic-map" style="height: 360px;"></div>
        <div class="mt-2">
          <a id="open-in-maps" class="link-muted" href="#" target="_blank" rel="noopener">Открыть в Google Maps</a>
        </div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="section-header">
      <h6 class="mb-0">Последние доставки</h6>
      <a href="/logistics/" class="link-muted">Открыть список</a>
    </div>
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Заказ</th>
            <th>Адрес</th>
            <th>Статус</th>
          </tr>
        </thead>
        <tbody>
          {% for d in recent_deliveries %}
            <tr>
              <td>{{ d.order.order_number }}</td>
              <td>{{ d.address|default:"—" }}</td>
              <td>{{ d.is_sent|yesno:"Отправлен,Ожидает" }}</td>
            </tr>
          {% empty %}
            <tr><td colspan="3" class="text-muted">Нет данных</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  {{ routes_payload|json_script:"routes-data" }}
  <script>
    async function geocodeAddress(address) {
      const url = "https://nominatim.openstreetmap.org/search?format=json&q=" + encodeURIComponent(address);
      const res = await fetch(url, { headers: { "Accept-Language": "ru" } });
      const data = await res.json();
      if (!data.length) return null;
      return { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lon) };
    }

    function buildGoogleMapsLink(points) {
      const addresses = points.map((p) => p.address).filter(Boolean);
      if (addresses.length < 2) return "#";
      const origin = encodeURIComponent(addresses[0]);
      const destination = encodeURIComponent(addresses[addresses.length - 1]);
      const waypoints = addresses.slice(1, -1).map(encodeURIComponent).join("|");
      let url = `https://www.google.com/maps/dir/?api=1&origin=${origin}&destination=${destination}`;
      if (waypoints) url += `&waypoints=${waypoints}`;
      return url;
    }

    async function initLogisticMap() {
      const data = JSON.parse(document.getElementById("routes-data").textContent || "[]");
      const mapEl = document.getElementById("logistic-map");
      if (!mapEl) return;
      const map = L.map(mapEl);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "&copy; OpenStreetMap",
      }).addTo(map);

      let polyline = null;
      let markers = [];

      async function renderRoute(route) {
        const points = [];
        for (const stop of route.stops || []) {
          let point = null;
          if (stop.lat && stop.lng) {
            point = { lat: stop.lat, lng: stop.lng, address: stop.address };
          } else if (stop.address) {
            const geo = await geocodeAddress(stop.address);
            if (geo) point = { ...geo, address: stop.address };
          }
          if (point) points.push(point);
        }

        markers.forEach((m) => map.removeLayer(m));
        markers = [];
        if (polyline) map.removeLayer(polyline);

        if (points.length) {
          const latLngs = points.map((p) => [p.lat, p.lng]);
          polyline = L.polyline(latLngs, { color: "#3b82f6" }).addTo(map);
          markers = points.map((p) => L.marker([p.lat, p.lng]).addTo(map).bindPopup(p.address || "Точка"));
          map.fitBounds(latLngs, { padding: [30, 30] });
        } else {
          map.setView([55.751244, 37.618423], 10);
        }

        const link = document.getElementById("open-in-maps");
        if (link) link.href = buildGoogleMapsLink(route.stops || []);
      }

      const firstRoute = data[0];
      if (firstRoute) await renderRoute(firstRoute);

      document.querySelectorAll("[data-route-id]").forEach((btn) => {
        btn.addEventListener("click", async () => {
          const route = data.find((r) => String(r.id) === btn.dataset.routeId);
          if (route) await renderRoute(route);
        });
      });
    }
  </script>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>initLogisticMap();</script>
{% endblock %}
```

155. templates/dashboard/manager.html
```html
{% extends "base.html" %}

{% block title %}Панель менеджера{% endblock %}
{% block sidebar %}{% include "partials/sidebars/manager.html" %}{% endblock %}
{% block topbar_title %}Панель менеджера{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/manager/">Кабинет менеджера</a> / Обзор
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Обзор</h4>
    <div class="d-flex gap-2">
      <a href="/clients/create/" class="btn btn-primary">Новый клиент</a>
      <a href="/orders/create/" class="btn btn-outline-secondary">Новый заказ</a>
    </div>
  </div>

  <div class="row g-3 mb-4">
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.clients }}</div>
        <div class="kpi-label">Клиентов в базе</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.orders }}</div>
        <div class="kpi-label">Всего заказов</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.active_orders }}</div>
        <div class="kpi-label">Заказы в работе</div>
      </div>
    </div>
  </div>

  <div class="row g-3">
    <div class="col-lg-6">
      <div class="card">
        <div class="section-header">
          <h6 class="mb-0">Новые клиенты</h6>
          <a href="/clients/" class="link-muted">Все клиенты</a>
        </div>
        <div class="table-responsive">
          <table class="table mb-0">
            <thead>
              <tr>
                <th>Название</th>
                <th>Статус</th>
              </tr>
            </thead>
            <tbody>
              {% for c in recent_clients %}
                <tr>
                  <td><a href="/clients/{{ c.id }}/" class="text-decoration-none">{{ c.name }}</a></td>
                  <td>{{ c.get_status_display }}</td>
                </tr>
              {% empty %}
                <tr><td colspan="2" class="text-muted">Нет данных</td></tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="card">
        <div class="section-header">
          <h6 class="mb-0">Последние заказы</h6>
          <a href="/orders/" class="link-muted">Все заказы</a>
        </div>
        <div class="table-responsive">
          <table class="table mb-0">
            <thead>
              <tr>
                <th>Номер</th>
                <th>Клиент</th>
                <th>Статус</th>
              </tr>
            </thead>
            <tbody>
              {% for o in recent_orders %}
                <tr>
                  <td>{{ o.order_number }}</td>
                  <td>{{ o.client.name }}</td>
                  <td>{{ o.get_status_display }}</td>
                </tr>
              {% empty %}
                <tr><td colspan="3" class="text-muted">Нет данных</td></tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
```

156. templates/dashboard/picker.html
```html
{% extends "base.html" %}

{% block title %}Панель сборщика{% endblock %}
{% block sidebar %}{% include "partials/sidebars/picker.html" %}{% endblock %}
{% block topbar_title %}Панель сборщика заказов{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/picker/">Кабинет сборщика</a> / Обзор
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Обзор производства</h4>
    <a href="/orders/picker/" class="btn btn-primary">К заказам</a>
  </div>

  <div class="row g-3 mb-4">
    <div class="col-md-6">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.orders }}</div>
        <div class="kpi-label">Всего заказов</div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="card kpi-card">
        <div class="kpi-value">{{ stats.in_progress }}</div>
        <div class="kpi-label">В производстве</div>
      </div>
    </div>
  </div>

  <div class="card">
    <div class="section-header">
      <h6 class="mb-0">Последние заказы</h6>
      <a href="/orders/picker/" class="link-muted">Открыть список</a>
    </div>
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Номер</th>
            <th>Клиент</th>
            <th>Статус</th>
          </tr>
        </thead>
        <tbody>
          {% for o in recent_orders %}
            <tr>
              <td>{{ o.order_number }}</td>
              <td>{{ o.client.name }}</td>
              <td>{{ o.get_status_display }}</td>
            </tr>
          {% empty %}
            <tr><td colspan="3" class="text-muted">Нет данных</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

157. templates/login_root.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Вход в Art Culinary CRM</title>
  <link rel="stylesheet" href="{% static 'login_root.css' %}">
</head>
<body>
  <div class="root-login">
    <div class="login-card">
      <div class="logo">AC</div>
      <h1>Art Culinary CRM</h1>
      <p class="subtitle">Авторизация в системе</p>
      <form method="post" action="{% url 'root-login' %}">
        {% csrf_token %}
        {% if form.errors %}
          <p class="errornote">Пожалуйста, введите корректные данные или войдите под учётной записью с ролью менеджера.</p>
        {% endif %}
        <label for="id_username">Электронная почта</label>
        <input type="text" id="id_username" name="username" autocomplete="username" required>

        <label for="id_password">Пароль</label>
        <input type="password" id="id_password" name="password" autocomplete="current-password" required>

        <button type="submit" class="btn primary">Войти</button>
        <a class="link" href="#">Забыли пароль?</a>
      </form>
    </div>
  </div>
</body>
</html>
```

158. templates/logistics/couriers.html
```html
{% extends "base.html" %}

{% block title %}Курьеры{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}Курьеры{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/logistic/">Кабинет логиста</a> / Курьеры
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Курьеры</h4>
  </div>

  <div class="card mb-3">
    <form method="get" class="row g-2 align-items-end">
      <div class="col-md-3">
        <label class="form-label">Статус</label>
        <select name="status" class="form-select">
          <option value="">Все</option>
          {% for value, label in status_choices %}
            <option value="{{ value }}" {% if request.GET.status == value %}selected{% endif %}>{{ label }}</option>
          {% endfor %}
        </select>
      </div>
      <div class="col-md-3">
        <label class="form-label">Тип транспорта</label>
        <select name="transport" class="form-select">
          <option value="">Все</option>
          {% for t in transport_types %}
            <option value="{{ t }}" {% if request.GET.transport == t %}selected{% endif %}>{{ t }}</option>
          {% endfor %}
        </select>
      </div>
      <div class="col-md-2">
        <label class="form-label">Зона</label>
        <input type="text" name="zone" value="{{ request.GET.zone }}" class="form-control" placeholder="Напр. Центр">
      </div>
      <div class="col-md-2">
        <label class="form-label">Груз (кг)</label>
        <input type="number" step="0.01" name="min_payload" value="{{ request.GET.min_payload }}" class="form-control" placeholder="Мин.">
      </div>
      <div class="col-md-2">
        <label class="form-label">Объём (м³)</label>
        <input type="number" step="0.01" name="min_volume" value="{{ request.GET.min_volume }}" class="form-control" placeholder="Мин.">
      </div>
      <div class="col-md-3">
        <label class="form-label">Сортировка</label>
        <select name="sort" class="form-select">
          <option value="">По умолчанию</option>
          <option value="name" {% if request.GET.sort == 'name' %}selected{% endif %}>Имя (А-Я)</option>
          <option value="-name" {% if request.GET.sort == '-name' %}selected{% endif %}>Имя (Я-А)</option>
          <option value="payload" {% if request.GET.sort == 'payload' %}selected{% endif %}>Грузоподъёмность</option>
          <option value="-payload" {% if request.GET.sort == '-payload' %}selected{% endif %}>Грузоподъёмность ↓</option>
          <option value="updated" {% if request.GET.sort == 'updated' %}selected{% endif %}>Обновление гео</option>
          <option value="-updated" {% if request.GET.sort == '-updated' %}selected{% endif %}>Обновление гео ↓</option>
        </select>
      </div>
      <div class="col-md-3 d-flex gap-2">
        <button class="btn btn-primary">Применить</button>
        <a href="/logistics/couriers/" class="btn btn-outline-secondary">Сбросить</a>
      </div>
    </form>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>ФИО</th>
            <th>Телефон</th>
            <th>Активность</th>
            <th>Зона</th>
            <th>Транспорт</th>
            <th>Грузоподъёмность</th>
            <th>Объём/Габариты</th>
            <th>Геолокация</th>
          </tr>
        </thead>
        <tbody>
          {% for c in couriers %}
            <tr>
              <td>{{ c.user.full_name }}</td>
              <td>{{ c.user.phone|default:"—" }}</td>
              <td>
                <span class="badge-soft {% if c.status == 'Свободен' %}success{% elif c.status == 'В рейсе' %}primary{% else %}warn{% endif %}">
                  {{ c.get_status_display }}
                </span>
              </td>
              <td>{{ c.zone|default:"—" }}</td>
              <td>{{ c.transport_type|default:"—" }}</td>
              <td>{{ c.payload_capacity_kg|default:"—" }}</td>
              <td>
                <div class="small text-muted">Объём: {{ c.cargo_volume_m3|default:"—" }}</div>
                <div class="small text-muted">Габариты: {{ c.cargo_length_cm|default:"—" }}×{{ c.cargo_width_cm|default:"—" }}×{{ c.cargo_height_cm|default:"—" }}</div>
              </td>
              <td>
                {% if c.current_lat and c.current_lng %}
                  {{ c.current_lat }}, {{ c.current_lng }}
                  <div class="small text-muted">{{ c.location_updated_at|date:"d.m.Y H:i"|default:"" }}</div>
                {% else %}
                  —
                {% endif %}
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="8" class="text-muted">Курьеры не найдены</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

159. templates/logistics/delivery_card.html
```html
{% extends "base.html" %}

{% block title %}Карточка доставки{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}Карточка доставки{% endblock %}
{% block breadcrumbs %}
  <a href="/logistics/">Заказы на доставку</a> / Карточка
{% endblock %}

{% block content %}
  <div class="section-header">
    <div>
      <h4 class="mb-1">Доставка по заказу №{{ delivery.order.order_number }}</h4>
      <span class="badge-soft {% if delivery.status == 'Доставлено' %}success{% elif delivery.status == 'Отменено' %}danger{% elif delivery.status == 'В пути' %}primary{% else %}warn{% endif %}">
        {{ delivery.status }}
      </span>
    </div>
    <a href="/logistics/" class="btn btn-outline-secondary">К списку</a>
  </div>

  <div class="row g-3">
    <div class="col-lg-4">
      <div class="card">
        <h6>Данные заказа</h6>
        <div class="small text-muted">Клиент</div>
        <div class="fw-semibold mb-2">{{ delivery.order.client.name }}</div>
        <div class="small text-muted">Адрес</div>
        <div class="mb-2">{{ delivery.address|default:delivery.order.address|default:"—" }}</div>
        <div class="small text-muted">Сумма</div>
        <div class="fw-semibold">{{ delivery.order.total_amount }}</div>
      </div>
      <div class="card mt-3">
        <h6>Параметры груза</h6>
        <div class="small text-muted">Вес (кг)</div>
        <div class="fw-semibold mb-2">{{ delivery.cargo_weight_kg|default:"—" }}</div>
        <div class="small text-muted">Объём (м³)</div>
        <div class="fw-semibold mb-2">{{ delivery.cargo_volume_m3|default:"—" }}</div>
        <div class="small text-muted">Габариты (см)</div>
        <div class="fw-semibold">{{ delivery.cargo_length_cm|default:"—" }}×{{ delivery.cargo_width_cm|default:"—" }}×{{ delivery.cargo_height_cm|default:"—" }}</div>
      </div>
      <div class="card mt-3">
        <h6>Подходящие курьеры</h6>
        <ul class="list-group list-group-flush">
          {% for c in suitable_couriers %}
            <li class="list-group-item bg-transparent">
              {{ c.user.full_name }} · {{ c.transport_type|default:"—" }} · {{ c.payload_capacity_kg|default:"—" }} кг
            </li>
          {% empty %}
            <li class="list-group-item text-muted bg-transparent">Нет подходящих курьеров</li>
          {% endfor %}
        </ul>
      </div>
    </div>
    <div class="col-lg-8">
      <div class="card">
        <h6>Планирование доставки</h6>
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
            <a href="/logistics/" class="btn btn-outline-secondary">Отмена</a>
          </div>
        </form>
      </div>
      <div class="card mt-3">
        <h6>Маршрут и карта</h6>
        <div id="delivery-map" style="height: 320px;"></div>
        <div class="d-flex gap-3 mt-2 small text-muted">
          <div>Расстояние: <span id="route-distance">—</span></div>
          <div>Время: <span id="route-duration">—</span></div>
          <div>Альтернативы: <span id="route-alternatives">—</span></div>
        </div>
        <div class="mt-2">
          <a id="open-delivery-maps" class="link-muted" href="#" target="_blank" rel="noopener">Открыть в Google Maps</a>
        </div>
      </div>
    </div>
  </div>

  {{ delivery_map_payload|json_script:"delivery-map-data" }}
  <script>
    async function geocodeAddress(address) {
      const url = "https://nominatim.openstreetmap.org/search?format=json&q=" + encodeURIComponent(address);
      const res = await fetch(url, { headers: { "Accept-Language": "ru" } });
      const data = await res.json();
      if (!data.length) return null;
      return { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lon) };
    }

    function buildGoogleMapsLink(origin, destination) {
      if (!origin || !destination) return "#";
      const o = encodeURIComponent(origin);
      const d = encodeURIComponent(destination);
      return `https://www.google.com/maps/dir/?api=1&origin=${o}&destination=${d}`;
    }

    async function initDeliveryMap() {
      const payload = JSON.parse(document.getElementById("delivery-map-data").textContent || "{}");
      const mapEl = document.getElementById("delivery-map");
      if (!mapEl) return;
      const map = L.map(mapEl);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "&copy; OpenStreetMap",
      }).addTo(map);

      if (!payload.origin || !payload.destination) {
        map.setView([55.751244, 37.618423], 10);
        return;
      }

      const originPoint = await geocodeAddress(payload.origin);
      const destPoint = await geocodeAddress(payload.destination);
      if (originPoint && destPoint) {
        const latLngs = [
          [originPoint.lat, originPoint.lng],
          [destPoint.lat, destPoint.lng],
        ];
        L.marker([originPoint.lat, originPoint.lng]).addTo(map).bindPopup(payload.origin);
        L.marker([destPoint.lat, destPoint.lng]).addTo(map).bindPopup(payload.destination);
        L.polyline(latLngs, { color: "#3b82f6" }).addTo(map);
        map.fitBounds(latLngs, { padding: [30, 30] });
      } else {
        map.setView([55.751244, 37.618423], 10);
      }

      const link = document.getElementById("open-delivery-maps");
      if (link) link.href = buildGoogleMapsLink(payload.origin, payload.destination);
    }
  </script>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>initDeliveryMap();</script>
{% endblock %}
```

160. templates/logistics/form.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/logistics/">Доставки</a> / {{ title }}
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
        <a href="/logistics/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

161. templates/logistics/list.html
```html
{% extends "base.html" %}

{% block title %}Заказы на доставку{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}Заказы на доставку{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/logistic/">Кабинет логиста</a> / Доставки
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Заказы, требующие доставки</h4>
    <div class="d-flex gap-2">
      <a href="/logistics/routes/" class="btn btn-outline-secondary">Маршруты</a>
      <a href="/logistics/couriers/" class="btn btn-outline-secondary">Курьеры</a>
    </div>
  </div>

  <div class="card mb-3">
    <form class="filters" method="get">
      <select class="form-select" name="client">
        <option value="">Все клиенты</option>
        {% for c in clients %}
          <option value="{{ c.id }}" {% if request.GET.client == c.id|stringformat:"s" %}selected{% endif %}>
            {{ c.name }}
          </option>
        {% endfor %}
      </select>
      <select class="form-select" name="courier">
        <option value="">Все курьеры</option>
        {% for c in couriers %}
          <option value="{{ c.id }}" {% if request.GET.courier == c.id|stringformat:"s" %}selected{% endif %}>
            {{ c.user.full_name }}
          </option>
        {% endfor %}
      </select>
      <select class="form-select" name="route">
        <option value="">Все маршруты</option>
        {% for r in routes %}
          <option value="{{ r.id }}" {% if request.GET.route == r.id|stringformat:"s" %}selected{% endif %}>
            {{ r.planned_date|date:"d.m.Y" }}
          </option>
        {% endfor %}
      </select>
      <select class="form-select" name="status">
        <option value="">Все статусы</option>
        {% for value, label in status_choices %}
          <option value="{{ value }}" {% if request.GET.status == value %}selected{% endif %}>{{ label }}</option>
        {% endfor %}
      </select>
      <input class="form-control" type="date" name="date" value="{{ request.GET.date }}">
      <select class="form-select" name="sort">
        <option value="">Сортировка</option>
        <option value="planned_at" {% if request.GET.sort == "planned_at" %}selected{% endif %}>По плану ↑</option>
        <option value="-planned_at" {% if request.GET.sort == "-planned_at" %}selected{% endif %}>По плану ↓</option>
        <option value="status" {% if request.GET.sort == "status" %}selected{% endif %}>По статусу ↑</option>
        <option value="-status" {% if request.GET.sort == "-status" %}selected{% endif %}>По статусу ↓</option>
        <option value="client" {% if request.GET.sort == "client" %}selected{% endif %}>По клиенту A‑Я</option>
        <option value="-client" {% if request.GET.sort == "-client" %}selected{% endif %}>По клиенту Я‑A</option>
      </select>
      <button class="btn btn-outline-secondary" type="submit">Фильтр</button>
      {% if request.GET.urlencode %}
        <a class="btn btn-outline-secondary" href="/logistics/?{{ request.GET.urlencode }}&export=1">Экспорт</a>
      {% else %}
        <a class="btn btn-outline-secondary" href="/logistics/?export=1">Экспорт</a>
      {% endif %}
    </form>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Заказ</th>
            <th>Клиент</th>
            <th>Адрес</th>
            <th>План</th>
            <th>Курьер</th>
            <th>Маршрут</th>
            <th>Статус</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {% for d in deliveries %}
            <tr>
              <td>{{ d.order.order_number }}</td>
              <td>{{ d.order.client.name }}</td>
              <td>{{ d.address|default:"—" }}</td>
              <td>{{ d.planned_at|date:"d.m.Y H:i"|default:"—" }}</td>
              <td>{{ d.courier.user.full_name|default:"—" }}</td>
              <td>{{ d.route.planned_date|date:"d.m.Y"|default:"—" }}</td>
              <td>
                <span class="badge-soft {% if d.status == 'Доставлено' %}success{% elif d.status == 'Отменено' %}danger{% elif d.status == 'В пути' %}primary{% else %}warn{% endif %}">
                  {{ d.status }}
                </span>
              </td>
              <td class="text-end">
                <a class="btn btn-sm btn-outline-secondary" href="/logistics/delivery/{{ d.id }}/">Открыть</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="8" class="text-muted">Нет доставок</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <div class="card mt-3">
    <h6>Заказы без доставки</h6>
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Номер</th>
            <th>Клиент</th>
            <th>Сумма</th>
            <th>Статус заказа</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {% for o in orders_without_delivery %}
            <tr>
              <td>{{ o.order_number }}</td>
              <td>{{ o.client.name }}</td>
              <td>{{ o.total_amount }}</td>
              <td>{{ o.get_status_display }}</td>
              <td class="text-end">
                <a class="btn btn-sm btn-outline-secondary" href="/logistics/orders/{{ o.id }}/delivery/">Создать доставку</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="5" class="text-muted">Все заказы уже имеют доставку</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

162. templates/logistics/profile.html
```html
{% extends "base.html" %}

{% block title %}Профиль логиста{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}Профиль логиста{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/logistic/">Кабинет логиста</a> / Профиль
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Профиль логиста</h4>
  </div>

  <div class="row g-3">
    <div class="col-lg-5">
      <div class="card">
        <h6>Параметры работы</h6>
        <div class="small text-muted">Регион</div>
        <div class="fw-semibold mb-2">{{ profile.region|default:"—" }}</div>
        <div class="small text-muted">Город</div>
        <div class="fw-semibold mb-2">{{ profile.city|default:"—" }}</div>
        <div class="small text-muted">Часовой пояс</div>
        <div class="fw-semibold mb-2">{{ profile.timezone|default:"UTC" }}</div>
        <div class="small text-muted">Тип маршрута</div>
        <div class="fw-semibold mb-2">{{ profile.get_preferred_route_type_display }}</div>
        <div class="small text-muted">Пробки</div>
        <div class="fw-semibold">{{ profile.map_show_traffic|yesno:"Включены,Выключены" }}</div>
      </div>
    </div>
    <div class="col-lg-7">
      <div class="card">
        <h6>Настройки профиля</h6>
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
            <a href="/dashboard/logistic/" class="btn btn-outline-secondary">К обзору</a>
          </div>
        </form>
      </div>
    </div>
  </div>
{% endblock %}
```

163. templates/logistics/route_detail.html
```html
{% extends "base.html" %}

{% block title %}Маршрут{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}Маршрут{% endblock %}
{% block breadcrumbs %}
  <a href="/logistics/routes/">Маршруты</a> / Детали
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Маршрут на {{ route.planned_date|date:"d.m.Y" }}</h4>
    <a href="/logistics/routes/" class="btn btn-outline-secondary">Назад</a>
  </div>

  <div class="card mb-3">
    <div class="section-header">
      <h6 class="mb-0">Проверка маршрута</h6>
      <form method="post">
        {% csrf_token %}
        <input type="hidden" name="action" value="publish_route">
        <button class="btn btn-primary" {% if route_errors %}disabled{% endif %}>
          Опубликовать маршрут
        </button>
      </form>
    </div>
    <div class="row g-2">
      <div class="col-md-4">
        <div class="small text-muted">Прогноз времени</div>
        <div class="fw-semibold">{{ route_duration_minutes }} мин / {{ route.max_duration_minutes }} мин</div>
      </div>
      <div class="col-md-4">
        <div class="small text-muted">Километраж</div>
        <div class="fw-semibold">{{ route_distance_km }} км</div>
      </div>
      <div class="col-md-4">
        <div class="small text-muted">Количество точек</div>
        <div class="fw-semibold">{{ total_points }} / {{ route.soft_limit_stops }}</div>
      </div>
      <div class="col-md-4">
        <div class="small text-muted">Вес</div>
        <div class="fw-semibold">{{ total_weight }}</div>
      </div>
      <div class="col-md-4">
        <div class="small text-muted">Объём</div>
        <div class="fw-semibold">{{ total_volume }}</div>
      </div>
    </div>
    {% if route_errors %}
      <div class="mt-3">
        <div class="text-danger fw-semibold">Невалидно:</div>
        <ul class="mb-0">
          {% for e in route_errors %}
            <li>{{ e }}</li>
          {% endfor %}
        </ul>
      </div>
    {% endif %}
    {% if route_warnings %}
      <div class="mt-2">
        <div class="text-warning fw-semibold">Предупреждения:</div>
        <ul class="mb-0">
          {% for w in route_warnings %}
            <li>{{ w }}</li>
          {% endfor %}
        </ul>
      </div>
    {% endif %}
  </div>

  <div class="row g-3">
    <div class="col-lg-6">
      <div class="card">
        <h6>Назначенные курьеры</h6>
        <ul class="list-group list-group-flush mb-3">
          {% for a in assignments %}
            <li class="list-group-item bg-transparent">{{ a.courier.user.full_name }}</li>
          {% empty %}
            <li class="list-group-item text-muted bg-transparent">Курьеры не назначены</li>
          {% endfor %}
        </ul>
        <form method="post">
          {% csrf_token %}
          <input type="hidden" name="action" value="assign_courier">
          <div class="mb-2">{{ assign_form.courier }}</div>
          <button class="btn btn-outline-secondary w-100">Назначить курьера</button>
        </form>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="card">
        <h6>Добавить остановку</h6>
        <form method="post">
          {% csrf_token %}
          <input type="hidden" name="action" value="add_stop">
          <div class="mb-2">{{ stop_form.delivery }}</div>
          <div class="mb-2">{{ stop_form.planned_time }}</div>
          <div class="mb-2">{{ stop_form.note }}</div>
          <div class="mb-2">{{ stop_form.status }}</div>
          <button class="btn btn-primary w-100">Добавить</button>
        </form>
      </div>
    </div>
  </div>

  <div class="card mt-3">
    <h6>Остановки маршрута</h6>
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Порядок</th>
            <th>Заказ</th>
            <th>Адрес</th>
            <th>План</th>
            <th>Статус</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for s in stops %}
            <tr>
              <td>{{ s.sequence_index }}</td>
              <td>{{ s.delivery.order.order_number }}</td>
              <td>{{ s.delivery.address|default:"—" }}</td>
              <td>{{ s.planned_time|date:"d.m.Y H:i"|default:"—" }}</td>
              <td>
                <span class="badge-soft {% if s.status == 'Доставлено' %}success{% elif s.status == 'В пути' %}warn{% elif s.status == 'Не доставлено' %}danger{% else %}primary{% endif %}">
                  {{ s.status }}
                </span>
              </td>
              <td class="text-end">
                <form method="post" class="d-inline">
                  {% csrf_token %}
                  <input type="hidden" name="action" value="move_up">
                  <input type="hidden" name="stop_id" value="{{ s.id }}">
                  <button class="btn btn-sm btn-outline-secondary">↑</button>
                </form>
                <form method="post" class="d-inline">
                  {% csrf_token %}
                  <input type="hidden" name="action" value="move_down">
                  <input type="hidden" name="stop_id" value="{{ s.id }}">
                  <button class="btn btn-sm btn-outline-secondary">↓</button>
                </form>
                <form method="post" class="d-inline">
                  {% csrf_token %}
                  <input type="hidden" name="action" value="remove_stop">
                  <input type="hidden" name="stop_id" value="{{ s.id }}">
                  <input type="hidden" name="reason" value="Удалено логистом">
                  <button class="btn btn-sm btn-outline-secondary">Удалить</button>
                </form>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="6" class="text-muted">Остановок пока нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <div class="card mt-3">
    <h6>Карта маршрута</h6>
    <div id="route-map" style="height: 360px;"></div>
  </div>

  {{ map_payload|json_script:"route-data" }}
  <script>
    async function geocodeAddress(address) {
      const url = "https://nominatim.openstreetmap.org/search?format=json&q=" + encodeURIComponent(address);
      const res = await fetch(url, { headers: { "Accept-Language": "ru" } });
      const data = await res.json();
      if (!data.length) return null;
      return { lat: parseFloat(data[0].lat), lng: parseFloat(data[0].lon) };
    }

    async function initRouteMap() {
      const payload = JSON.parse(document.getElementById("route-data").textContent || "{}");
      const mapEl = document.getElementById("route-map");
      if (!mapEl) return;
      const map = L.map(mapEl);
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution: "&copy; OpenStreetMap",
      }).addTo(map);

      const points = [];
      for (const stop of payload.stops || []) {
        let point = null;
        if (stop.lat && stop.lng) {
          point = { lat: stop.lat, lng: stop.lng };
        } else if (stop.address) {
          point = await geocodeAddress(stop.address);
        }
        if (point) {
          points.push(point);
          L.marker([point.lat, point.lng]).addTo(map).bindPopup(stop.address || "Остановка");
        }
      }

      if (points.length) {
        const latLngs = points.map((p) => [p.lat, p.lng]);
        L.polyline(latLngs, { color: "#3b82f6" }).addTo(map);
        map.fitBounds(latLngs, { padding: [30, 30] });
      } else {
        map.setView([55.751244, 37.618423], 10);
      }
    }
  </script>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <script>initRouteMap();</script>
{% endblock %}
```

164. templates/logistics/route_form.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/logistics/routes/">Маршруты</a> / {{ title }}
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
        <a href="/logistics/routes/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

165. templates/logistics/routes.html
```html
{% extends "base.html" %}

{% block title %}Маршруты{% endblock %}
{% block sidebar %}{% include "partials/sidebars/logistic.html" %}{% endblock %}
{% block topbar_title %}Маршруты{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/logistic/">Кабинет логиста</a> / Маршруты
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Маршруты</h4>
    <a href="/logistics/routes/create/" class="btn btn-primary">Новый маршрут</a>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Дата</th>
            <th>Логист</th>
            <th>Статус</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for r in routes %}
            <tr>
              <td>{{ r.planned_date|date:"d.m.Y" }}</td>
              <td>{{ r.logistician.full_name|default:"—" }}</td>
              <td>{{ r.get_status_display }}</td>
              <td class="text-end">
                <a href="/logistics/routes/{{ r.id }}/" class="btn btn-sm btn-outline-secondary">Открыть</a>
                <a href="/logistics/routes/{{ r.id }}/edit/" class="btn btn-sm btn-outline-secondary">Изменить</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="4" class="text-muted">Маршруты не найдены</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

166. templates/manager/proof_review_list.html
```html
{% extends "base.html" %}

{% block title %}Проверка доставок{% endblock %}
{% block sidebar %}{% include "partials/sidebars/manager.html" %}{% endblock %}
{% block topbar_title %}Проверка доставок{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/manager/">Кабинет менеджера</a> / Проверка доставок
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Документы доставки</h4>
  </div>

  <div class="card mb-3">
    <form method="get" class="row g-2 align-items-end">
      <div class="col-md-4">
        <label class="form-label">Статус проверки</label>
        <select name="status" class="form-select">
          <option value="">Все</option>
          <option value="Ожидает проверки" {% if request.GET.status == 'Ожидает проверки' %}selected{% endif %}>Ожидает проверки</option>
          <option value="Подтверждено" {% if request.GET.status == 'Подтверждено' %}selected{% endif %}>Подтверждено</option>
          <option value="Отклонено" {% if request.GET.status == 'Отклонено' %}selected{% endif %}>Отклонено</option>
        </select>
      </div>
      <div class="col-md-4 d-flex gap-2">
        <button class="btn btn-primary">Применить</button>
        <a href="/logistics/manager/proofs/" class="btn btn-outline-secondary">Сбросить</a>
      </div>
    </form>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Маршрут</th>
            <th>Заказ</th>
            <th>Адрес</th>
            <th>Статус</th>
            <th>Документ</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for s in stops %}
            <tr>
              <td>{{ s.route.planned_date|date:"d.m.Y" }}</td>
              <td>{{ s.delivery.order.order_number }}</td>
              <td>{{ s.delivery.address|default:s.delivery.order.address|default:"—" }}</td>
              <td>{{ s.proof_review_status }}</td>
              <td>
                {% if s.proof_of_delivery %}
                  <a href="{{ s.proof_of_delivery.url }}" target="_blank">Открыть</a>
                {% else %}
                  —
                {% endif %}
              </td>
              <td class="text-end">
                <form method="post" action="/logistics/manager/proofs/{{ s.id }}/" class="d-inline">
                  {% csrf_token %}
                  <input type="hidden" name="action" value="approve">
                  <button class="btn btn-sm btn-outline-secondary">Подтвердить</button>
                </form>
                <form method="post" action="/logistics/manager/proofs/{{ s.id }}/" class="d-inline">
                  {% csrf_token %}
                  <input type="hidden" name="action" value="reject">
                  <input type="hidden" name="comment" value="Отклонено менеджером">
                  <button class="btn btn-sm btn-outline-secondary">Отклонить</button>
                </form>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="6" class="text-muted">Документов нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

167. templates/manager_clients.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Клиенты — Панель менеджера</title>
  <link rel="stylesheet" href="{% static 'manager.css' %}">
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <div class="logo">AC</div>
      <nav class="menu">
        <a class="menu-item active" href="/manager/clients/">Клиенты</a>
        <a class="menu-item" href="/manager/orders/">Заказы</a>
        <a class="menu-item" href="/manager/">Главная</a>
      </nav>
    </aside>
    <main class="content">
      <header class="topbar">
        <div class="breadcrumb">Клиенты</div>
        <div class="userbox">
          <span class="user-name">{{ request.user.full_name|default:request.user.username }}</span>
          <a class="logout" href="/logout/">Выйти</a>
        </div>
      </header>

      <section class="card">
        <div class="card-head">
          <div><h2>Список клиентов</h2><p class="muted">Создание, редактирование, удаление</p></div>
        </div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Название</th><th>Тип</th><th>Статус</th><th>Ответственный</th></tr></thead>
            <tbody>
              {% for c in clients %}
              <tr>
                <td>{{ c.name }}</td>
                <td>{{ c.get_client_type_display }}</td>
                <td>{{ c.get_status_display }}</td>
                <td>{{ c.responsible_manager|default:"—" }}</td>
              </tr>
              {% empty %}
              <tr><td colspan="4">Нет клиентов</td></tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </section>

      <section class="card">
        <div class="card-head"><h2>Добавить клиента</h2></div>
        <form method="post" class="form-grid">
          {% csrf_token %}
          {{ form.as_p }}
          <button class="btn primary" type="submit">Сохранить</button>
        </form>
      </section>
    </main>
  </div>
</body>
</html>
```

168. templates/manager_dashboard.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CRM — Панель менеджера</title>
  <link rel="stylesheet" href="{% static 'manager.css' %}">
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <div class="logo">AC</div>
      <nav class="menu">
        <a class="menu-item active" href="#clients">Клиенты</a>
        <a class="menu-item" href="#orders">Заказы</a>
        <a class="menu-item" href="#analytics">Аналитика</a>
        <a class="menu-item" href="#reports">Отчёты</a>
        <a class="menu-item" href="#archive">Архив заказов</a>
      </nav>
    </aside>

    <main class="content">
      <header class="topbar">
        <div class="breadcrumb">Панель менеджера</div>
        <div class="userbox">
          <span class="user-name">Менеджер</span>
          <a class="logout" href="/admin/logout/">Выйти</a>
        </div>
      </header>

      <section id="clients" class="card">
        <div class="card-head">
          <div>
            <h2>Клиенты</h2>
            <p class="muted">Поиск, фильтры, этапы сотрудничества</p>
          </div>
          <div class="actions">
            <input type="search" class="input" placeholder="Поиск клиента">
            <select class="input">
              <option>Все статусы</option>
              <option>Активен</option>
              <option>Переговоры</option>
              <option>Приостановлен</option>
            </select>
            <select class="input">
              <option>Все этапы</option>
              <option>Переговоры</option>
              <option>Тестовый заказ</option>
              <option>Регулярные поставки</option>
            </select>
            <a class="btn primary" href="/admin/crm/client/add/" target="_blank">Добавить клиента</a>
          </div>
        </div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>ФИО / Компания</th><th>Статус</th><th>Этап</th><th>Контакты</th><th></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Ирина Покупатель (Магазин «ВкусМаркет»)</td>
                <td><span class="badge success">Активен</span></td>
                <td>Регулярные поставки</td>
                <td>+7 903 111-22-33 · irina@vkusmarket.ru</td>
                <td class="row-actions">
                  <button class="link">Карточка</button>
                  <button class="link">Редактировать</button>
                  <button class="link danger">Удалить</button>
                </td>
              </tr>
              <tr>
                <td>Анна Бариста (Кафе «Брусника»)</td>
                <td><span class="badge warning">Переговоры</span></td>
                <td>Тестовый заказ</td>
                <td>+7 913 111-22-11 · anna@brusnika.cafe</td>
                <td class="row-actions">
                  <button class="link">Карточка</button>
                  <button class="link">Редактировать</button>
                  <button class="link danger">Удалить</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section id="orders" class="card">
        <div class="card-head">
          <div>
            <h2>Заказы</h2>
            <p class="muted">Создание, статусы, привязка к клиенту</p>
          </div>
          <div class="actions">
            <a class="btn primary" href="/admin/crm/order/add/" target="_blank">Создать заказ</a>
            <a class="btn ghost" href="#archive">Архив заказов</a>
          </div>
        </div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Номер</th><th>Клиент</th><th>Статус</th><th>Сумма</th><th></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>ORD-1003</td>
                <td>Маркет «Фреш»</td>
                <td><span class="badge success">Подтвержден</span></td>
                <td>7 850 ₽</td>
                <td class="row-actions"><button class="link">Редактировать</button></td>
              </tr>
              <tr>
                <td>ORD-1002</td>
                <td>Ресторан «Невский»</td>
                <td><span class="badge info">В производстве</span></td>
                <td>2 560 ₽</td>
                <td class="row-actions"><button class="link">Редактировать</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <section id="analytics" class="card grid-2">
        <div class="card-head">
          <div>
            <h2>Аналитика</h2>
            <p class="muted">Ключевые показатели</p>
          </div>
          <div class="actions">
            <input type="date" class="input">
            <input type="date" class="input">
            <button class="btn ghost" type="button">Фильтр</button>
          </div>
        </div>
        <div class="kpi-grid">
          <div class="kpi">
            <div class="kpi-title">Заказы (неделя)</div>
            <div class="kpi-value">42</div>
          </div>
          <div class="kpi">
            <div class="kpi-title">Конверсия</div>
            <div class="kpi-value">31%</div>
          </div>
          <div class="kpi">
            <div class="kpi-title">Выручка</div>
            <div class="kpi-value">1 240 000 ₽</div>
          </div>
          <div class="kpi">
            <div class="kpi-title">Средний чек</div>
            <div class="kpi-value">29 500 ₽</div>
          </div>
        </div>
      </section>

      <section id="reports" class="card">
        <div class="card-head">
          <div>
            <h2>Отчёты</h2>
            <p class="muted">Формирование и проверка данных</p>
          </div>
          <div class="actions">
            <button class="btn primary" type="button">Создать отчёт</button>
            <button class="btn ghost" type="button">Импорт</button>
          </div>
        </div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Название</th><th>Период</th><th>Статус</th><th></th></tr></thead>
            <tbody>
              <tr><td>Отчёт по выручке</td><td>Январь 2026</td><td><span class="badge info">Готов</span></td><td><button class="link">Открыть</button></td></tr>
              <tr><td>Отчёт по логистике</td><td>Январь 2026</td><td><span class="badge warning">Требует проверки</span></td><td><button class="link">Проверить</button></td></tr>
            </tbody>
          </table>
        </div>
      </section>

      <section id="archive" class="card">
        <div class="card-head">
          <div>
            <h2>Архив заказов</h2>
            <p class="muted">Завершённые и отменённые заказы</p>
          </div>
          <div class="actions">
            <input type="search" class="input" placeholder="Поиск по номеру">
            <button class="btn ghost" type="button">Фильтр</button>
          </div>
        </div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Номер</th><th>Клиент</th><th>Статус</th><th>Сумма</th></tr></thead>
            <tbody>
              <tr><td>ORD-0098</td><td>Магазин «ВкусМаркет»</td><td><span class="badge danger">Отменён</span></td><td>0 ₽</td></tr>
              <tr><td>ORD-0087</td><td>Кафе «Брусника»</td><td><span class="badge neutral">Архив</span></td><td>4 200 ₽</td></tr>
            </tbody>
          </table>
        </div>
      </section>
    </main>
  </div>
</body>
</html>
```

169. templates/manager_orders.html
```html
{% load static %}
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Заказы — Панель менеджера</title>
  <link rel="stylesheet" href="{% static 'manager.css' %}">
</head>
<body>
  <div class="layout">
    <aside class="sidebar">
      <div class="logo">AC</div>
      <nav class="menu">
        <a class="menu-item" href="/manager/clients/">Клиенты</a>
        <a class="menu-item active" href="/manager/orders/">Заказы</a>
        <a class="menu-item" href="/manager/">Главная</a>
      </nav>
    </aside>
    <main class="content">
      <header class="topbar">
        <div class="breadcrumb">Заказы</div>
        <div class="userbox">
          <span class="user-name">{{ request.user.full_name|default:request.user.username }}</span>
          <a class="logout" href="/logout/">Выйти</a>
        </div>
      </header>

      <section class="card">
        <div class="card-head">
          <div><h2>Список заказов</h2><p class="muted">Создание, изменение статусов</p></div>
        </div>
        <div class="table-wrap">
          <table>
            <thead><tr><th>Номер</th><th>Клиент</th><th>Статус</th><th>Сумма</th></tr></thead>
            <tbody>
              {% for o in orders %}
              <tr>
                <td>{{ o.order_number }}</td>
                <td>{{ o.client }}</td>
                <td>{{ o.get_status_display }}</td>
                <td>{{ o.total_amount }}</td>
              </tr>
              {% empty %}
              <tr><td colspan="4">Нет заказов</td></tr>
              {% endfor %}
            </tbody>
          </table>
        </div>
      </section>

      <section class="card">
        <div class="card-head"><h2>Создать заказ</h2></div>
        <form method="post" class="form-grid">
          {% csrf_token %}
          {{ form.as_p }}
          <button class="btn primary" type="submit">Сохранить</button>
        </form>
      </section>
    </main>
  </div>
</body>
</html>
```

170. templates/orders/archive.html
```html
{% extends "base.html" %}

{% block title %}Архив заказов{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Архив заказов{% endblock %}
{% block breadcrumbs %}
  <a href="/orders/">Заказы</a> / Архив
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Архив заказов</h4>
    <a href="/orders/" class="btn btn-outline-secondary">К активным</a>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Номер</th>
            <th>Клиент</th>
            <th>Статус</th>
            <th>Сумма</th>
            <th>Дата доставки</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for o in orders %}
            <tr>
              <td>{{ o.order_number }}</td>
              <td>{{ o.client.name }}</td>
              <td>
                <span class="badge-soft {% if o.status == 'Отменен' %}danger{% elif o.status == 'Отгружен' %}success{% elif o.status == 'Подтвержден производством' %}primary{% else %}warn{% endif %}">
                  {{ o.status }}
                </span>
              </td>
              <td>{{ o.total_amount }}</td>
              <td>{{ o.delivery_date|date:"d.m.Y"|default:"—" }}</td>
              <td class="text-end">
                <form method="post" action="/orders/{{ o.id }}/archive-toggle/" class="d-inline">
                  {% csrf_token %}
                  <button class="btn btn-sm btn-outline-secondary">Восстановить</button>
                </form>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="6" class="text-muted">Архив пуст</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

171. templates/orders/delete.html
```html
{% extends "base.html" %}

{% block title %}Удаление заказа{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Удаление заказа{% endblock %}
{% block breadcrumbs %}
  <a href="/orders/">Заказы</a> / Удаление
{% endblock %}

{% block content %}
  <div class="card">
    <h5>Удалить заказ «{{ object.order_number }}»?</h5>
    <p class="text-muted">Действие нельзя отменить.</p>
    <form method="post">
      {% csrf_token %}
      <button class="btn btn-danger">Удалить</button>
      <a href="/orders/" class="btn btn-outline-secondary">Отмена</a>
    </form>
  </div>
{% endblock %}
```

172. templates/orders/form.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/orders/">Заказы</a> / {{ title }}
{% endblock %}

{% block content %}
  <div class="card">
    <form method="post" novalidate data-order-id="{{ form.instance.pk|default_if_none:'' }}">
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
      {% if warnings %}
        <div class="mt-3">
          <div class="text-warning fw-semibold">Предупреждения</div>
          <ul class="mb-0">
            {% for w in warnings %}
              <li>{{ w }}</li>
            {% endfor %}
          </ul>
        </div>
      {% endif %}
      {% if info %}
        <div class="mt-3">
          <div class="fw-semibold">Подсказки производства</div>
          <div class="small text-muted">Доступно к производству: {{ info.production_capacity|default:"—" }} кг</div>
          <div class="small text-muted">Уже запланировано: {{ info.production_reserved|default:"—" }} кг</div>
          <div class="small text-muted">Вес текущего заказа: {{ info.order_weight|default:"—" }} кг</div>
          {% if info.client_daily_limit %}
            <div class="small text-muted">Лимит клиента: {{ info.client_daily_limit }} кг (занято {{ info.client_reserved }})</div>
          {% endif %}
          {% if info.ingredient_warnings %}
            <div class="mt-2 text-danger fw-semibold">Недостаточно ингредиентов</div>
            <div class="table-responsive">
              <table class="table table-sm mb-0">
                <thead>
                  <tr>
                    <th>Ингредиент</th>
                    <th>Нужно</th>
                    <th>Доступно</th>
                    <th>Зарезервировано</th>
                    <th>Не хватает</th>
                  </tr>
                </thead>
                <tbody>
                  {% for w in info.ingredient_warnings %}
                    <tr>
                      <td>{{ w.name }}</td>
                      <td>{{ w.required }}</td>
                      <td>{{ w.available }}</td>
                      <td>{{ w.reserved }}</td>
                      <td class="text-danger">{{ w.missing }}</td>
                    </tr>
                  {% endfor %}
                </tbody>
              </table>
            </div>
          {% endif %}
        </div>
      {% endif %}
      {% if formset %}
        <div class="mt-4">
          <h6>Позиции заказа</h6>
          <div class="text-muted small mb-2" id="delivery-hint">Сначала выберите дату доставки.</div>
          {{ formset.management_form }}
          <div class="table-responsive">
            <table class="table mb-0">
              <thead>
                <tr>
                  <th>Блюдо</th>
                  <th>Кол-во</th>
                  <th>Цена</th>
                  <th>Сумма</th>
                  <th>Тип</th>
                  <th>Комментарий</th>
                  <th></th>
                </tr>
              </thead>
              <tbody id="items-body">
                {% for f in formset %}
                  <tr class="item-row">
                    <td>{{ f.dish }}</td>
                    <td>
                      {{ f.quantity }}
                      <div class="small text-muted available-qty"></div>
                    </td>
                    <td>{{ f.unit_price }}</td>
                    <td><span class="line-total">—</span></td>
                    <td>{{ f.supply_type }}</td>
                    <td>{{ f.item_comment }}</td>
                    <td>
                      {% if f.DELETE %}
                        <label class="small">{{ f.DELETE }} Удалить</label>
                      {% endif %}
                    </td>
                  </tr>
                {% endfor %}
              </tbody>
            </table>
          </div>
          <div class="text-warning small mt-2" id="qty-warning" style="display:none"></div>
          <div class="text-danger small mt-2" id="price-warning" style="display:none"></div>
          <div class="mt-2">
            <button type="button" class="btn btn-outline-secondary" id="add-item">Добавить позицию</button>
          </div>
        </div>
      {% endif %}
      <div class="d-flex gap-2 mt-4">
        <button class="btn btn-primary">Сохранить</button>
        <a href="/orders/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>

  {% if dish_prices %}
    {{ dish_prices|json_script:"dish-price-data" }}
  {% endif %}

  {% if formset %}
    <template id="empty-form">
      <tr class="item-row">
        <td>{{ formset.empty_form.dish }}</td>
        <td>
          {{ formset.empty_form.quantity }}
          <div class="small text-muted available-qty"></div>
        </td>
        <td>{{ formset.empty_form.unit_price }}</td>
        <td><span class="line-total">—</span></td>
        <td>{{ formset.empty_form.supply_type }}</td>
        <td>{{ formset.empty_form.item_comment }}</td>
        <td></td>
      </tr>
    </template>
    <script>
      (function() {
        const addBtn = document.getElementById("add-item");
        const body = document.getElementById("items-body");
        const template = document.getElementById("empty-form");
        if (!addBtn || !body || !template) return;
        addBtn.addEventListener("click", () => {
          const totalInput = document.getElementById("id_form-TOTAL_FORMS");
          const index = parseInt(totalInput.value, 10);
          const html = template.innerHTML.replace(/__prefix__/g, index);
          body.insertAdjacentHTML("beforeend", html);
          totalInput.value = index + 1;
        });
      })();
    </script>
    <script>
      (function() {
        const body = document.getElementById("items-body");
        const dateInput = document.getElementById("id_delivery_date");
        const totalInput = document.getElementById("id_total_amount");
        const form = document.querySelector("form[data-order-id]");
        const warning = document.getElementById("qty-warning");
        const priceWarning = document.getElementById("price-warning");
        const hint = document.getElementById("delivery-hint");
        const addBtn = document.getElementById("add-item");
        let totalDisplay = null;
        const priceDataEl = document.getElementById("dish-price-data");
        const fallbackPrices = priceDataEl ? JSON.parse(priceDataEl.textContent) : {};
        if (!body) return;

        const dishCache = new Map();
        let lastDate = null;
        const moneyFormatter = new Intl.NumberFormat("ru-RU", { minimumFractionDigits: 2, maximumFractionDigits: 2 });

        function formatDateLocal(date) {
          const year = date.getFullYear();
          const month = String(date.getMonth() + 1).padStart(2, "0");
          const day = String(date.getDate()).padStart(2, "0");
          return `${year}-${month}-${day}`;
        }

        function getDeliveryDate() {
          if (dateInput && dateInput.value) {
            return dateInput.value;
          }
          return formatDateLocal(new Date());
        }

        function fetchPrices() {
          const deliveryDate = getDeliveryDate();
          if (deliveryDate === lastDate && dishCache.size) {
            return Promise.resolve();
          }
          lastDate = deliveryDate;
          dishCache.clear();
          const orderId = form && form.dataset.orderId ? form.dataset.orderId : "";
          const url = `/api/orders/availability/?delivery_date=${encodeURIComponent(deliveryDate)}${orderId ? `&order_id=${encodeURIComponent(orderId)}` : ""}`;
          return fetch(url, { headers: { "Accept": "application/json" } })
            .then((response) => {
              if (!response.ok) {
                throw new Error("Failed to load prices");
              }
              return response.json();
            })
            .then((data) => {
              (data.dishes || []).forEach((dish) => {
                if (!dish.dish_id) return;
                dishCache.set(String(dish.dish_id), {
                  price: dish.price,
                  availableQty: dish.available_qty,
                  unit: dish.unit,
                  baseUom: dish.base_uom,
                  quantityScale: dish.quantity_scale,
                  weightPerUnitKg: dish.weight_per_unit_kg,
                  dailyCapacity: dish.daily_capacity,
                  reservedQty: dish.reserved_qty,
                  maxByCapacity: dish.max_by_capacity,
                });
              });
            })
            .catch(() => {});
        }

        function setRowPrice(row, price) {
          const priceInput = row.querySelector('input[name$="-unit_price"]');
          if (!priceInput) return;
          if (price === null || price === undefined || !Number.isFinite(Number(price))) {
            priceInput.value = "";
            return;
          }
          priceInput.value = Number(price).toFixed(2);
        }

        function setAvailableQty(row, entry) {
          const container = row.querySelector(".available-qty");
          if (!container) return;
          if (!entry || entry.availableQty === null || entry.availableQty === undefined) {
            container.textContent = "";
            return;
          }
          const unit = entry.unit ? ` ${entry.unit}` : "";
          const scale = entry.quantityScale !== undefined ? entry.quantityScale : 3;
          container.textContent = `Доступно: ${formatQty(Number(entry.availableQty), scale)}${unit}`;
        }

        function parseNumber(value) {
          if (value === null || value === undefined) return null;
          const normalized = String(value).replace(",", ".").trim();
          if (!normalized) return null;
          const num = Number(normalized);
          return Number.isFinite(num) ? num : null;
        }

        function formatMoney(value) {
          if (value === null || value === undefined || !Number.isFinite(value)) return "—";
          return moneyFormatter.format(value);
        }

        function formatQty(value, scale) {
          if (value === null || value === undefined || !Number.isFinite(value)) return "—";
          const digits = Number.isFinite(scale) ? scale : 3;
          return value.toFixed(digits);
        }

        function showWarning(message) {
          if (!warning) return;
          if (!message) {
            warning.style.display = "none";
            warning.textContent = "";
            return;
          }
          warning.textContent = message;
          warning.style.display = "block";
        }

        function showPriceWarning(message) {
          if (!priceWarning) return;
          if (!message) {
            priceWarning.style.display = "none";
            priceWarning.textContent = "";
            return;
          }
          priceWarning.textContent = message;
          priceWarning.style.display = "block";
        }

        function setPositionsEnabled(enabled) {
          const inputs = body.querySelectorAll("select, input, textarea, button");
          inputs.forEach((el) => {
            if (enabled) {
              el.removeAttribute("disabled");
            } else {
              el.setAttribute("disabled", "disabled");
            }
          });
          if (addBtn) {
            if (enabled) {
              addBtn.removeAttribute("disabled");
            } else {
              addBtn.setAttribute("disabled", "disabled");
            }
          }
          if (hint) {
            hint.style.display = enabled ? "none" : "block";
          }
        }

        function applyQtyLimit(row, availableQty) {
          const qtyInput = row.querySelector('input[name$="-quantity"]');
          if (!qtyInput) return;
          if (availableQty === null || availableQty === undefined || !Number.isFinite(Number(availableQty))) {
            qtyInput.removeAttribute("max");
            showWarning("");
            return;
          }
          const maxValue = Number(availableQty);
          qtyInput.setAttribute("max", String(maxValue));
          const current = parseNumber(qtyInput.value);
          if (current !== null && current > maxValue) {
            const dishSelect = row.querySelector('select[name$="-dish"]');
            const entry = dishSelect ? dishCache.get(String(dishSelect.value)) : null;
            const scale = entry && entry.quantityScale !== undefined ? entry.quantityScale : 3;
            qtyInput.value = formatQty(maxValue, scale);
            showWarning(`Количество уменьшено до доступного: ${formatQty(maxValue, scale)}.`);
          } else {
            showWarning("");
          }
        }

        function updateLineTotal(row) {
          const qtyInput = row.querySelector('input[name$="-quantity"]');
          const priceInput = row.querySelector('input[name$="-unit_price"]');
          const display = row.querySelector(".line-total");
          if (!display) return 0;
          const qty = parseNumber(qtyInput ? qtyInput.value : null);
          const price = parseNumber(priceInput ? priceInput.value : null);
          if (qty === null || price === null) {
            display.textContent = price === null ? "Цена не задана" : "—";
            return 0;
          }
          const total = qty * price;
          display.textContent = formatMoney(total);
          return total;
        }

        function updateOrderTotal() {
          let total = 0;
          body.querySelectorAll("tr.item-row").forEach((row) => {
            total += updateLineTotal(row);
          });
          if (totalInput) {
            totalInput.value = Number.isFinite(total) ? total.toFixed(2) : "";
          }
          if (totalInput) {
            if (!totalDisplay) {
              totalDisplay = document.createElement("div");
              totalDisplay.className = "small text-muted";
              totalInput.parentElement && totalInput.parentElement.appendChild(totalDisplay);
            }
            totalDisplay.textContent = Number.isFinite(total) ? `Итого: ${formatMoney(total)}` : "";
          }
        }

        function configureQuantityInput(row, entry) {
          const qtyInput = row.querySelector('input[name$="-quantity"]');
          if (!qtyInput || !entry) return;
          if (entry.baseUom === "kg") {
            qtyInput.setAttribute("step", "0.001");
            qtyInput.setAttribute("inputmode", "decimal");
            qtyInput.setAttribute("pattern", "[0-9]+([.,][0-9]{1,3})?");
          } else {
            qtyInput.setAttribute("step", "1");
            qtyInput.setAttribute("inputmode", "numeric");
            qtyInput.setAttribute("pattern", "[0-9]*");
          }
        }

        function updateRow(row) {
          const dishSelect = row.querySelector('select[name$="-dish"]');
          if (!dishSelect || !dishSelect.value) return;
          const entry = dishCache.get(String(dishSelect.value));
          if (entry) {
            if (entry.price !== undefined) {
              setRowPrice(row, entry.price);
            }
            setAvailableQty(row, entry);
            applyQtyLimit(row, entry.availableQty);
            configureQuantityInput(row, entry);
          } else {
            setAvailableQty(row, null);
            applyQtyLimit(row, null);
            const fallback = fallbackPrices[dishSelect.value];
            if (fallback !== undefined) {
              setRowPrice(row, fallback);
            }
          }
          updateLineTotal(row);
          updateOrderTotal();
        }

        function refreshAllRows() {
          body.querySelectorAll("tr.item-row").forEach(updateRow);
          updateOrderTotal();
        }

        body.addEventListener("change", (event) => {
          const target = event.target;
          if (!target || target.tagName !== "SELECT" || !target.name.endsWith("-dish")) return;
          const row = target.closest("tr");
          fetchPrices().then(() => updateRow(row));
        });

        body.addEventListener("input", (event) => {
          const target = event.target;
          if (!target) return;
          if (target.name && (target.name.endsWith("-quantity") || target.name.endsWith("-unit_price"))) {
            const row = target.closest("tr");
            if (row) {
              const dishSelect = row.querySelector('select[name$="-dish"]');
              if (dishSelect && dishSelect.value) {
                const entry = dishCache.get(String(dishSelect.value));
                if (entry) {
                  if (target.name.endsWith("-quantity") && entry.baseUom !== "kg") {
                    if (target.value !== "") {
                      const sanitized = target.value.replace(/[^\d]/g, "");
                      if (sanitized !== target.value) {
                        target.value = sanitized;
                      }
                    }
                  }
                  applyQtyLimit(row, entry.availableQty);
                }
              }
              updateLineTotal(row);
              updateOrderTotal();
            }
          }
        });

        if (dateInput) {
          dateInput.addEventListener("change", () => {
            fetchPrices().then(() => {
              refreshAllRows();
              showWarning("Цены пересчитаны по новой дате.");
            });
          });
        }

        const hasDate = dateInput && dateInput.value;
        setPositionsEnabled(!!hasDate);
        if (hasDate) {
          fetchPrices().then(refreshAllRows);
        }

        if (dateInput) {
          dateInput.addEventListener("change", () => {
            const enabled = !!dateInput.value;
            setPositionsEnabled(enabled);
            if (enabled) {
              fetchPrices().then(refreshAllRows);
            } else {
              body.querySelectorAll(".line-total").forEach((el) => (el.textContent = "—"));
              if (totalInput) totalInput.value = "";
            }
          });
        }

        if (form) {
          form.addEventListener("submit", (event) => {
            let hasMissingPrice = false;
            body.querySelectorAll("tr.item-row").forEach((row) => {
              const dishSelect = row.querySelector('select[name$="-dish"]');
              const priceInput = row.querySelector('input[name$="-unit_price"]');
              if (dishSelect && dishSelect.value) {
                if (priceInput && !priceInput.value && fallbackPrices[dishSelect.value] !== undefined) {
                  setRowPrice(row, fallbackPrices[dishSelect.value]);
                }
                const price = parseNumber(priceInput ? priceInput.value : null);
                if (price === null) {
                  hasMissingPrice = true;
                }
              }
            });
            if (hasMissingPrice) {
              event.preventDefault();
              showPriceWarning("Цена не задана для одной или нескольких позиций. Сохранение невозможно.");
            } else {
              showPriceWarning("");
            }
          });
        }
      })();
    </script>
  {% endif %}
{% endblock %}
```

173. templates/orders/list.html
```html
{% extends "base.html" %}

{% block title %}Заказы{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Заказы{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/manager/">Кабинет менеджера</a> / Заказы / Список
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Заказы</h4>
    <a href="/orders/create/" class="btn btn-primary">Создать заказ</a>
  </div>

  <div class="card mb-3">
    <form class="filters" method="get">
      <input class="form-control" type="text" name="q" value="{{ request.GET.q }}" placeholder="Поиск по номеру">
      <select class="form-select" name="client">
        <option value="">Все клиенты</option>
        {% for c in clients %}
          <option value="{{ c.id }}" {% if request.GET.client == c.id|stringformat:"s" %}selected{% endif %}>{{ c.name }}</option>
        {% endfor %}
      </select>
      <select class="form-select" name="status">
        <option value="">Все статусы</option>
        {% for value, label in statuses %}
          <option value="{{ value }}" {% if request.GET.status == value %}selected{% endif %}>{{ label }}</option>
        {% endfor %}
      </select>
      <input class="form-control" type="date" name="from" value="{{ request.GET.from }}">
      <input class="form-control" type="date" name="to" value="{{ request.GET.to }}">
      <select class="form-select" name="sort">
        <option value="">Сортировка</option>
        <option value="created_at" {% if request.GET.sort == "created_at" %}selected{% endif %}>По дате ↑</option>
        <option value="-created_at" {% if request.GET.sort == "-created_at" %}selected{% endif %}>По дате ↓</option>
        <option value="order_number" {% if request.GET.sort == "order_number" %}selected{% endif %}>По номеру ↑</option>
        <option value="-order_number" {% if request.GET.sort == "-order_number" %}selected{% endif %}>По номеру ↓</option>
      </select>
      <button class="btn btn-outline-secondary" type="submit">Фильтр</button>
      <a href="/orders/archive/" class="btn btn-outline-secondary">Архив</a>
    </form>
  </div>

  <div class="card">
    <form method="post" action="/orders/bulk-delete/" id="bulk-delete-form">
      {% csrf_token %}
      <div class="d-flex justify-content-between align-items-center px-3 pt-3">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" id="select-all">
          <label class="form-check-label" for="select-all">Выбрать все</label>
        </div>
        <button class="btn btn-outline-danger btn-sm" id="bulk-delete-btn" disabled>Удалить выбранные</button>
      </div>
      <div class="table-responsive">
        <table class="table mb-0">
          <thead>
            <tr>
              <th style="width: 36px;"></th>
              <th>Номер</th>
              <th>Клиент</th>
              <th>Статус</th>
              <th>Сумма</th>
              <th>Дата доставки</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {% for o in orders %}
              <tr>
                <td>
                  <input class="form-check-input order-checkbox" type="checkbox" name="order_ids" value="{{ o.id }}">
                </td>
                <td>{{ o.order_number }}</td>
                <td>{{ o.client.name }}</td>
                <td>
                  <span class="badge-soft {% if o.status == 'Отменен' %}danger{% elif o.status == 'Отгружен' %}success{% elif o.status == 'Подтвержден производством' %}primary{% else %}warn{% endif %}">
                    {{ o.status }}
                  </span>
                </td>
                <td>{{ o.total_amount }}</td>
                <td>{{ o.delivery_date|date:"d.m.Y"|default:"—" }}</td>
                <td class="text-end">
                  <a class="btn btn-sm btn-outline-secondary" href="/orders/{{ o.id }}/edit/">Изменить</a>
                  <form method="post" action="/orders/{{ o.id }}/archive-toggle/" class="d-inline">
                    {% csrf_token %}
                    <button class="btn btn-sm btn-outline-secondary">В архив</button>
                  </form>
                  <a class="btn btn-sm btn-outline-danger" href="/orders/{{ o.id }}/delete/">Удалить</a>
                </td>
              </tr>
            {% empty %}
              <tr><td colspan="7" class="text-muted">Нет заказов</td></tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </form>
  </div>
{% endblock %}

{% block extra_js %}
  <script>
    (function () {
      const selectAll = document.getElementById("select-all");
      const checkboxes = Array.from(document.querySelectorAll(".order-checkbox"));
      const bulkBtn = document.getElementById("bulk-delete-btn");
      const form = document.getElementById("bulk-delete-form");

      function updateState() {
        const checkedCount = checkboxes.filter((c) => c.checked).length;
        bulkBtn.disabled = checkedCount === 0;
        selectAll.checked = checkedCount > 0 && checkedCount === checkboxes.length;
        selectAll.indeterminate = checkedCount > 0 && checkedCount < checkboxes.length;
      }

      if (selectAll) {
        selectAll.addEventListener("change", () => {
          checkboxes.forEach((c) => (c.checked = selectAll.checked));
          updateState();
        });
      }

      checkboxes.forEach((c) => c.addEventListener("change", updateState));
      updateState();

      if (form) {
        form.addEventListener("submit", (e) => {
          const checkedCount = checkboxes.filter((c) => c.checked).length;
          if (checkedCount === 0) {
            e.preventDefault();
            return;
          }
          if (!confirm(`Удалить выбранные заказы (${checkedCount})?`)) {
            e.preventDefault();
          }
        });
      }
    })();
  </script>
{% endblock %}
```

174. templates/orders/picker_detail.html
```html
{% extends "base.html" %}

{% block title %}Сборка заказа{% endblock %}
{% block sidebar %}{% include "partials/sidebars/picker.html" %}{% endblock %}
{% block topbar_title %}Сборка заказа{% endblock %}
{% block breadcrumbs %}
  <a href="/orders/picker/">Заказы в работе</a> / Сборка заказа
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Заказ №{{ order.order_number }}</h4>
    <div class="d-flex gap-2">
      <span class="badge-soft {% if order.status == 'Отменен' %}danger{% elif order.status == 'Отгружен' %}primary{% elif order.status == 'Подтвержден производством' %}success{% else %}warn{% endif %}">
        {{ order.status }}
      </span>
      <a href="/orders/picker/" class="btn btn-outline-secondary">К списку</a>
    </div>
  </div>

  <div class="row g-3 mb-3">
    <div class="col-lg-8">
      <div class="card">
        <h6>Данные заказа</h6>
        <div class="row g-3 mt-1">
          <div class="col-md-6"><strong>Клиент:</strong> {{ order.client.name }}</div>
          <div class="col-md-6"><strong>Дата:</strong> {{ order.created_at|date:"d.m.Y H:i" }}</div>
          <div class="col-md-6"><strong>Сумма:</strong> {{ order.total_amount }}</div>
          <div class="col-md-6"><strong>Адрес:</strong> {{ order.address|default:"—" }}</div>
          <div class="col-12"><strong>Комментарий клиента:</strong> {{ order.comments|default:"—" }}</div>
        </div>
      </div>
    </div>
    <div class="col-lg-4">
      <div class="card">
        <h6>История сборки</h6>
        <div class="small text-muted">Сборщик</div>
        <div class="fw-semibold mb-2">{{ session.picker.full_name|default:"—" }}</div>
        <div class="small text-muted">Начата</div>
        <div class="mb-2">{{ session.started_at|date:"d.m.Y H:i"|default:"—" }}</div>
        <div class="small text-muted">Завершена</div>
        <div class="mb-2">{{ session.finished_at|date:"d.m.Y H:i"|default:"—" }}</div>
      </div>
    </div>
  </div>

  <form method="post" novalidate>
    {% csrf_token %}
    {{ formset.management_form }}
    <div class="card mb-3">
      <h6>Позиции заказа</h6>
      <div class="table-responsive">
        <table class="table mb-0">
          <thead>
            <tr>
              <th>Позиция</th>
              <th>Заказано</th>
              <th>Собрано фактически</th>
              <th>Статус</th>
              <th>Комментарий</th>
              <th>Замена</th>
              <th>Действия</th>
            </tr>
          </thead>
          <tbody>
            {% for form in formset %}
              <tr>
                <td class="fw-semibold">{{ form.instance.display_name }}</td>
                <td>{{ form.instance.quantity }}</td>
                <td>{{ form.picked_quantity }}</td>
                <td>{{ form.item_status }}</td>
                <td>{{ form.item_comment }}</td>
                <td>{{ form.replacement_text }}</td>
                <td class="text-end">
                  <button type="button" class="btn btn-sm btn-outline-secondary" data-set-status="done" data-item="{{ forloop.counter0 }}">Собрано</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" data-set-status="out_of_stock" data-item="{{ forloop.counter0 }}">Нет в наличии</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" data-set-status="replaced" data-item="{{ forloop.counter0 }}">Замена</button>
                </td>
              </tr>
            {% empty %}
              <tr><td colspan="7" class="text-muted">Позиции не найдены</td></tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>

    <div class="card mb-3">
      <h6>Примечание сборщика</h6>
      {{ session_form.note }}
    </div>

    <div class="d-flex gap-2">
      <button class="btn btn-outline-secondary" name="action" value="save">Сохранить изменения</button>
      <button class="btn btn-primary" name="action" value="finish" onclick="return confirm('Завершить сборку и передать в доставку?');">
        Завершить сборку и передать в доставку
      </button>
    </div>
  </form>

  <script>
    const rows = Array.from(document.querySelectorAll("tbody tr"));
    rows.forEach((row, index) => {
      row.querySelectorAll("[data-set-status]").forEach((btn) => {
        btn.addEventListener("click", () => {
          const status = btn.getAttribute("data-set-status");
          const statusSelect = row.querySelector('select[name$="item_status"]');
          const pickedInput = row.querySelector('input[name$="picked_quantity"]');
          const ordered = row.children[1].textContent.trim();
          statusSelect.value = status;
          if (status === "done" && pickedInput && !pickedInput.value) {
            pickedInput.value = ordered;
          }
          if (status === "out_of_stock") {
            row.querySelector('input[name$="item_comment"]').focus();
          }
          if (status === "replaced") {
            row.querySelector('input[name$="replacement_text"]').focus();
          }
        });
      });
    });
  </script>
{% endblock %}
```

175. templates/orders/picker_list.html
```html
{% extends "base.html" %}

{% block title %}Заказы в работе{% endblock %}
{% block sidebar %}{% include "partials/sidebars/picker.html" %}{% endblock %}
{% block topbar_title %}Заказы в работе{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/picker/">Кабинет сборщика</a> / Заказы
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Заказы в работе</h4>
  </div>

  <div class="card mb-3">
    <form class="filters" method="get">
      <select class="form-select" name="status">
        <option value="">Все статусы</option>
        {% for value, label in statuses %}
          <option value="{{ value }}" {% if request.GET.status == value %}selected{% endif %}>{{ label }}</option>
        {% endfor %}
      </select>
      <input class="form-control" type="date" name="from" value="{{ request.GET.from }}">
      <input class="form-control" type="date" name="to" value="{{ request.GET.to }}">
      <button class="btn btn-outline-secondary" type="submit">Фильтр</button>
    </form>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Номер</th>
            <th>Клиент</th>
            <th>Сумма</th>
            <th>Статус</th>
            <th>Дата</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {% for o in orders %}
            <tr>
              <td><a href="/orders/picker/{{ o.id }}/" class="text-decoration-none">{{ o.order_number }}</a></td>
              <td>{{ o.client.name }}</td>
              <td>{{ o.total_amount }}</td>
              <td>
                <span class="badge-soft {% if o.status == 'Отменен' %}danger{% elif o.status == 'Отгружен' %}primary{% elif o.status == 'Подтвержден производством' %}success{% else %}warn{% endif %}">
                  {{ o.status }}
                </span>
              </td>
              <td>{{ o.delivery_date|date:"d.m.Y"|default:"—" }}</td>
              <td class="text-end">
                <a class="btn btn-sm btn-outline-secondary" href="/orders/picker/{{ o.id }}/">Открыть</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="6" class="text-muted">Нет заказов</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```

176. templates/partials/sidebars/admin.html
```html
<div class="logo">
  <i data-lucide="sparkles"></i>
  <span>Art Culinary CRM</span>
</div>
<div class="menu">
  <div class="menu-title">Система</div>
  <a href="/dashboard/admin/" class="{% if '/dashboard/admin/' in request.path %}active{% endif %}">
    <i data-lucide="layout-grid"></i>Обзор
  </a>
  <a href="/admin-panel/" class="{% if request.path == '/admin-panel/' %}active{% endif %}">
    <i data-lucide="settings"></i>Админ‑панель
  </a>
  <a href="/admin-panel/" class="{% if '/admin-panel/entities/' in request.path %}active{% endif %}">
    <i data-lucide="table-2"></i>Сущности
  </a>
  <a href="/admin-panel/users/" class="{% if '/admin-panel/users/' in request.path %}active{% endif %}">
    <i data-lucide="users"></i>Пользователи
  </a>
  <a href="/admin-panel/roles/" class="{% if '/admin-panel/roles/' in request.path %}active{% endif %}">
    <i data-lucide="shield"></i>Роли
  </a>
  <a href="/admin-panel/access/" class="{% if '/admin-panel/access/' in request.path %}active{% endif %}">
    <i data-lucide="lock"></i>Роли и доступы
  </a>
  <a href="/admin-panel/data-check/" class="{% if '/admin-panel/data-check/' in request.path %}active{% endif %}">
    <i data-lucide="check-square"></i>Проверка данных
  </a>
  <a href="/admin-panel/backups/" class="{% if '/admin-panel/backups/' in request.path %}active{% endif %}">
    <i data-lucide="database-backup"></i>Резервные копии
  </a>
  <div class="menu-title">Данные</div>
  <a href="/clients/" class="{% if '/clients/' in request.path %}active{% endif %}">
    <i data-lucide="users"></i>Клиенты
  </a>
  <a href="/orders/" class="{% if request.path == '/orders/' %}active{% endif %}">
    <i data-lucide="clipboard-list"></i>Заказы
  </a>
</div>
```

177. templates/partials/sidebars/courier.html
```html
<div class="logo">
  <i data-lucide="truck"></i>
  <span>Art Culinary CRM</span>
</div>
<div class="menu">
  <div class="menu-title">Курьер</div>
  <a href="/logistics/courier/profile/" class="{% if '/logistics/courier/profile/' in request.path %}active{% endif %}">
    <i data-lucide="user"></i>Профиль
  </a>
  <a href="/logistics/courier/routes/" class="{% if '/logistics/courier/routes/' in request.path %}active{% endif %}">
    <i data-lucide="route"></i>Маршруты
  </a>
</div>
```

178. templates/partials/sidebars/logistic.html
```html
<div class="logo">
  <i data-lucide="sparkles"></i>
  <span>Art Culinary CRM</span>
</div>
<div class="menu">
  <div class="menu-title">Логистика</div>
  <a href="/dashboard/logistic/" class="{% if '/dashboard/logistic/' in request.path %}active{% endif %}">
    <i data-lucide="layout-grid"></i>Обзор
  </a>
  <a href="/logistics/" class="{% if request.path == '/logistics/' %}active{% endif %}">
    <i data-lucide="truck"></i>Заказы на доставку
  </a>
  <a href="/logistics/routes/" class="{% if '/logistics/routes/' in request.path %}active{% endif %}">
    <i data-lucide="route"></i>Маршруты
  </a>
  <a href="/logistics/couriers/" class="{% if '/logistics/couriers/' in request.path %}active{% endif %}">
    <i data-lucide="user-check"></i>Курьеры
  </a>
  <a href="/logistics/profile/" class="{% if '/logistics/profile/' in request.path %}active{% endif %}">
    <i data-lucide="settings"></i>Профиль логиста
  </a>
</div>
```

179. templates/partials/sidebars/manager.html
```html
<div class="logo">
  <i data-lucide="sparkles"></i>
  <span>Art Culinary CRM</span>
</div>
<div class="menu">
  <div class="menu-title">Рабочий стол</div>
  <a href="/dashboard/manager/" class="{% if '/dashboard/manager/' in request.path %}active{% endif %}">
    <i data-lucide="layout-grid"></i>Обзор
  </a>
  <div class="menu-title">Продажи</div>
  <a href="/clients/" class="{% if '/clients/' in request.path %}active{% endif %}">
    <i data-lucide="users"></i>Клиенты
  </a>
  <a href="/orders/" class="{% if request.path == '/orders/' %}active{% endif %}">
    <i data-lucide="clipboard-list"></i>Заказы
  </a>
  <a href="/orders/archive/" class="{% if '/orders/archive/' in request.path %}active{% endif %}">
    <i data-lucide="archive"></i>Архив заказов
  </a>
  <a href="/reports/analytics/" class="{% if '/reports/analytics/' in request.path %}active{% endif %}">
    <i data-lucide="bar-chart-3"></i>Аналитика
  </a>
  <a href="/reports/" class="{% if '/reports/' in request.path and '/reports/analytics/' not in request.path %}active{% endif %}">
    <i data-lucide="file-text"></i>Отчёты
  </a>
  <a href="/logistics/manager/proofs/" class="{% if '/logistics/manager/proofs/' in request.path %}active{% endif %}">
    <i data-lucide="file-check-2"></i>Проверка доставок
  </a>
</div>
```

180. templates/partials/sidebars/picker.html
```html
<div class="logo">
  <i data-lucide="sparkles"></i>
  <span>Art Culinary CRM</span>
</div>
<div class="menu">
  <div class="menu-title">Производство</div>
  <a href="/dashboard/picker/" class="{% if '/dashboard/picker/' in request.path %}active{% endif %}">
    <i data-lucide="layout-grid"></i>Обзор
  </a>
  <a href="/orders/picker/" class="{% if '/orders/picker/' in request.path %}active{% endif %}">
    <i data-lucide="clipboard-check"></i>Заказы в работе
  </a>
</div>
```

181. templates/portal/base_portal.html
```html
{% load static %}
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>{% block title %}CRM{% endblock %}</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'login_root.css' %}">
</head>
<body class="bg-light">
  <nav class="navbar navbar-expand navbar-light bg-white border-bottom mb-3">
    <div class="container-fluid">
      <a class="navbar-brand fw-bold" href="/manager/">Art Culinary CRM</a>
      <div class="d-flex align-items-center gap-3">
        {% if request.user.is_authenticated %}
          <span class="text-muted">{{ request.user.username }}</span>
          <a class="btn btn-outline-secondary btn-sm" href="/logout/">Выйти</a>
        {% endif %}
      </div>
    </div>
  </nav>
  <div class="container py-3">
    {% block content %}{% endblock %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

182. templates/portal/client_form.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}{{ title }}{% endblock %}
{% block content %}
<h3 class="mb-3">{{ title }}</h3>
<form method="post" class="card card-body shadow-sm">
  {% csrf_token %}
  {{ form.non_field_errors }}
  {% for field in form %}
    <div class="mb-3">
      <label class="form-label">{{ field.label }}</label>
      {{ field }}
      {% if field.errors %}<div class="text-danger small">{{ field.errors|join:", " }}</div>{% endif %}
    </div>
  {% endfor %}
  <button class="btn btn-primary">Сохранить</button>
</form>
{% endblock %}
```

183. templates/portal/clients_list.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}Клиенты{% endblock %}
{% block content %}
<h3 class="mb-3">Клиенты</h3>
<form class="row g-2 mb-3" method="get">
  <div class="col-md-4"><input name="q" value="{{ request.GET.q }}" class="form-control" placeholder="Поиск"></div>
  <div class="col-md-3"><input name="status" value="{{ request.GET.status }}" class="form-control" placeholder="Статус"></div>
  <div class="col-md-2"><button class="btn btn-secondary w-100">Фильтр</button></div>
  <div class="col-md-3 text-end"><a class="btn btn-primary" href="/manager/clients/create/">Добавить клиента</a></div>
</form>
<table class="table table-hover align-middle">
  <thead><tr><th>Название</th><th>Статус</th><th>Этап</th><th>Ответственный</th><th></th></tr></thead>
  <tbody>
  {% for c in clients %}
    <tr>
      <td>{{ c.name }}</td>
      <td>{{ c.status }}</td>
      <td>{{ c.stage }}</td>
      <td>{{ c.responsible|default:"—" }}</td>
      <td class="text-end">
        <a class="btn btn-sm btn-outline-primary" href="/manager/clients/{{ c.id }}/edit/">Редактировать</a>
      </td>
    </tr>
  {% empty %}<tr><td colspan="5">Нет данных</td></tr>{% endfor %}
  </tbody>
</table>
{% endblock %}
```

184. templates/portal/delivery_plan.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}Планирование доставки{% endblock %}
{% block content %}
<h3 class="mb-3">Планирование доставки для {{ delivery.order.order_number }}</h3>
<form method="post" class="card card-body shadow-sm">
  {% csrf_token %}
  {{ form.non_field_errors }}
  {% for field in form %}
    <div class="mb-3">
      <label class="form-label">{{ field.label }}</label>
      {{ field }}
      {% if field.errors %}<div class="text-danger small">{{ field.errors|join:", " }}</div>{% endif %}
    </div>
  {% endfor %}
  <button class="btn btn-primary">Сохранить</button>
</form>
{% endblock %}
```

185. templates/portal/login.html
```html
{% load static %}
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <title>Вход в CRM</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'login_root.css' %}">
</head>
<body class="bg-light">
  <div class="root-login">
    <div class="login-card">
      <div class="logo">AC</div>
      <h1>Art Culinary CRM</h1>
      <p class="subtitle">Авторизация для роли менеджера</p>
      {% if messages %}
        {% for m in messages %}<div class="alert alert-danger py-2 mb-2">{{ m }}</div>{% endfor %}
      {% endif %}
      <form method="post" action="/login/">
        {% csrf_token %}
        <label for="id_username">Электронная почта</label>
        <input type="text" id="id_username" name="username" autocomplete="username" required>
        <label for="id_password">Пароль</label>
        <input type="password" id="id_password" name="password" autocomplete="current-password" required>
        <button type="submit" class="btn primary">Войти</button>
      </form>
    </div>
  </div>
</body>
</html>
```

186. templates/portal/logistic_dashboard.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}Кабинет логиста{% endblock %}
{% block content %}
<h3 class="mb-3">Кабинет логиста</h3>
<table class="table table-hover">
  <thead><tr><th>Заказ</th><th>Курьер</th><th>Отправление</th><th>Доставка</th><th>Адрес</th><th></th></tr></thead>
  <tbody>
    {% for d in deliveries %}
    <tr>
      <td>{{ d.order.order_number }}</td>
      <td>{{ d.courier|default:"—" }}</td>
      <td>{{ d.departure_time|default:"—" }}</td>
      <td>{{ d.delivered_at|default:"—" }}</td>
      <td>{{ d.address }}</td>
      <td><a class="btn btn-sm btn-outline-primary" href="/logistic/delivery/{{ d.id }}/">Изменить</a></td>
    </tr>
    {% empty %}<tr><td colspan="6">Нет доставок</td></tr>{% endfor %}
  </tbody>
</table>
{% endblock %}
```

187. templates/portal/manager_dashboard.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}Панель менеджера{% endblock %}
{% block content %}
<div class="row g-3 mb-3">
  <div class="col-md-4">
    <div class="card shadow-sm"><div class="card-body">
      <div class="text-muted">Клиенты</div>
      <div class="fs-3 fw-bold">{{ stats.clients }}</div>
    </div></div>
  </div>
  <div class="col-md-4">
    <div class="card shadow-sm"><div class="card-body">
      <div class="text-muted">Заказы</div>
      <div class="fs-3 fw-bold">{{ stats.orders }}</div>
    </div></div>
  </div>
  <div class="col-md-4">
    <div class="card shadow-sm"><div class="card-body">
      <div class="text-muted">Активные</div>
      <div class="fs-3 fw-bold">{{ stats.active_orders }}</div>
    </div></div>
  </div>
</div>
<div class="d-flex gap-2">
  <a class="btn btn-primary" href="/manager/clients/">Клиенты</a>
  <a class="btn btn-outline-primary" href="/manager/orders/">Заказы</a>
</div>
{% endblock %}
```

188. templates/portal/order_form.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}{{ title }}{% endblock %}
{% block content %}
<h3 class="mb-3">{{ title }}</h3>
<form method="post" class="card card-body shadow-sm">
  {% csrf_token %}
  {{ form.non_field_errors }}
  {% for field in form %}
    <div class="mb-3">
      <label class="form-label">{{ field.label }}</label>
      {{ field }}
      {% if field.errors %}<div class="text-danger small">{{ field.errors|join:", " }}</div>{% endif %}
    </div>
  {% endfor %}
  <button class="btn btn-primary">Сохранить</button>
</form>
{% endblock %}
```

189. templates/portal/orders_list.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}Заказы{% endblock %}
{% block content %}
<h3 class="mb-3">Заказы</h3>
<form class="row g-2 mb-3" method="get">
  <div class="col-md-4"><input name="q" value="{{ request.GET.q }}" class="form-control" placeholder="Поиск по номеру"></div>
  <div class="col-md-3"><input name="status" value="{{ request.GET.status }}" class="form-control" placeholder="Статус"></div>
  <div class="col-md-2"><button class="btn btn-secondary w-100">Фильтр</button></div>
  <div class="col-md-3 text-end"><a class="btn btn-primary" href="/manager/orders/create/">Создать заказ</a></div>
</form>
<table class="table table-hover align-middle">
  <thead><tr><th>Номер</th><th>Клиент</th><th>Статус</th><th>Сумма</th><th></th></tr></thead>
  <tbody>
  {% for o in orders %}
    <tr>
      <td>{{ o.order_number }}</td>
      <td>{{ o.client }}</td>
      <td>{{ o.status }}</td>
      <td>{{ o.total_amount }}</td>
      <td class="text-end"><a class="btn btn-sm btn-outline-primary" href="/manager/orders/{{ o.id }}/edit/">Редактировать</a></td>
    </tr>
  {% empty %}<tr><td colspan="5">Нет данных</td></tr>{% endfor %}
  </tbody>
</table>
{% endblock %}
```

190. templates/portal/picker_dashboard.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}Кабинет сборщика{% endblock %}
{% block content %}
<h3 class="mb-3">Кабинет сборщика заказов</h3>
<table class="table table-hover">
  <thead><tr><th>Номер</th><th>Клиент</th><th>Статус</th><th></th></tr></thead>
  <tbody>
    {% for o in orders %}
    <tr>
      <td>{{ o.order_number }}</td>
      <td>{{ o.client }}</td>
      <td>{{ o.get_status_display }}</td>
      <td><a class="btn btn-sm btn-outline-primary" href="/picker/orders/{{ o.id }}/status/">Изменить статус</a></td>
    </tr>
    {% empty %}<tr><td colspan="4">Нет заказов</td></tr>{% endfor %}
  </tbody>
</table>
{% endblock %}
```

191. templates/portal/sysadmin_dashboard.html
```html
{% extends "portal/base_portal.html" %}
{% block title %}Администратор системы{% endblock %}
{% block content %}
<h3 class="mb-3">Администратор системы</h3>
<p class="text-muted">Здесь будет управление пользователями, ролями, резервным копированием и проверкой данных.</p>
<div class="alert alert-info">Добавьте нужные действия: CRUD пользователей/ролей, бэкапы, проверки связей.</div>
{% endblock %}
```

192. templates/registration/login.html
```html
{% extends "admin/base_site.html" %}
{% load i18n static %}

{% block title %}Вход в CRM{% endblock %}

{% block content %}
<div class="login-hero light-login">
  <div class="login-card clean">
    <div class="login-header clean">
      <div class="login-logo clean">AC</div>
      <div class="login-titles clean">
        <h1>Art Culinary CRM</h1>
        <p class="login-subtitle">Авторизация в системе</p>
      </div>
    </div>
    <form action="{% url 'admin:login' %}" method="post" id="login-form">
      {% csrf_token %}
      {% if form.errors %}
        <p class="errornote">Пожалуйста, исправьте ошибки ниже.</p>
      {% endif %}
      <div class="form-row">
        <label for="id_username">Электронная почта</label>
        {{ form.username }}
      </div>
      <div class="form-row">
        <label for="id_password">Пароль</label>
        {{ form.password }}
      </div>
      <div class="form-actions stacked">
        <button type="submit" class="button default button-wide">Войти</button>
        <a class="link-muted" href="#">Забыли пароль?</a>
      </div>
      {% if form.non_field_errors %}
        {{ form.non_field_errors }}
      {% endif %}
    </form>
  </div>
</div>
{% endblock %}
```

193. templates/reports/analytics.html
```html
{% extends "base.html" %}

{% block title %}Аналитика{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Аналитика{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/manager/">Кабинет менеджера</a> / Аналитика
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Аналитика</h4>
  </div>

  <div class="card mb-3">
    <form class="filters" method="get">
      <input class="form-control" type="date" name="from" value="{{ request.GET.from }}">
      <input class="form-control" type="date" name="to" value="{{ request.GET.to }}">
      <select class="form-select" name="status">
        <option value="">Все статусы</option>
        {% for value, label in statuses %}
          <option value="{{ value }}" {% if request.GET.status == value %}selected{% endif %}>{{ label }}</option>
        {% endfor %}
      </select>
      <select class="form-select" name="client">
        <option value="">Все клиенты</option>
        {% for c in clients %}
          <option value="{{ c.id }}" {% if request.GET.client == c.id|stringformat:"s" %}selected{% endif %}>{{ c.name }}</option>
        {% endfor %}
      </select>
      <button class="btn btn-outline-secondary" type="submit">Показать</button>
      <a class="btn btn-primary" href="/reports/create/?from={{ request.GET.from }}&to={{ request.GET.to }}">Сформировать отчёт</a>
    </form>
  </div>

  <div class="row g-3 mb-3">
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ total_orders }}</div>
        <div class="kpi-label">Заказов за период</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ revenue }}</div>
        <div class="kpi-label">Выручка</div>
      </div>
    </div>
    <div class="col-md-4">
      <div class="card kpi-card">
        <div class="kpi-value">{{ avg_check }}</div>
        <div class="kpi-label">Средний чек</div>
      </div>
    </div>
  </div>

  <div class="card mb-3">
    <div class="section-header">
      <h6 class="mb-0">Заказы по статусам</h6>
      <div class="d-flex gap-2">
        <button class="btn btn-outline-secondary btn-sm" id="download-status-chart">Скачать график</button>
        <button class="btn btn-outline-secondary btn-sm" id="download-status-table">Скачать таблицу</button>
      </div>
    </div>
    <canvas id="statusChart" height="120"></canvas>
    <div class="table-responsive mt-3">
      <table class="table mb-0" id="statusTable">
        <thead>
          <tr>
            <th>Статус</th>
            <th>Количество</th>
          </tr>
        </thead>
        <tbody>
          {% for row in by_status %}
            <tr>
              <td>{{ row.label }}</td>
              <td>{{ row.cnt }}</td>
            </tr>
          {% empty %}
            <tr><td colspan="2" class="text-muted">Нет данных</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <div class="card">
    <div class="section-header">
      <h6 class="mb-0">Динамика заказов</h6>
      <div class="d-flex gap-2">
        <button class="btn btn-outline-secondary btn-sm" id="download-orders-chart">Скачать график</button>
        <button class="btn btn-outline-secondary btn-sm" id="download-orders-table">Скачать таблицу</button>
      </div>
    </div>
    <canvas id="ordersChart" height="140"></canvas>
    <div class="table-responsive mt-3">
      <table class="table mb-0" id="ordersTable">
        <thead>
          <tr>
            <th>Дата</th>
            <th>Заказы</th>
          </tr>
        </thead>
        <tbody>
          {% for row in by_day %}
            <tr>
              <td>{{ row.day }}</td>
              <td>{{ row.cnt }}</td>
            </tr>
          {% empty %}
            <tr><td colspan="2" class="text-muted">Нет данных</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <div class="card mt-3">
    <div class="section-header">
      <h6 class="mb-0">Динамика выручки</h6>
      <div class="d-flex gap-2">
        <button class="btn btn-outline-secondary btn-sm" id="download-revenue-chart">Скачать график</button>
        <button class="btn btn-outline-secondary btn-sm" id="download-revenue-table">Скачать таблицу</button>
      </div>
    </div>
    <canvas id="revenueChart" height="140"></canvas>
    <div class="table-responsive mt-3">
      <table class="table mb-0" id="revenueTable">
        <thead>
          <tr>
            <th>Дата</th>
            <th>Выручка</th>
          </tr>
        </thead>
        <tbody>
          {% for row in by_day %}
            <tr>
              <td>{{ row.day }}</td>
              <td>{{ row.revenue }}</td>
            </tr>
          {% empty %}
            <tr><td colspan="2" class="text-muted">Нет данных</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <div class="card mt-3">
    <div class="section-header">
      <h6 class="mb-0">Средний чек по дням</h6>
      <div class="d-flex gap-2">
        <button class="btn btn-outline-secondary btn-sm" id="download-avg-chart">Скачать график</button>
        <button class="btn btn-outline-secondary btn-sm" id="download-avg-table">Скачать таблицу</button>
      </div>
    </div>
    <canvas id="avgChart" height="140"></canvas>
    <div class="table-responsive mt-3">
      <table class="table mb-0" id="avgTable">
        <thead>
          <tr>
            <th>Дата</th>
            <th>Средний чек</th>
          </tr>
        </thead>
        <tbody>
          {% for row in avg_check_by_day %}
            <tr>
              <td>{{ row.day }}</td>
              <td>{{ row.avg_check }}</td>
            </tr>
          {% empty %}
            <tr><td colspan="2" class="text-muted">Нет данных</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  <div class="card mt-3">
    <div class="section-header">
      <h6 class="mb-0">Топ‑10 клиентов по выручке</h6>
      <div class="d-flex gap-2">
        <button class="btn btn-outline-secondary btn-sm" id="download-client-chart">Скачать график</button>
        <button class="btn btn-outline-secondary btn-sm" id="download-client-table">Скачать таблицу</button>
      </div>
    </div>
    <canvas id="clientChart" height="140"></canvas>
    <div class="table-responsive mt-3">
      <table class="table mb-0" id="clientTable">
        <thead>
          <tr>
            <th>Клиент</th>
            <th>Заказы</th>
            <th>Выручка</th>
          </tr>
        </thead>
        <tbody>
          {% for row in by_client %}
            <tr>
              <td>{{ row.client }}</td>
              <td>{{ row.cnt }}</td>
              <td>{{ row.revenue }}</td>
            </tr>
          {% empty %}
            <tr><td colspan="3" class="text-muted">Нет данных</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>

  {{ by_status|json_script:"status-data" }}
  {{ by_day|json_script:"day-data" }}
  {{ avg_check_by_day|json_script:"avg-data" }}
  {{ by_client|json_script:"client-data" }}
  {{ by_client_type|json_script:"client-type-data" }}
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <script>
    (function() {
      const statusData = JSON.parse(document.getElementById("status-data").textContent || "[]");
      const dayData = JSON.parse(document.getElementById("day-data").textContent || "[]");
      const avgData = JSON.parse(document.getElementById("avg-data").textContent || "[]");
      const clientData = JSON.parse(document.getElementById("client-data").textContent || "[]");
      const clientTypeData = JSON.parse(document.getElementById("client-type-data").textContent || "[]");

      const statusCtx = document.getElementById("statusChart").getContext("2d");
      const statusChart = new Chart(statusCtx, {
        type: "bar",
        data: {
          labels: statusData.map((r) => r.label),
          datasets: [{
            label: "Количество",
            data: statusData.map((r) => r.cnt),
            backgroundColor: "#3b82f6",
          }],
        },
        options: { responsive: true },
      });

      const ordersCtx = document.getElementById("ordersChart").getContext("2d");
      const ordersChart = new Chart(ordersCtx, {
        type: "line",
        data: {
          labels: dayData.map((r) => r.day),
          datasets: [
            { label: "Заказы", data: dayData.map((r) => r.cnt), borderColor: "#3b82f6" },
          ],
        },
        options: { responsive: true },
      });

      const revenueCtx = document.getElementById("revenueChart").getContext("2d");
      const revenueChart = new Chart(revenueCtx, {
        type: "line",
        data: {
          labels: dayData.map((r) => r.day),
          datasets: [
            { label: "Выручка", data: dayData.map((r) => r.revenue), borderColor: "#22c55e" },
          ],
        },
        options: { responsive: true },
      });

      const avgCtx = document.getElementById("avgChart").getContext("2d");
      const avgChart = new Chart(avgCtx, {
        type: "line",
        data: {
          labels: avgData.map((r) => r.day),
          datasets: [
            { label: "Средний чек", data: avgData.map((r) => r.avg_check), borderColor: "#a855f7" },
          ],
        },
        options: { responsive: true },
      });

      function downloadChart(chart, filename) {
        const link = document.createElement("a");
        link.href = chart.toBase64Image();
        link.download = filename;
        link.click();
      }

      function downloadTable(tableId, filename) {
        const table = document.getElementById(tableId);
        if (!table) return;
        const rows = Array.from(table.querySelectorAll("tr"));
        const csv = rows.map((row) => {
          const cols = Array.from(row.querySelectorAll("th,td")).map((c) => `"${c.textContent.trim()}"`);
          return cols.join(",");
        }).join("\n");
        const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = filename;
        link.click();
      }

      document.getElementById("download-status-chart").addEventListener("click", () => downloadChart(statusChart, "status-chart.png"));
      document.getElementById("download-orders-chart").addEventListener("click", () => downloadChart(ordersChart, "orders-chart.png"));
      document.getElementById("download-revenue-chart").addEventListener("click", () => downloadChart(revenueChart, "revenue-chart.png"));
      document.getElementById("download-avg-chart").addEventListener("click", () => downloadChart(avgChart, "avg-chart.png"));
      document.getElementById("download-status-table").addEventListener("click", () => downloadTable("statusTable", "status-table.csv"));
      document.getElementById("download-orders-table").addEventListener("click", () => downloadTable("ordersTable", "orders-table.csv"));
      document.getElementById("download-revenue-table").addEventListener("click", () => downloadTable("revenueTable", "revenue-table.csv"));
      document.getElementById("download-avg-table").addEventListener("click", () => downloadTable("avgTable", "avg-table.csv"));

      const clientEl = document.getElementById("clientChart");
      if (clientEl) {
        const clientCtx = clientEl.getContext("2d");
        const clientChart = new Chart(clientCtx, {
          type: "bar",
          data: {
            labels: clientData.map((r) => r.client),
            datasets: [{
              label: "Выручка",
              data: clientData.map((r) => r.revenue),
              backgroundColor: "#f97316",
            }],
          },
          options: { responsive: true },
        });
        document.getElementById("download-client-chart").addEventListener("click", () => downloadChart(clientChart, "client-chart.png"));
        document.getElementById("download-client-table").addEventListener("click", () => downloadTable("clientTable", "client-table.csv"));
      }
    })();
  </script>
{% endblock %}
```

194. templates/reports/form.html
```html
{% extends "base.html" %}

{% block title %}{{ title }}{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}{{ title }}{% endblock %}
{% block breadcrumbs %}
  <a href="/reports/">Отчёты</a> / {{ title }}
{% endblock %}

{% block content %}
  <div class="card">
    <form method="post" enctype="multipart/form-data" novalidate>
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
        <a href="/reports/" class="btn btn-outline-secondary">Отмена</a>
      </div>
    </form>
  </div>
{% endblock %}
```

195. templates/reports/list.html
```html
{% extends "base.html" %}

{% block title %}Отчёты{% endblock %}
{% block sidebar %}
  {% if is_admin %}
    {% include "partials/sidebars/admin.html" %}
  {% else %}
    {% include "partials/sidebars/manager.html" %}
  {% endif %}
{% endblock %}
{% block topbar_title %}Отчёты{% endblock %}
{% block breadcrumbs %}
  <a href="/dashboard/manager/">Кабинет менеджера</a> / Отчёты / Список
{% endblock %}

{% block content %}
  <div class="section-header">
    <h4 class="mb-0">Отчёты</h4>
    <div class="d-flex gap-2">
      <a href="/reports/create/" class="btn btn-primary">Создать отчёт</a>
      <a href="/reports/create/" class="btn btn-outline-secondary">Импортировать</a>
    </div>
  </div>

  <div class="card">
    <div class="table-responsive">
      <table class="table mb-0">
        <thead>
          <tr>
            <th>Название</th>
            <th>Период</th>
            <th>Статус</th>
            <th>Проверка</th>
            <th>Файл</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {% for r in reports %}
            <tr>
              <td>{{ r.title }}</td>
              <td>{{ r.period_from|date:"d.m.Y" }} – {{ r.period_to|date:"d.m.Y" }}</td>
              <td>
                <span class="badge-soft {% if r.status == 'ready' %}success{% elif r.status == 'error' %}danger{% else %}warn{% endif %}">
                  {{ r.get_status_display }}
                </span>
              </td>
              <td>
                <span class="badge-soft {% if r.validation_status == 'ok' %}success{% elif r.validation_status == 'warn' %}warn{% else %}danger{% endif %}">
                  {{ r.get_validation_status_display }}
                </span>
                <div class="small text-muted">{{ r.validation_message|default:"—" }}</div>
              </td>
              <td>{% if r.file %}<a href="{{ r.file.url }}" class="text-decoration-none">Скачать</a>{% else %}—{% endif %}</td>
              <td class="text-end">
                <form method="post" action="/reports/{{ r.id }}/validate/" class="d-inline">
                  {% csrf_token %}
                  <button class="btn btn-sm btn-outline-secondary">Проверить</button>
                </form>
                <a class="btn btn-sm btn-outline-secondary" href="/reports/{{ r.id }}/edit/">Изменить</a>
              </td>
            </tr>
          {% empty %}
            <tr><td colspan="6" class="text-muted">Отчётов нет</td></tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
{% endblock %}
```
