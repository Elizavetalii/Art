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
