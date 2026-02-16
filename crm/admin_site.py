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
