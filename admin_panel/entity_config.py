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
