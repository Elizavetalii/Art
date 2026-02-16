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
