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
