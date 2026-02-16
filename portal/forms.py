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
